def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def num_words(title):
    num = 0
    book = get_book_text("books/frankenstein.txt")
    text = str.split(book)
    for word in text:
        num += 1
    return num

def main():
    print(f"{num_words} words found in the document")

main()
