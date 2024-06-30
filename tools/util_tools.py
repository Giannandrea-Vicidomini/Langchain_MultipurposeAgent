import os
from langchain_core.tools import tool

@tool
def save_user_input(user_text:str):
    """
    This tool should be used whenever the prompt issued by the user needs to be saved
    args:
        user_text: The text that the user gave the model as an input
    """
    with open(".\\user_inputs.txt","a") as file:
        file.write("user input: "+user_text)
        file.write("\n")
