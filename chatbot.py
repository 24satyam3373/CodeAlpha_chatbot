def chatbot():
    print(" Welcome! I am CodeBot. Type 'bye' to exit.")
    
    while True:
        user_input = input("You: ").lower()

        if "hello" in user_input:
            print("CodeBot: Hi there!")
        elif "how are you" in user_input:
            print("CodeBot: I'm doing great, thank you!")
        elif "bye" in user_input:
            print("CodeBot: Goodbye! Have a nice day.")
            break
        else:
            print("CodeBot: I'm not sure how to respond to that.")

chatbot()
