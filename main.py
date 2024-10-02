def main():
    book_path = 'books/frankenstein.txt'
    text = get_book_text(book_path)
    word_count = get_word_count(text)
    characters_dict = get_characters_count(text)
    sorted_characters_list = convert_dictonary_to_sorted_list(characters_dict)
    print_book_report(book_path, sorted_characters_list)
    
def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_word_count(text):
    return len(text.split())

def get_characters_count(text):
    chars = {}
    for char in text:
        if char.lower() in chars:
            chars[char.lower()] += 1
        else:
            chars[char.lower()] = 1
    return chars
        
def sort_on(d):
    return d["num"]

def convert_dictonary_to_sorted_list(dict):
    sorted = []
    for c in dict:
        sorted.append({"char": c, "num": dict[c]})
    sorted.sort(reverse=True, key=sort_on)
    return sorted
        
def print_book_report(path, list):
    print(f'--- Begin report of {path} ---')
    for item in list:
        if item["char"].isalpha():
            print(f"The '{item['char']}' character was found {item['num']} times")
    print("--- End report ---")
    
main()