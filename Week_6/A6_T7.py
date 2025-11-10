LOWER_ALPHABET = "abcdefghijklmnopqrstuvwxyz"
UPPER_ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

LOCATIONS = [
    "home",
    "Galba's palace",
    "Otho's palace",
    "Vitellius' palace",
    "Vespasian's palace"
]

PROGRESS_FILE = "player_progress.txt"
HEADER = "current_location;next_location;passphrase"

#ROT13 Cipher
def rot13(text: str) -> str:
    result = []
    for char in text:
        if char in LOWER_ALPHABET:
            pos = LOWER_ALPHABET.index(char)
            result.append(LOWER_ALPHABET[(pos + 13) % 26])
        elif char in UPPER_ALPHABET:
            pos = UPPER_ALPHABET.index(char)
            result.append(UPPER_ALPHABET[(pos + 13) % 26])
        else:
            result.append(char)
    return "".join(result)

#File & Progress Management
def init_progress_file() -> None:
    with open(PROGRESS_FILE, 'w', encoding='UTF-8') as f:
        f.write(HEADER + "\n")
        f.write("0;1;qvfpvcyvar\n")

def read_progress() -> list:
    try:
        with open(PROGRESS_FILE, 'r', encoding='UTF-8') as f:
            lines = f.readlines()
            return [line.strip() for line in lines[1:] if line.strip()]
    except FileNotFoundError:
        return []

def get_current_progress() -> tuple:
    progress = read_progress()
    if progress:
        parts = progress[-1].split(';')
        return int(parts[0]), int(parts[1]), parts[2]
    return 0, 1, "qvfpvcyvar"

def update_progress(current_id: int, next_id: int, ciphered_passphrase: str) -> None:
    with open(PROGRESS_FILE, 'a', encoding='UTF-8') as f:
        f.write(f"{current_id};{next_id};{ciphered_passphrase}\n")

def read_ciphered_message(next_id: int, ciphered_passphrase: str) -> tuple:
    filename = f"{next_id}_{ciphered_passphrase}.gkg"
    try:
        with open(filename, 'r', encoding='UTF-8') as f:
            lines = f.readlines()
        if not lines:
            raise ValueError("Empty message file")
        first_line = lines[0].strip()
        rest_ciphered = "".join(lines[1:])
        rest_plain = rot13(rest_ciphered)
        return first_line, rest_plain
    except FileNotFoundError:
        raise FileNotFoundError(f"Message file '{filename}' not found")

def save_plain_message(next_id: int, plain_passphrase: str, message: str) -> None:
    filename = f"{next_id}-{plain_passphrase}.txt"
    with open(filename, 'w', encoding='UTF-8') as f:
        f.write(message)

# --- Game Flow Functions ---
def print_game_start() -> None:
    current_id = get_current_progress()[0]
    print("Travel starting.")
    print(f"Currently at {LOCATIONS[current_id]}.")

def print_game_end() -> None:
    print("Travel ending.")

def travel_to_next() -> None:
    current_id, next_id, ciphered_passphrase = get_current_progress()
    
    print(f"Travelling to {LOCATIONS[next_id]}...")
    print(f"...Arriving to the {LOCATIONS[next_id]}.")
    print("Passing the guard at the entrance.")
    plain_passphrase = rot13(ciphered_passphrase)
    print(f'"{plain_passphrase}!"')
    
    print("Looking for the message in the palace...")
    print("Ah, there it is! Seems cryptic.")
    
    first_ciphered, rest_plain = read_ciphered_message(next_id, ciphered_passphrase)
    print("[Game] Progress autosaved!")
    
    # Append ciphered first line
    with open(PROGRESS_FILE, 'a', encoding='UTF-8') as f:
        f.write(first_ciphered + "\n")
    
    print("Deciphering Emperor's message...")
    save_plain_message(next_id, plain_passphrase, rest_plain)
    print("Looks like I've got now the plain version copy of the Emperor's message.")
    
    print("Time to leave...")
    
    # Update progress for next run
    if next_id < 4:
        # Hardcoded next passphrases (ROT13): discipline → tbypr, pbcvr, snrg
        next_passphrases = ["tbypr", "pbcvr", "snrg"]
        new_ciphered = next_passphrases[next_id - 1]
        update_progress(next_id, next_id + 1, new_ciphered)

# --- Main Function ---
def main() -> None:
    if not read_progress():
        init_progress_file()
    
    print_game_start()
    travel_to_next()
    print_game_end()

if __name__ == "__main__":
    main()