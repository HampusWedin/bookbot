def main():
    book_path = "books/frankenstein.txt"
    text = read_book_text(book_path)
    #print(text)
    no_of_words = count_words(text)
    char_count = count_characters(text)
    sorted_list = sort_list(char_count)

    # Print a book report   
    print(f"--- Begin report of {book_path} ---")
    print(f"{no_of_words} words found in the document")
    print()
    for char in sorted_list:
        print(f"The '{char['character']}' character was found {char['count']} times")
    print("--- End report ---")



def count_words(text):
    counter = 0
    for words in text.split():
        counter +=1
    return counter

def read_book_text(path):
    with open(path) as f:
        return f.read()

def count_characters(text):
    # function to count number of times each character occurs in book. 
    # function also sorts
    
    char_count = {}
    
    for char in text:
        if char.lower() in char_count:
            char_count[char.lower()] +=1
        else:
            char_count[char.lower()] = 1
    sorted_char_count = dict(sorted(char_count.items()))
    return sorted_char_count

def sort_on(char_count):
     # defines sort for "count", for list sorting
     return char_count["count"]

def sort_list(list):
    # sorts a list of dictionaries with "count" as a key (int). Also cleans list from non-alphabetical
    # characters
    
    sorted_list = []
    for char in list:
        if char.isalpha():
            sorted_list.append({"character" : char, "count" : list[char]}) 

    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

main()