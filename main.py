from agents.agent import initialize_agent
from langchain_core.tools import create_retriever_tool
from langchain.schema import StrOutputParser

def main() -> None:
    parser = StrOutputParser()

    done = False
    executor = initialize_agent()

    print("Initializing console")
    while not done:
        question = input("User: ")
        if question.lower() == "quit":
            done = True
        else:
            prompt = f"Given the prompt the user will give you, you analyze what he is asking and you answer his request,then, you need to save this prompt in a file.the prompt:{question}"
            result = executor.invoke({"input":prompt})

            print("Agent: ")
            print(result["output"])

    exit(0)


if __name__ == "__main__":
    main()
