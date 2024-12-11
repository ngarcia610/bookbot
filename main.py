
def print_book():
    with open("books/frankenstein.txt") as f:
      file_contents = f.read()
    return file_contents

def word_count(text):
    return len(text.split())

book1 = print_book()
words = word_count(book1)

#print(book1)
print(words)
