import os 
import string

def read_file(file_path):
    # Read and return the contents of a file
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"The file at '{file_path}' does not exist.")
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

def clean_text(text):
    # Clean text by removing punctuation .
    translator = str.maketrans('', '', string.punctuation)
    words = text.translate(translator).split()
    filtered_words =[word.lower() for  word in words]
    return filtered_words

input_path = input("Enter input file path: ").strip()
# Read files
text = read_file(input_path)
# Analyze rext
words = clean_text(text)
lines = text.splitlines()
sentences = text.split('.')

word_counter = {}
for word in words:
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

print_most_common(word_counter, 6)
