DELIMITER = ','

def collectWords():
    words_string = ""
    while True:
        word = input("Insert word(empty stops): ").strip()
        if word == "":
            break
        if words_string:
            words_string += DELIMITER + word
        else:
            words_string = word
    return words_string

def analyseWords(words_string):
    if not words_string:
        print("- 0 Words")
        print("- 0 Characters")
        print("- 0.00 Average word length")
        return
    
    words = words_string.split(DELIMITER)
    word_count = len(words)
    total_chars = sum(len(word) for word in words)
    avg_length = total_chars / word_count if word_count > 0 else 0
    
    print(f"- {word_count} Words")
    print(f"- {total_chars} Characters")
    print("- {:.2f} Average word length".format(avg_length))

def main():
    print("Program starting.")
    collected = collectWords()
    analyseWords(collected)
    print("Program ending.")

main()
