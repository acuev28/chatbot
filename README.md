# Chatbot Project

This is a simple chatbot program that offers two modes:
- **ELIZA (Rule-based)** chatbot
- **Corpus-based** chatbot using a language model with sentence embeddings.

## Features

- ELIZA-style rule-based conversation.
- Corpus-based conversation using semantic similarity (Sentence Transformers).
- Regex-based detection to end conversations ("bye", "exit").

- Choose your chatbot:
    - Type `1` for ELIZA (rule-based chatbot).
    - Type `2` for Corpus-based chatbot.

-Chat normally.  
   To end the conversation, type **"bye"** or **"exit"**.

## Notes
- The corpus-based model uses **Sentence Transformers** for understanding meaning instead of exact word matching.
- ELIZA is based on simple rule patterns and keyword detection.
