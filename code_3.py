import random

# List of jokes
jokes = [
    "Why do Python programmers wear glasses? Because they can't C!",
    "I told my computer I needed a break, and now it won’t stop sending me KitKat ads.",
    "Why did the programmer quit his job? Because he didn’t get arrays.",
    "Debugging: Being the detective in a crime movie where *you* are also the murderer.",
    "Why do Java developers wear glasses? Because they don’t see sharp.",
    "How many programmers does it take to change a light bulb? None. That’s a hardware problem.",
    "There are 10 types of people in the world: those who understand binary and those who don’t.",
    "Why was the function sad after its breakup? Because it had too many arguments.",
    "What do you call a Python snake that works on your computer? A Python script!",
    "I would tell you a recursion joke... but you'd have to hear it again."
]

# Pick a random joke
joke = random.choice(jokes)

# Display the joke
print("😂 Here's your random programming joke:\n")
print(joke)
