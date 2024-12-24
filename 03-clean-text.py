import unicodedata

path_f = 'text.txt'
punc_marks = {}
for line in open(path_f):
    for char in line:
        category = unicodedata.category(char)
        if category.startswith('P'):
            punc_marks[char] = 1

punctuation = ''.join(punc_marks)
print(punctuation)

def clean_word(word):
    return word.strip(punctuation).lower()

print(clean_word('“Behold!”'))