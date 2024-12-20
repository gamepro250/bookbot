def main():
    book_path = "books/frankenstein.txt"

    text = get_book_text(book_path)   
    num_words = word_count(text)
    character_count = char_count(text)
    character_list = list_of_dicts(character_count)
    character_list.sort(reverse=True, key=sort_on)
    
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document\n")
    for char in character_list:
        print(f"The '{char["char"]}' character was found {char["num"]} times")
    print("--- End report ---")

def get_book_text(book):
    with open(book) as f:
        return f.read()

def word_count(text):
    words = text.split()
    return len(words)

def char_count(text):
    char_dict = {}
    letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", 
               "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    
    for char in text:
        char = char.lower()
        if char in letters:
            if char in char_dict:
                char_dict[char] += 1
            else:
                char_dict[char] = 1
    
    return char_dict

def list_of_dicts(dict):
    return [{"char": k, "num": v} for k, v in dict.items()]

def sort_on(dict):
    return dict["num"]

main()