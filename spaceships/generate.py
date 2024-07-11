import shutil
from os import path
from pathlib import Path
from typing import Dict, List, Optional, Tuple

import requests
from dotenv import load_dotenv
from openai import OpenAI

if load_dotenv():
    print("Parsed .env file successfully")
else:
    print("Did not find .env file")

client = OpenAI()


role = "You are a writer of science-fiction novels. You like to use complex character names and invent new technologies for your books. Unless otherwise specified, all responses should be formatted in github markdown. Do not include text like `sure I can do that` in the response. only include the generated content."
name_and_crew_prompt = "I'd like help writing a novel about a theoretical spaceship, its crew, and its adventures.  Can you help with this?  Can you start with a name for the spaceship and create a list of characters with details about each character? The characters do not necessarily need to be human."
name_as_snake_case_prompt = "Can you provide me the spaceship name in snake_case. Please only provide the name and do not format it in markdown."

chapter_summaries_prompt = "Next lets start to figure out the plot of the book. Please write a list of chapters and a short summary for each. Chapters should be numbered with sequential integers starting at 1."

chapter_count_prompt = "How many chapters are there in the book? Please only provide the number of chapters. Like just the integer value. Example response: 15"

chapter_image_prompt = "Now that you have finished writing the chapter, is there some moment in the chapter that you could capture in an image? If yes, please write a prompt for DALL-E 3 to use to generate the image. If not, please just return 'no'"
front_cover_prompt = "Now that we know the name of the spaceship and the crew, please write a prompt for DALL-E 3 to generate an image for the front cover of the book."
back_cover_prompt = "Now that we know the outline of the book, please write a prompt for DALL-E 3 to generate an image for the back cover of the book."

epilog_prompt = (
    "We have finished writing all the chapters. Now write an epilog for the book."
)


def chapter_outline_prompt(chapter: int):
    return f"Using the chapter summaries and crew info, expand on the plot for chapter: {chapter}, by making an outline of everything you want to cover in the chapter"


part_counts_prompt = "How many sections are in this outline? Please only provide the number of sections. Like just the integer value. Example response: 7"


def chapter_part_prompt(chapter: int, part: int):
    return f"Using the chapter summaries and the outline of chapter {chapter}, write the text for part {part} of the outline."


def get_next_response(prompt, previous_pairs: Optional[List[Tuple[str, str]]] = []):

    messages = [{"role": "system", "content": role}]

    for previous_pair in previous_pairs:
        messages.append({"role": "user", "content": previous_pair[0]})
        messages.append({"role": "assistant", "content": previous_pair[1]})

    messages.append({"role": "user", "content": prompt})

    response = client.chat.completions.create(
        model="gpt-4o",
        messages=messages,
        temperature=1,
        max_tokens=4096,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
    )
    return response.choices[0].message.content


def generate_image(description, save_path):
    response = client.images.generate(
        model="dall-e-3",
        prompt=description,
        size="1792x1024",
        quality="hd",
        n=1,
    )

    image_url = response.data[0].url
    try:
        response = requests.get(image_url, stream=True)
        response.raise_for_status()

        with open(save_path, "wb") as out_file:
            shutil.copyfileobj(response.raw, out_file)

        print(f"Image successfully saved to {save_path}")
    except requests.exceptions.RequestException as e:
        print(f"Error fetching the image: {e}")


def generate_novel():
    print(f"Generating the name of the spaceship and the characters for the book.")
    name_and_crew = get_next_response(name_and_crew_prompt)

    previous_pairs = [(name_and_crew_prompt, name_and_crew)]

    name_as_snake_case = get_next_response(
        name_as_snake_case_prompt, previous_pairs=previous_pairs
    )

    book_path = name_as_snake_case
    contents_path = path.join(book_path, "contents")

    Path(contents_path).mkdir(parents=True, exist_ok=True)

    with open(path.join(book_path, "name_and_crew.md"), "w") as f:
        f.write(name_and_crew)

    print(f"Generating an image for the front cover of the book")

    front_cover = get_next_response(front_cover_prompt, previous_pairs=previous_pairs)
    generate_image(front_cover, save_path=path.join(contents_path, f"front_cover.png"))

    print(f"Generating short summaries of each chapter")
    chapter_summaries = get_next_response(
        chapter_summaries_prompt, previous_pairs=previous_pairs
    )

    with open(path.join(book_path, "chapter_summaries.md"), "w") as f:
        f.write(chapter_summaries)

    previous_pairs.append((chapter_summaries_prompt, chapter_summaries))

    chapter_count = get_next_response(
        chapter_count_prompt, previous_pairs=previous_pairs
    )
    chapter_count = int(chapter_count.strip())

    print(f"Story {name_as_snake_case} will have {chapter_count} chapters.")

    chapter_outlines: Dict[int, str] = {}

    chapter_outline_pairs = previous_pairs

    with open(path.join(book_path, "plot_outline.md"), "w") as f:
        for chapter in range(1, chapter_count + 1):
            outline_prompt = chapter_outline_prompt(chapter)
            outline = get_next_response(
                outline_prompt, previous_pairs=chapter_outline_pairs
            )
            chapter_outline_pairs.append((outline_prompt, outline))
            f.write(outline + "\n")
            chapter_outlines[chapter] = outline
            print(f"Finished building outline of chapter {chapter}")

    print(f"Generating an image for the back cover of the book")

    front_cover = get_next_response(back_cover_prompt, previous_pairs=previous_pairs)
    generate_image(front_cover, save_path=path.join(contents_path, f"back_cover.png"))

    for chapter in range(1, chapter_count + 1):
        chapter_part_pairs = previous_pairs
        chapter_part_pairs.append(
            (chapter_outline_prompt(chapter), chapter_outlines[chapter])
        )

        parts_count = get_next_response(
            part_counts_prompt, previous_pairs=chapter_part_pairs
        )
        parts_count = int(parts_count.strip())
        print(f"Found {parts_count} parts for chapter {chapter}.")

        parts_moving_window_pairs = []

        with open(path.join(contents_path, f"chapter_{chapter}.md"), "w") as f:
            for part_index in range(1, parts_count + 1):
                part_prompt = chapter_part_prompt(chapter=chapter, part=part_index)
                part_text = get_next_response(
                    part_prompt,
                    previous_pairs=chapter_part_pairs + parts_moving_window_pairs,
                )
                parts_moving_window_pairs.append((part_prompt, part_text))
                if len(parts_moving_window_pairs) > 3:
                    parts_moving_window_pairs.pop(0)
                f.write(part_text + "\n")
                print(f"\tFinished writing part {part_index}")

        print(f"\tChecking if we should generate an image for the chapter")
        description = get_next_response(
            chapter_image_prompt, previous_pairs=chapter_part_pairs
        )

        if len(description) > 50:
            print(f"\tGenerating an image for the chapter")
            generate_image(
                description,
                save_path=path.join(contents_path, f"chapter_{chapter}.png"),
            )

    print(f"Writing the book epilog.")
    epilog = get_next_response(epilog_prompt, previous_pairs=chapter_outline_pairs)
    with open(path.join(contents_path, f"epilog.md"), "w") as f:
        f.write(epilog)


generate_novel()
