def showOptions():
    print("Options:")
    print("1 - Show count")
    print("2 - Increase count")
    print("3 - Reset count")
    print("0 - Exit")


def askChoice():
    user_input = input("Your choice: ").strip()
    if user_input.isnumeric():
        return int(user_input)
    else:
        return -1


def main():
    count = 0
    print("Program starting.")

    while True:
        showOptions()
        choice = askChoice()

        
        if choice == -1 or choice not in [0, 1, 2, 3]:
            print("Unknown option!")
            print()
            continue

        
        if choice == 1:
            print(f"Current count - {count}")
        elif choice == 2:
            count += 1
            print("Count increased!")
        elif choice == 3:
            count = 0
            print("Cleared count!")
        elif choice == 0:
            print("Exiting program.")
            break

        print()

    print("Program ending.")


main()