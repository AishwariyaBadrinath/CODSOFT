def chatbot():
    print("Chatbot: Hello! I am a rule-based chatbot.")
    print("Chatbot: Type 'exit' to end the conversation.\n")

    while True:
        user_input = input("You: ").lower()
        if user_input == "exit":
            print("Chatbot: Goodbye! Have a nice day.")
            break

        elif "hello" in user_input or "hi" in user_input or "hey" in user_input:
            print("Chatbot: Hello! How can I help you?")

        elif "who are you" in user_input or "what are you" in user_input:
            print("Chatbot: I am a simple rule-based chatbot created using Python.")

        elif "help" in user_input:
            print("Chatbot: I can answer basic questions like greetings, information, and guidance.")

        elif "ai" in user_input or "artificial intelligence" in user_input:
            print("Chatbot: Artificial Intelligence is the simulation of human intelligence in machines.")

        elif "internship" in user_input:
            print("Chatbot: Internships help students gain real-world experience and skills.")

        elif "thank" in user_input:
            print("Chatbot: You're welcome!")

        elif "bye" in user_input or "goodbye" in user_input:
            print("Chatbot: Goodbye! Take care.")

        else:
            print("Chatbot: Sorry, I don't understand that. Please try something else.")
        
chatbot()
