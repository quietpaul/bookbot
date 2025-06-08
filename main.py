import sys
from stats import num_words, num_chars, get_book_text, sort_on, sort_list

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    book = get_book_text(book_path)
    word_count = num_words(book)
    unsorted_dict = num_chars(book)
    sorted_list = sort_list(unsorted_dict)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for item in sorted_list:
        if item["char"].isalpha():
            print(f'{item["char"]}: {item["num"]}')
    print("============= END ===============")
    

main()
