def print_start_message() -> None:
    print("Program starting.")
    print("This program can read a file.")

def get_filename() -> str:
    return input("Insert filename: ").strip()

def print_decorative_start(filename: str) -> None:
    print(f'#### START "{filename}" ####')

def print_decorative_end(filename: str) -> None:
    print(f'#### END "{filename}" ####')

def read_and_print_file(filename: str) -> None:
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            content = file.read()
            print(content, end='')
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    except Exception as e:
        print(f"Error reading file: {e}")

def main() -> None:
    print_start_message()
    filename = get_filename()
    print_decorative_start(filename)
    read_and_print_file(filename)
    print_decorative_end(filename)
    print("Program ending.")

if __name__ == "__main__":
    main()