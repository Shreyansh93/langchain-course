from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_xai import ChatXAI
from langchain_ollama import ChatOllama
import os


def main() -> None:
    load_dotenv()

    print("Hello from LangChain Course!")

    api_key = os.getenv("XAI_API_KEY")
    print("Grok API key loaded:", bool(api_key))


    information = "You are a helpful assistant that can answer questions about the weather."

    summary_template = """
    Summarize the following information:
    {information}
    1. Give a short summary of the information.
    2. Give a list of the key points of the information.
    3. Give a list of the key questions that the information answers.
    4. Give a list of the key answers that the information provides.
    5. Give a list of the key recommendations that the information provides.
    6. Give a list of the key actions that the information provides.
    7. Give a list of the key outcomes that the information provides.
    8. Give a list of the key follow-up actions that the information provides.
    9. Give a list of the key follow-up questions that the information provides.
    """

    summary_prompt_template = PromptTemplate.from_template(template=summary_template)

    #llm = ChatXAI(model="grok-2-1212", temperature=0.0, api_key=api_key)

    llm = ChatOllama(model="gemma3:270m", temperature=0.0)
    
    chain = summary_prompt_template | llm

    response = chain.invoke({"information": information})

    print(response.content)

if __name__ == "__main__":
    main()