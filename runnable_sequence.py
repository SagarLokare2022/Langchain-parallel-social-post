from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain_core.runnables.base import RunnableSequence

load_dotenv()

prompt1 = PromptTemplate(
    template= "tell me a joke about {topic}",
    input_variables=["topic"]
)
prompt2 = PromptTemplate(
    template= "explain the text in a summary {text}",
    input_variables=["text"]
)


llm = ChatOpenAI()
parser = StrOutputParser()

chain1 = RunnableSequence(prompt1, llm, parser)
joke = chain1.invoke({"topic": "AI"})
print("Joke:\n", joke, "\n")

chain2 = RunnableSequence(prompt2, llm, parser)
summary = chain2.invoke({"text": joke})
print("Summary:\n", summary)

print(chain1.get_graph().print_ascii())
print(chain2.get_graph().print_ascii())


