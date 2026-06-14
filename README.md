# Self-RAG: Self-Reflective Retrieval-Augmented Generation

[![Python Version](https://img.shields.io/badge/python-3.9%2B-blue.svg)](https://www.python.org/)
[![Framework](https://img.shields.io/badge/Framework-LangChain%20%2F%20LangGraph-orange)](https://github.com/langchain-ai/langgraph)

An implementation of **Self-RAG**, an advanced, self-reflective Retrieval-Augmented Generation framework. Instead of blindly trusting retrieved documents, this system uses a critique-driven reflection mechanism to dynamically judge retrieval necessity, evaluate document relevance, filter internal knowledge chunks, and trigger fallback web search when local context falls short.

---

## 🚀 Overview

Traditional RAG often suffers from over-retrieval (fetching documents unnecessarily) or generating answers based on irrelevant, noisy snippets. 

**Self-RAG** solves this by introducing an explicit **Retrieval Evaluator** and a multi-tiered **Knowledge Correction** loop before the text ever hits the final Generator.

---

## 🏗️ System Architecture
<img width="787" height="572" alt="image" src="https://github.com/user-attachments/assets/11261ed0-69ac-4833-866a-7ab94238297c" />

The complete workflow of the architecture is detailed in the pipeline diagram below:

<p align="center">
  <img src="image_1dcf37.jpg" alt="Self-RAG Knowledge Correction and Generation Architecture" width="85%"/>
</p>

### Pipeline Breakdown:

1. **Retrieval Stage:** 
   * Given a user query $x$ (e.g., *"Who was the screenwriter for Death of a Batman?"*), the system fetches initial raw documents ($d_1, d_2$).
2. **Knowledge Correction Stage:**
   * A **Retrieval Evaluator** assesses the documents with the core question: *Are the retrieved documents correct and sufficient for $x$?*
   * **Correct Branch (Knowledge Refinement):** If relevant, documents are decomposed into fine-grained snippets ($\text{strip}_1, \text{strip}_2, \dots, \text{strip}_k$), filtered for quality, and recomposed into clean internal knowledge ($k_{\text{in}}$).
   * **Incorrect/Ambiguous Branch (Knowledge Searching):** If the internal documents are noisy, lacking, or ambiguous, the query is rewritten into an optimized search query $q$ to trigger an external **Web Search**, selecting highly relevant external knowledge ($k_{\text{ex}}$).
3. **Generation Stage:**
   * The final **Generator** is dynamically fed the optimal context combinations depending on the evaluation state:
     * **Correct:** Query ($x$) + Refined Internal Knowledge ($k_{\text{in}}$)
     * **Ambiguous:** Query ($x$) + $k_{\text{in}}$ + External Knowledge ($k_{\text{ex}}$)
     * **Incorrect:** Query ($x$) + External Knowledge ($k_{\text{ex}}$)

---

## ✨ Features

* **Adaptive Retrieval & Filtering:** Strips away irrelevant text fragments, passing only verified information tokens downstream.
* **Autonomous Knowledge Correction:** Dynamically detects ambiguities and fallbacks to internet/web-search mid-flight.
* **State-Graph Implementation:** Fully deterministic routing built via cyclic graphs to prevent infinite generation loops.

---

## 🛠️ Installation

1. **Clone the repository:**
```bash
   git clone [https://github.com/yourusername/self-rag.git](https://github.com/yourusername/self-rag.git)
   cd self-rag
