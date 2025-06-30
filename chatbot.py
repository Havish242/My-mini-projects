from transformers import pipeline
chatbot = pipeline("text-generation", model="microsoft/DialoGPT-small")

while True:
    user_input = input("You: ")
    if user_input.lower() in ["quit", "exit"]:
        print("Chatbot: Goodbye!")
        break
    response = chatbot(user_input, max_length=50, num_return_sequences=1)
    print("Chatbot:", response[0]['generated_text'])
