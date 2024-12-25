import os
import string

def read_file(file_path):
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"The file at '{file_path}' does not exist.")
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

def split_line(line):
    return line.replace('-', ' ').split()

def clean_text(text):
    translator = str.maketrans('', '', string.punctuation)
    words = text.translate(translator).split()
    return words.lower()

input_path = input("Enter input file path: ").strip()
text = read_file(input_path)

for line in open(input_path):
        print(clean_text(line))

word_counter = {}
for line in open(input_path):
    for word in split_line(line):
        word = clean_text(word)
        if word not in word_counter:
            word_counter[word] = 1
        else:
            word_counter[word] += 1

def second_element(t):
    return t[1]
def print_most_common(word_counter, num=5):
    items = sorted(word_counter.items(), key=second_element, reverse=True)

    for word, freq in items[:num]:
        print(freq, word, sep='\t')

print_most_common(word_counter, 3)