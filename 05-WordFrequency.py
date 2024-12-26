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

def second_element(t):
    return t[1]

def print_most_common(word_counter, num=5):
    items = sorted(word_counter.items(), key=second_element, reverse=True)

    for word, freq in items[:num]:
        print(freq, word, sep='\t')
def analyze_text(input_path):
    """Main function to analyze text."""
    try:
        # Read files
        text = read_file(input_path)
              
        # Analyze text
        words = clean_text(text)
        lines = text.splitlines()
        sentences = text.split('.')
        word_counter = {}
        for word in words:
            if word not in word_counter:
                word_counter[word] = 1
            else:
                word_counter[word] += 1
       
        result = {
            "number_of_lines": len(lines),
            "number_of_sentences": len(sentences),
            "number_of_words": len(words),
            "longest_words": sorted(set(words), key=len, reverse=True)[:10],
            "average_word_length": sum(len(word) for word in words) / len(words) if words else 0
        }


        # Count consecutive words
        print_most_common(word_counter, 6)
       
        # Write results to output file
        
    except Exception as e:
        print(f"Error: {e}")

def main():
    print("Welcome to Text Analyzer!")
    while True:
        try:
            command = input("Enter command (or type 'quit' to exit): ").strip().lower()
            if command == 'quit':
                break
            elif command == 'analyze':
                input_path = input("Enter input file path: ").strip()
               
                analyze_text(input_path)
            else:
                print("Unknown command. Try again.")
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main() 