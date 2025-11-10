# English alphabets (2 x 26)
LOWER_ALPHABETS = "abcdefghijklmnopqrstuvwxyz"
UPPER_ALPHABETS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def askRows() -> str:
    print("\nCollecting plain text rows for ciphering.")
    lines = []
    while True:
        row = input("Insert row(empty stops): ").rstrip()
        if row == "":
            break
        lines.append(row)
    return "\n".join(lines)

def shiftCharacter(Character: str, Alphabets: str, Shift: int = 13) -> str:
    if Character not in Alphabets:
        return Character
    pos = Alphabets.index(Character)
    new_pos = (pos + Shift) % 26
    return Alphabets[new_pos]

def rot13(Content: str) -> str:
    result = []
    for char in Content:
        if char in LOWER_ALPHABETS:
            result.append(shiftCharacter(char, LOWER_ALPHABETS))
        elif char in UPPER_ALPHABETS:
            result.append(shiftCharacter(char, UPPER_ALPHABETS))
        else:
            result.append(char)
    return "".join(result)

def writeFile(Filename: str, Content: str) -> None:
    try:
        with open(Filename, 'w', encoding='UTF-8') as f:
            f.write(Content)
        print("Ciphered text saved!")
    except Exception as e:
        print(f"Error saving file: {e}")

def main() -> None:
    print("Program starting.")
    
    plain_text = askRows()
    
    ciphered = rot13(plain_text)
    
    print("\n#### Ciphered text ####")
    print(ciphered)
    print("#### Ciphered text ####")
    
    filename = input("Insert filename to save: ").strip()
    
    if filename:
        writeFile(filename, ciphered + "\n")  
    else:
        print("File name not defined.")
        print("Aborting save operation.")
    
    print("Program ending.")

if __name__ == "__main__":
    main()