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
    lower = text.lower()
    for char in lower:
        if char in letters:
            letters[char] += 1
        else:
            letters[char] = 1
    return letters

def sort_on(dict):
    return dict["num"]

def sort_list(dict):
    final_list = []
    for item in dict:
        final_list.append({
            "char" : item,
            "num" : dict[item],
        })
    final_list.sort(reverse=True, key=sort_on)
    return final_list
