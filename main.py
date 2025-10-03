
from stats import get_book_text, get_num_words, count_chars, sort_char_counts
import sys 

print(f"sys.argv :{sys.argv}")

arguments = sys.argv[0:]
print(f"argument length: {len(arguments)}")
print(f"arguments: {arguments}")
if len(arguments) != 2:
    print(f"Error: Two argument is required. Usage: python3 main.py <path_to_book>")
    sys.exit(1)
def main():
    book_path = arguments[1]
    book_text = get_book_text(book_path)
    num_words = get_num_words(book_text)      
    char_counts  = count_chars(book_text)

    sorted_chars = sort_char_counts(char_counts)
   
    
    print("============ BOOKBOT ===========")
    print(f"Analyzing book found at {book_path}")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in sorted_chars:
        ch = item["char"]
        if ch.isalpha():
            print(f"{ch}: {item['num']}")
    print("============= END ===============")

if __name__ == "__main__":
    main()

