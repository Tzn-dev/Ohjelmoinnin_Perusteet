# Program starting.
print("Program starting.")
# Insert a positive integer:
number = int(input("Insert a positive integer: "))

if number <= 0:
    print("Please insert a positive integer.")
else:
    count = 0
    print(number, end="")

    while number != 1:
        if number % 2 == 0: 
            number //= 2 
        else: 
            number = 3 * number + 1 
        print(f" -> {number}", end="") 
        count += 1 

# Sequence had x total steps.
    print(f"\nSequence had {count} total steps.")

print("\nProgram ending.")