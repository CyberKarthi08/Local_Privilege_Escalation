from colorama import Fore, Style, init
import random

# Initialize colorama
init(autoreset=True)

# Define a list of color options
COLORS = [
    Fore.RED
]

def colorize_text(text):
    # Split the text into words
    words = text
    
    # Create a colored version of each word
    colored_words = []
    color = random.choice(COLORS)
    colored_words.append(f"{color}{words}")

    # Join the colored words back into a single string
    return ' '.join(colored_words)

if __name__ == "__main__":
    text = "This is a sample text to demonstrate colored words."
    colored_text = colorize_text(text)
    print(colored_text)