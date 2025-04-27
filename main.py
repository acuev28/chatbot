import eliza 
import re
import pandas as pd
import numpy as np
from datetime import datetime
from sentence_transformers import SentenceTransformer, util

def is_end(input_string):
    # This will check if the user wants to end conversation with the chatbot
    pattern = re.compile(r'(bye|exit)\b', re.IGNORECASE)
    if pattern.search(input_string):
        return True
    return False


def rule_based():
    eliza_chat = eliza.Eliza() # load the model

    # Start the chat
    while True:
        user_input = input("\nYou: ")

        # print(f"\nUser: {user_input}")

        # If the user wants to end chat by typing ("bye" or "exit")
        if is_end(user_input):
            print("Agent: Goodbye!")
            break
        # Get ELIZA response
        eliza_response = eliza_chat.respond(user_input)
        print(f"Agent: {eliza_response}")


def main():
    print("What type of chatbot would you like to chat with?\n")
    print("1: ELIZA (Rule-based)")
    print("2: Corpus Based")

    user_choice = input("Enter your chatbot choice: ")

    if (user_choice == "1"):
        rule_based()

main()