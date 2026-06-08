import random

def main():
    """
    A simple rule-based chatbot demonstrating basic control flow,
    conditional logic, and interactive loops in Python.
    """
    # Greeting variations to avoid repeating the exact same response
    greeting_responses = [
        "Hello! How can I help you today?",
        "Hi there! Nice to meet you.",
        "Hey! Great to chat with you."
    ]

    print("==================================================")
    print("             Simple Rule-Based Chatbot            ")
    print("==================================================")
    print("Type your message below. Type 'exit' to quit.")
    print("==================================================")

    # Continuous loop keeping the chatbot active
    while True:
        # Prompt user for input
        try:
            user_input = input("\nYou: ")
        except (KeyboardInterrupt, EOFError):
            print("\nBot: Goodbye!")
            break

        # Process input to ensure case-insensitivity and clean up leading/trailing spaces
        cleaned_input = user_input.strip().lower()

        # Conditional logic to route responses using standard if-elif-else
        if cleaned_input in ["exit", "quit", "bye"]:
            # Gracefully break the loop and terminate the program
            print("Bot: Goodbye! Have a great day!")
            break
        
        elif cleaned_input in ["hello", "hi", "hey"]:
            # Respond warmly using a randomized greeting variation
            response = random.choice(greeting_responses)
            print(f"Bot: {response}")
            
        else:
            # Fallback response for unrecognized inputs
            print("Bot: I'm sorry, I didn't quite understand that. Try saying 'hello' or 'exit'.")

if __name__ == "__main__":
    main()
