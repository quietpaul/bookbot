def get_book_text(path_to_book):
    with open(path_to_book) as f:
        text = f.read()
    return text

def num_words(text):
    word_count = 0
    words = text.split()
    for word in words:
        word_count += 1
    return word_count

def num_chars(text):
    letters = {}
    for char in text:
        if letters[char] == False:
            letters[char] += 1
        return letters
