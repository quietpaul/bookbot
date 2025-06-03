from stats import num_words
from stats import get_book_text

def main():
    book = get_book_text("books/frankenstein.txt")
    word_count = num_words(book)
    print(f"{word_count} words found in the document")
    print(chars(book))

main()
