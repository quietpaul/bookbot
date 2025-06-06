from stats import num_words
from stats import num_chars
from stats import get_book_text
from stats import sort_on

def main():
    book = get_book_text("books/frankenstein.txt")
    word_count = num_words(book)
    unsorted = num_chars(book)
    print(f"{word_count} words found in the document")
    print(unsorted.sort(reverse=True, key=sort_on))
    

main()
