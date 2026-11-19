from dotenv import load_dotenv
import os


def main() -> None:
    load_dotenv()

    print("Hello from LangChain Course!")

    api_key = os.getenv("XAI_API_KEY")
    print("Grok API key loaded:", bool(api_key))


if __name__ == "__main__":
    main()