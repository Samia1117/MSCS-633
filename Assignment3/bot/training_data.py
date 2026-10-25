"""
Training conversations for the chatbot.

Each inner list is one conversation. ListTrainer treats every line as a
reply to the line before it, so the order matters.
"""

CONVERSATIONS = [
    # The example dialog from the assignment
    [
        "Good morning! How are you doing?",
        "I am doing very well, thank you for asking.",
        "You're welcome.",
        "Do you like hats?",
    ],
    [
        "Hello",
        "Hi there! How can I help you today?",
        "What is your name?",
        "I am a simple chatbot built with ChatterBot and Django.",
    ],
    [
        "Hi",
        "Hello! Nice to meet you.",
        "Nice to meet you too.",
        "What do you like to talk about?",
    ],
    [
        "How are you?",
        "I am doing well, thanks. How about you?",
        "I am fine.",
        "Glad to hear that.",
    ],
    [
        "Good afternoon",
        "Good afternoon! How is your day going?",
        "It is going well.",
        "That is great to hear.",
    ],
    [
        "Good evening",
        "Good evening! Did you have a good day?",
        "Yes, I did.",
        "Wonderful. Do you like hats?",
    ],
    [
        "Do you like hats?",
        "I think hats are great, especially on a sunny day.",
        "What is your favorite color?",
        "I like blue. What about you?",
    ],
    [
        "What can you do?",
        "I can chat with you about simple things like greetings and hobbies.",
        "That is cool.",
        "Thanks! Ask me anything.",
    ],
    [
        "Thank you",
        "You're welcome.",
        "Thanks for the help.",
        "Anytime!",
    ],
    [
        "What is artificial intelligence?",
        "It is the field of making computers do things that normally need human intelligence.",
        "Is it hard to learn?",
        "It takes practice, but it is a fun subject.",
    ],
    [
        "Tell me a joke",
        "Why do programmers prefer dark mode? Because light attracts bugs.",
        "Haha, that was funny.",
        "I am glad you liked it.",
    ],
    [
        "Goodbye",
        "Goodbye! Have a nice day.",
        "Bye",
        "See you later.",
    ],
]
