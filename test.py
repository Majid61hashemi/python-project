
# # def clean_word(word):
# #     return word.strip('!?."#$%&').lower()

# # print(clean_word('Majid?%.'))
# # import string

# # def clean_text(text):
# #     translator = str.maketrans('', '', string.punctuation)
# #     words = text.translate(translator)
# #     return words
# # print(clean_text('M!ajid *hashemi.'))

# from collections import Counter
# print(Counter("mississippi"))
# word = "mississippi"
# counter = {}

# for letter in word:
#      counter[letter] = counter.get(letter, 0) + 1

# print(counter) 

from collections import Counter

def count_consecutive_words(words, group_size):
    """Count occurrences of consecutive word groups.""" 
    
    groups = [' '.join(words[i:i + group_size]) for i in range(len(words) - group_size + 1)]
    print(groups)
    return Counter(groups)

# Count consecutive words
result = {
            "consecutive_word_count": {}
        }
words = ['seyed', 'majid', 'hashemi','majid', 'majid', 'majid', 'arad', 'arad']
group_size = 2
consecutive_count = count_consecutive_words(words, group_size)
# sort_order = input("Sort order (asc/desc or leave blank): ").strip().lower()
# result["consecutive_word_count"] = dict(sorted(consecutive_count.items(), key=lambda x: x[1],reverse=(sort_order == "desc")) if sort_order else consecutive_count)
print(consecutive_count)
