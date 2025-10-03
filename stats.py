def get_book_text(filepath):
    with open(filepath) as file:
        file_contents  = file.read()
    return file_contents

def get_num_words(text:str) -> int: 
    words = text.split()
    return len(words)

def count_chars(text: str) -> dict[str, int]:
    counts = {}    
    for c in text.lower():
        if c.isalpha():  
            counts[c] = counts.get(c, 0) + 1
    return counts

def _sort_on(item):
    return item["num"]

def sort_char_counts(char_counts):
    items = []
    for ch, n in char_counts.items():
        items.append({"char": ch, "num": n})
    items.sort(key=_sort_on, reverse=True)
    return items