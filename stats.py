from main import get_book_text

def num_words(text):
    count = 0
    words = text.split()
    for word in words:
        count += 1
    return count

def num_chars(text):
    chars = {}
    words = get_book_text(text)
    for char in words:
        if blah:
            chars[char] = 
