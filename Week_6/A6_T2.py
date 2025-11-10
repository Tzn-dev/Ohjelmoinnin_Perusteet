def get_first_name() -> str:
    return input("Insert first name: ").strip()

def get_last_name() -> str:
    return input("Insert last name: ").strip()

def get_filename() -> str:
    return input("Insert filename: ").strip()

def write_name_file(filename: str, first_name: str, last_name: str) -> None:
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            print(first_name, file=f)
            print(last_name,  file=f)
            print("",        file=f)
    except Exception as e:
        print(f"Error writing file: {e}")

def main() -> None:
    print("Program starting.")
    first_name = get_first_name()
    last_name  = get_last_name()
    filename   = get_filename()
    write_name_file(filename, first_name, last_name)
    print("Program ending.")

if __name__ == "__main__":
    main()