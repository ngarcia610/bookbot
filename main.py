import json

BOOK_PATH = "books/frankenstein.txt"

def print_book(path):
    with open(path) as f:
      return f.read()

def word_count(text):
    return len(text.split())

def char_count(text):
    char_dict = {
        'a': 0,
        'b': 0,
        'c': 0,
        'd': 0,
        'e': 0,
        'f': 0,
        'g': 0,
        'h': 0,
        'i': 0,
        'j': 0,
        'k': 0,
        'l': 0,
        'm': 0,
        'n': 0,
        'o': 0,
        'p': 0,
        'q': 0,
        'r': 0,
        's': 0,
        't': 0,
        'u': 0,
        'v': 0,
        'w': 0,
        'x': 0,
        'y': 0,
        'z': 0
    }
    text = text.lower()
    for word in text:
        for char in word:
            for key, value in char_dict.items():
                if key == char:
                    char_dict[key] += 1
    return char_dict

book = print_book(BOOK_PATH)
words = word_count(book)
chars = char_count(book)

# Print the entire book
#print(book)

# Print the number of words
print(f"The number of words in the text: {words}")

# Print the number of times each character appears
nice_chars = json.dumps(chars, indent=4, sort_keys=True)
print(f"The number of times each character appears in the text: \n {nice_chars}")