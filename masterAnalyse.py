import os
import json
import string
from collections import Counter

def read_file(file_path):
    """Read and return the contents of a file."""
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"The file at '{file_path}' does not exist.")
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

def clean_text(text, ignored_words, min_len, max_len):
    """Clean text by removing punctuation and filtering words."""
    translator = str.maketrans('', '', string.punctuation)
    words = text.translate(translator).split()
    filtered_words = [
        word.lower() for word in words
        if word.lower() not in ignored_words and
        (min_len <= len(word) <= max_len if min_len and max_len else True)
    ]
    return filtered_words

def count_consecutive_words(words, group_size):
    """Count occurrences of consecutive word groups."""
    groups = [' '.join(words[i:i + group_size]) for i in range(len(words) - group_size + 1)]
    return Counter(groups)

def analyze_text(input_path, ignored_path, output_path, group_size=1, sort_order=None, min_len=None, max_len=None):
    """Main function to analyze text."""
    try:
        # Read files
        text = read_file(input_path)
        ignored_words = set(read_file(ignored_path).split()) if ignored_path else set()
       
        # Analyze text
        words = clean_text(text, ignored_words, min_len, max_len)
        lines = text.splitlines()
        sentences = text.split('.')
       
        result = {
            "number_of_lines": len(lines),
            "number_of_sentences": len(sentences),
            "number_of_words": len(words),
            "words": words,
            "consecutive_word_count": {},
            "longest_words": sorted(set(words), key=len, reverse=True)[:10],
            "ignored_words": list(ignored_words),
            "average_word_length": sum(len(word) for word in words) / len(words) if words else 0
        }
       
        # Count consecutive words
        consecutive_count = count_consecutive_words(words, group_size)
        result["consecutive_word_count"] = dict(sorted(
            consecutive_count.items(),
            key=lambda x: x[1],
            reverse=(sort_order == "desc")
        ) if sort_order else consecutive_count)
       
        # Write results to output file
        with open(output_path, 'w', encoding='utf-8') as file:
            json.dump(result, file, indent=4)
       
        print("Analysis complete. Results saved to", output_path)
   
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
                ignored_path = input("Enter ignored words file path (or leave blank): ").strip()
                output_path = input("Enter output file path: ").strip()
                group_size = int(input("Enter consecutive word group size (default 1): ") or 1)
                sort_order = input("Sort order (asc/desc or leave blank): ").strip().lower()
                min_len = input("Enter minimum word length (or leave blank): ").strip()
                max_len = input("Enter maximum word length (or leave blank): ").strip()
               
                analyze_text(
                    input_path,
                    ignored_path or None,
                    output_path,
                    group_size=group_size,
                    sort_order=sort_order if sort_order in ["asc", "desc"] else None,
                    min_len=int(min_len) if min_len else None,
                    max_len=int(max_len) if max_len else None
                )
            else:
                print("Unknown command. Try again.")
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main() 