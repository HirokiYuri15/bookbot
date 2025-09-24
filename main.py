from pathlib import Path
import sys
from stats import *


def main():
    if len (sys.argv) < 2:
        print ("usage: Usage: python3 main.py <path_to_book>")
        sys.exit(1)
        
    file_name = sys.argv[1]
    ready_dicts_list = sorted_dict(file_name)
        
    print ("============ BOOKBOT ============")
    print (f"Analyzing book found at books/{file_name}...")
    print ("----------- Word Count ----------")
    print (f"Found {getting_wc(file_name)} total words")
    print ("--------- Character Count -------")
    for dicte in ready_dicts_list:
        chr_type = dicte ["char"]
        chr_count = dicte ["num"]
        print (f"{chr_type}: {chr_count}")
    print ("============= END ===============")
        

if __name__ == "__main__":
    main()