from agents.agent import initialize_agent
from langchain_core.tools import create_retriever_tool


def main() -> None:
    done = False
    executor = initialize_agent()

    print("Initializing console")
    while not done:
        question = input("User: ")
        if question.lower() == "quit":
            done = True
        else:
            result = executor.invoke({"input":question})
            print("Agent: ")
            print(result)

    exit(0)


if __name__ == "__main__":
    main()
