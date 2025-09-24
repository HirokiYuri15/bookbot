from pathlib import Path

books_dir = Path(__file__).resolve().parent / "books"

def _resolve (path_or_name: str | Path) -> Path:
    path = Path(path_or_name)
    if path.is_absolute() or path.exists():
        return path
    
    else:
        return (books_dir / path)

def get_book_text(file_path):
    path = _resolve(file_path)
    if path.exists():
        with open (path, "r", encoding="utf-8") as f:
            return f.read()
    else:
        raise Exception ("the error is coming from get_book_text || ")

def split_words(file_path):
    content = get_book_text(file_path=file_path)
    words = content.split()
    return words

def getting_wc(file_path):
    words_counted = len(split_words(file_path=file_path))
    print (f"{words_counted} words found in the document")
    return words_counted

def counting_characters(file_path):
    content = split_words(file_path=file_path)
    dictionary = {}
 
    
    for word in content:
        for chr in word.lower():
            if chr not in dictionary:  
               dictionary [chr] = 0
            
            dictionary [chr] += 1
            
    return dictionary     
                
def dict_list (file_path):
    dict_list = []
    dictionary = counting_characters(file_path=file_path)
    
    for key in dictionary:
        value = dictionary[key]
        new_dict = {"char":key, "num":value}
        dict_list.append(new_dict)
    return dict_list

def sort_on(items):
    value = items["num"]
    return value

def sorted_dict(file_path):
    dictionary = dict_list(file_path=file_path)
    dictionary.sort(reverse=True, key=sort_on)
     
    return dictionary
