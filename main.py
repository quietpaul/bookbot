from stats import num_words, num_chars, get_book_text, sort_on, sort_list

def main():
    book_path = "books/frankenstein.txt"
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
