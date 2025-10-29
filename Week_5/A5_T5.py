def display_menu():
    print("Options:")
    print("1 - Insert word")
    print("2 - Show current word")
    print("3 - Show current word in reverse")
    print("0 - Exit")

def insert_word():
    word = input("Insert word: ")
    print()
    return word

def show_word(word):
    if word == "":
        print('Current word - ""')
    else:
        print(f'Current word - "{word}"')
    print()

def show_reversed_word(word):
    if word == "":
        print('Word reversed - ""')
    else:
        print(f'Word reversed - "{word[::-1]}"')
    print()

def main():
    current_word = ""

    print("Program starting.")
    
    while True:
        display_menu()
        choice = input("Your choice: ").strip()
        print()
        
        if choice == "1":
            current_word = insert_word()
        
        elif choice == "2":
            show_word(current_word)
        
        elif choice == "3":
            show_reversed_word(current_word)
        
        elif choice == "0":
            print("Exiting program.")
            break
        
        else:
            print("Unknown option! try again.")
            print()
    
    print("Program ending.")


if __name__ == "__main__":
    main()


