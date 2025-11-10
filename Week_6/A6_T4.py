def print_start_message() -> None:
    print("Program starting.")
    print("This program analyses a list of names from a file.")

def get_filename() -> str:
    return input("Insert filename to read: ").strip()

def read_names_from_file(filename: str) -> list:
    print(f'Reading names from "{filename}".')
    names = []
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            for line in file:
                name = line.strip()
                if name:  
                    names.append(name)
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        raise
    except Exception as e:
        print(f"Error reading file: {e}")
        raise
    return names

def analyze_names(names: list) -> dict:
    print("Analysing names...")
    if not names:
        return {
            'count': 0,
            'shortest': 0,
            'longest': 0,
            'average': 0.00
        }
    
    lengths = [len(name) for name in names]
    count = len(names)
    shortest = min(lengths)
    longest = max(lengths)
    average = sum(lengths) / count
    
    return {
        'count': count,
        'shortest': shortest,
        'longest': longest,
        'average': average
    }

def generate_report(stats: dict) -> str:
    report_lines = [
        "#### REPORT BEGIN ####",
        f"Name count - {stats['count']}",
        f"Shortest name - {stats['shortest']} chars",
        f"Longest name - {stats['longest']} chars",
        f"Average name - {stats['average']:.2f} chars",
        "#### REPORT END ####"
    ]
    return "\n".join(report_lines)

def print_analysis_complete() -> None:
    print("Analysis complete!")

def main() -> None:
    print_start_message()
    filename = get_filename()
    names = read_names_from_file(filename)
    stats = analyze_names(names)
    print_analysis_complete()
    report = generate_report(stats)
    print(report)
    print("Program ending.")

if __name__ == "__main__":
    main()