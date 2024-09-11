# AI-Powered Customer Support Tool Legal Documents

This folder contains a set of interrelated legal agreements drafted for a fictional project to develop an **AI-Powered Customer Support Tool**. These agreements are designed to test the capabilities of a **Graph RAG (Retrieval-Augmented Generation)** system by requiring cross-document references and complex relationships between sections. The documents include:

1. **Software Development Agreement (SDA)**
2. **Non-Disclosure Agreement (NDA)**
3. **Intellectual Property Licensing Agreement (IPLA)**
4. **Service Level Agreement (SLA)**

## Purpose

The documents are intended to serve as a realistic set of legal contracts governing the development, licensing, confidentiality, and support of the AI tool. Each document references sections in others, simulating a real-world scenario where legal agreements are interconnected and require detailed cross-referencing.

This structure will allow us to generate questions that require a **Graph RAG** system to correctly traverse and reference content across multiple documents, as opposed to simpler extraction techniques used by standard RAG systems.

---

## Document Descriptions

### 1. **Software Development Agreement (SDA)**
The **SDA** is the core contract governing the development of the AI-Powered Customer Support Tool. It details the scope of work, deliverables, payment terms, intellectual property rights, and confidentiality requirements.

Key sections:
- **Scope of Work**: Describes the AI tool’s features and phases of development.
- **Intellectual Property**: Cross-references the **IPLA** to define ownership rights.
- **Confidentiality**: Cross-references the **NDA** for handling sensitive data.
- **Support**: Cross-references the **SLA** to define post-deployment support and uptime expectations.

### 2. **Non-Disclosure Agreement (NDA)**
The **NDA** protects confidential information exchanged between the Developer and the Client during the course of the project.

Key sections:
- **Confidential Information**: References the **SDA** to define what information is considered confidential.
- **Breach and Remedies**: References the **SDA** to define the consequences of breaching confidentiality.

### 3. **Intellectual Property Licensing Agreement (IPLA)**
The **IPLA** governs the ownership and licensing of the AI models, source code, and other intellectual property developed during the project.

Key sections:
- **Ownership**: References the **SDA** to establish ownership rights after payment.
- **Licensing Terms**: Defines how the Client may use, modify, and distribute the licensed IP.
- **Confidentiality**: Cross-references the **NDA** to ensure proprietary information remains protected.

### 4. **Service Level Agreement (SLA)**
The **SLA** defines the performance metrics, uptime commitments, and support obligations for the AI-Powered Customer Support Tool after deployment.

Key sections:
- **Uptime Commitment**: Details the guaranteed uptime of the system.
- **Support and Response Times**: Specifies the response and resolution times for different issue severities.
- **Termination**: References the **SDA** for conditions under which the SLA may be terminated.

---

## Links Between Documents

The documents are interlinked to reflect real-world contractual relationships, requiring cross-referencing for certain terms and conditions. Here's an overview of the most important links between the documents:

1. **SDA and NDA**:
   - The **SDA's** confidentiality clause (**Section 7.1**) refers to the definitions of confidential information outlined in **Section 1.1** of the **NDA**.
   - The **NDA** specifies that breaches of confidentiality may result in termination of the **SDA** (**SDA Section 6.3**).

2. **SDA and IPLA**:
   - The **SDA** references the **IPLA** in **Section 4.1** to define intellectual property ownership upon project completion.
   - The **IPLA** confirms that certain IP rights are transferred upon the fulfillment of the payment terms in **SDA Section 5**.

3. **SDA and SLA**:
   - The **SDA** references the **SLA** in **Section 8.1** to define post-deployment support and uptime obligations.
   - The **SLA's** termination clause links to the **SDA's** breach terms in **Section 6.1**.

4. **NDA and IPLA**:
   - The **IPLA**'s confidentiality obligations (**Section 5.1**) refer to the **NDA**, specifically **Section 2.1**.

These links establish a complex web of interdependencies, making the set of documents an ideal test case for a **Graph RAG** system. Questions about intellectual property, confidentiality, or performance standards require the system to navigate across these documents and their respective sections.

---

## Example Queries

Here are some example questions that a **Graph RAG** system would need to answer by referencing multiple sections and documents:

1. **"What customer data needs to be protected during the development of the AI tool?"**
   - Requires referencing the **NDA’s** "Confidential Information" clause and the **SDA’s** project description.

2. **"Who owns the AI models after project completion?"**
   - Requires referencing the **IPLA's** "Ownership" clause and the **SDA's** payment completion terms.

3. **"What is the maximum response time for a critical issue?"**
   - Requires referencing the **SLA’s** response time for critical issues and potentially cross-checking it with the **SDA’s** post-deployment support section.

---

## Conclusion

These interconnected legal documents offer a robust test for a **Graph RAG** system by requiring the system to handle complex, multi-document references. By simulating a real-world project with legal agreements that span across several topics—confidentiality, intellectual property, and service expectations—the documents challenge the system to provide accurate, cross-referenced answers to detailed queries.

