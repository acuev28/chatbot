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

def get_response(user_input, data, model, user_embedding):
    # Convert the input of the user to its sentence embedding
    input_embedding = model.encode(user_input)
    
    # Compute cosine similarities
    cosine_scores = util.pytorch_cos_sim(user_embedding, input_embedding)
    
    # Find the index of the highest cosine similarity using np.argmax.
    best_match_idx = np.argmax(cosine_scores).item()
    
    # Return the corresponding string for the 'Agent' column
    return data.iloc[best_match_idx]["Agent"]


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

def corpus_based():
    data = pd.read_csv("dialogue.csv")
    model = SentenceTransformer("all-MiniLM-L6-v2")

    user_dialogue = data['User'].tolist()
    user_embeddings = model.encode(user_dialogue)



def main():
    print("What type of chatbot would you like to chat with?\n")
    print("1: ELIZA (Rule-based)")
    print("2: Corpus Based")

    user_choice = input("Enter your chatbot choice: ")

    if (user_choice == "1"):
        rule_based()
    elif (user_choice == "2"):
        corpus_based()


main()