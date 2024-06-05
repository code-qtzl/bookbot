def main():
    path = "./books/frankenstein.txt"
    word = read_book(path)
    content = count_content(word)
    letters = count_letters(word)
    char_data = generate_char_data(letters)
    report = compile_report(content, char_data)
    print(report)

def read_book(path):
    # Reads the content in the book
    with open(path) as f:
        file_contents = f.read()
    return file_contents

def count_content(word):
    # Takes the text from the book as a string, and returns the number of words in the string
    content = word.split()
    return len(content)

def count_letters(word):
    # Takes the text from the book as a string, and returns the number of times each character appears in the string. Also, takes any character and converts it to lowercase, and removed duplicates.
    word = ''.join(filter(str.isalpha, word.lower()))
    letters_dict = {}
    for letter in word:
        if letter in letters_dict:
            letters_dict[letter] += 1
        else:
            letters_dict[letter] = 1
    return letters_dict

def get_value(item):
    # The purpose of this function is to be passed to the sorted function as the key argument. found in line 39
    return item[1]

def generate_char_data(letters):
    # Takes the letters dictionary as input, sorts the letters by frequency, and generates the character frequency data string
    chars_data = ""
    sorted_letters = sorted(letters.items(), key=get_value, reverse=True)

    for char, count in sorted_letters:
        char_data = f"The '{char}' character was found {count} times\n"
        chars_data += char_data

    return chars_data

def compile_report(content, char_data):
    # Takes the word count and the character frequency data as input, and compiles the final report string
    return f"--- Begin report of books/frankenstein.txt ---\n{content} content found in the document\n\n{char_data}--- End report ---"

main()