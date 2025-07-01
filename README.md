#Project Goal:-
To build a simple conversational chatbot in Python that:
->Understands user input
->Responds in a natural, human-like way
->Maintains the conversation context

#Tech Stack:-
Language: Python
Library: Hugging Face Transformers
Model: microsoft/DialoGPT-small (a conversational version of GPT-2)
Backend: Command-line interaction (can be extended to GUI or web app)

##How It Works:-
-User inputs a message
The chatbot:
-Encodes the message using a tokenizer
-Combines it with previous conversation history
-Sends it to the DialoGPT model
-Decodes the model's response
-The response is printed to the user
-This loop continues until the user types quit

##Features:-
>Multi-turn chat (remembers the conversation)
>Natural, playful language generation
>Can tell jokes, chat casually, and respond creatively

!Limitations!:-
>Not reliable for factual questions (uses old training data)
>May output gibberish if chat history gets too long or if randomness settings are too high
>No built-in memory or internet access
>No understanding of real user intent (just text prediction)
