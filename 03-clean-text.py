import os
import string

def read_file(file_path):
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"The file at '{file_path}' does not exist.")
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()


def clean_text(text):
    translator = str.maketrans('', '', string.punctuation)
    words = text.translate(translator).split()
    return words

input_path = input("Enter input file path: ").strip()
text = read_file(input_path)

for line in open(input_path):
        print(clean_text(line))