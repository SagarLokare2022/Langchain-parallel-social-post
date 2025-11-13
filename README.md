# 🚀 LangChain Runnables Demo – Parallel Social Post Generator

This project demonstrates practical hands-on experience with **LangChain 2.x Runnables**, showcasing how to build modular, composable LLM pipelines using `RunnableSequence` and `RunnableParallel`.

The script generates **two different social media posts in parallel** — a Tweet and a LinkedIn post — based on a user-provided topic.  
It also prints the **ASCII graph** of the chain, giving a visual understanding of the runnable flow.

---

## 🧠 What This Project Demonstrates

### ✔️ LangChain Concepts Used
- `PromptTemplate`
- `ChatOpenAI`
- `StrOutputParser`
- `RunnableSequence`
- `RunnableParallel`
- Runnable graph visualization (`print_ascii()`)

### ✔️ Skills Demonstrated
- Building runnable pipelines in LangChain  
- Running multiple LLM tasks *in parallel*  
- Handling outputs cleanly (tweet + LinkedIn post)  
- Using `.env` files for API key security  
- Writing clean, modular, production-style Python code  
- Using Git & GitHub professionally  

---

## 📂 Project Structure

```text
/Langchain-parallel-social-post/
│
├── runnable_parallel.py        # Main project file (parallel Tweet + LinkedIn)
├── runnable_sequence.py        # Demo for sequential runnable chain
├── runnable_lambda.py          # Demo using RunnableLambda
├── requirements.txt            # All dependencies
├── .gitignore                  # Protects secrets (.env)
└── .env                        # Your API key (not uploaded to GitHub)

![Chain Graph](assets/parallel_chain_graph.png)

