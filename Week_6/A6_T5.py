SEPARATOR = ";"


def readValues(filename: str) -> str:
    values = ""
    try:
        with open(filename, "r", encoding="utf-8") as f:
            for line in f:
                stripped = line.strip()
                if stripped:                     
                    try:
                        num = int(stripped)
                        if values:
                            values += SEPARATOR
                        values += str(num)
                    except ValueError:
                        continue          
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        raise
    except Exception as e:
        print(f"Error reading file: {e}")
        raise
    return values

def analyseValues(values_str: str) -> str:
    
    if not values_str:
        return "Count;Sum;Greatest;Average\n0;0;0;0.00\n"

    nums = [int(x) for x in values_str.split(SEPARATOR)]

    count = len(nums)
    total = sum(nums)
    greatest = max(nums)
    average = total / count

    header = "Count;Sum;Greatest;Average"
    data   = f"{count};{total};{greatest};{average:.2f}"
    return f"{header}\n{data}\n"

def print_start():
    print("Program starting.")

def get_filename() -> str:
    return input("Insert filename: ").strip()

def print_report(filename: str, csv_text: str) -> None:
    lines = [
        "#### Number analysis - START ####",
        f'File "{filename}" results:',
        csv_text.strip(),
        "",
        "#### Number analysis - END ####"
    ]
    print("\n".join(lines))


def main() -> None:
    print_start()
    filename = get_filename()
    data = readValues(filename)          
    csv  = analyseValues(data)           
    print_report(filename, csv)
    print("Program ending.")


if __name__ == "__main__":
    main()