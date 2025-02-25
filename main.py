from stats import word_count, char_count, sort_dictionaries
import sys

def get_book_text(filepath):
    contents = ""

    with open(filepath) as f:
        contents = f.read()

    return contents

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    print("============ BOOKBOT ============")
    
    book = sys.argv[1]
    print(f"Analyzing book found at {book}...")

    print("----------- Word Count ----------")
    text = get_book_text(book)
    print(f"Found {word_count(text)} total words")

    print("--------- Character Count -------")
    char_count_dictionary = char_count(text)
    sorted_list = sort_dictionaries(char_count_dictionary)

    for entry in sorted_list:
        if entry["char"].isalpha():
            print(f"{entry["char"]}: {entry["count"]}")

    print("============= END ===============")

main()