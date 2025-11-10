def print_start_message() -> None:
    print("Program starting.")
    print("This program can copy a file.")

def get_source_filename() -> str:
    return input("Insert source filename: ").strip()

def get_destination_filename() -> str:
    return input("Insert destination filename: ").strip()

def read_file_content(filename: str) -> str:
    print(f"Reading file '{filename}' content.")
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            content = file.read()
        print("File content ready in memory.")
        return content
    except FileNotFoundError:
        print(f"Error: Source file '{filename}' not found.")
        raise
    except Exception as e:
        print(f"Error reading file: {e}")
        raise

def write_file_content(filename: str, content: str) -> None:
    print(f"Writing content into file '{filename}'.")
    try:
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(content)
        print("Copying operation complete.")
    except Exception as e:
        print(f"Error writing file: {e}")
        raise

def main() -> None:
    print_start_message()
    source = get_source_filename()
    destination = get_destination_filename()
    content = read_file_content(source)
    write_file_content(destination, content)
    print("Program ending.")

if __name__ == "__main__":
    main()