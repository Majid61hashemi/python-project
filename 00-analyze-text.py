f = 'text.txt'
unique_words = {}
for line in open(f):
    seq = line.split()
    for word in seq:
        unique_words[word] = 1

print(len(unique_words))
print(sorted(unique_words, key=len)[-5:])