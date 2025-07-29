import sys

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        book_contents = f.read()
    return book_contents

    
from stats import get_num_words

from stats import get_num_characters

from stats import sort_dictionary

def main():
    if len(sys.argv) < 2:
      print("Usage: python3 main.py <path_to_book>")
      sys.exit(1)
    else:
        text = get_book_text(sys.argv[1])
        num_words = get_num_words(text)
        num_characters = get_num_characters(text)
        sorted_characters = sort_dictionary(num_characters)
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {sys.argv[1]}...")
        print("----------- Word Count ----------")
        print(f"Found {num_words} total words")
        print("--------- Character Count -------")
        for char_dict in sorted_characters:
            char = char_dict["char"]
            count = char_dict["num"]
            if char.isalpha():
                print(f"{char}: {count}")
        print("============= END ===============") 
       

main()


