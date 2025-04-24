import eliza 
import re
import pandas as pd
import numpy as np
from datetime import datetime
from sentence_transformers import SentenceTransformer, util

def is_end(input_string):
    # This will check if the user wants to end conversation with the chatbot
    pattern = re.compile(r'\(bye|exit)\b', re.IGNORECASE)
    if pattern.search(input_string):
        return True
    return False

def rule_based():
    eliza = eliza.Eliza() # load the model



def main():
    print("What type of chatbot would you like to chat with?\n")
    print("1: ELIZA (Rule-based)\n2: Corpus Based\n")

    user_choice = input("Enter your chatbot choice: ")




main()