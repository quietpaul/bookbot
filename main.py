from stats import num_words

def get_book_text(path_to_book):
    with open(path_to_book) as f:
        text = f.read()
    return text

def main():
    book = get_book_text("books/frankenstein.txt")
    word_count = num_words(book)
    print(f"{word_count} words found in the document")

main()
