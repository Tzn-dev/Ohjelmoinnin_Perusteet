# Program starting.
print("Program starting.")
# Check multiplicative persistence.
print("\nCheck multiplicative persistence.")
# Insert an integer: 
while True:
    user_input = input("Insert an integer: ")
    try:
        number = int(user_input)
        if number >= 0:
            break
        print("Invalid input. Please enter a valid non-negative integer.")
    except:
        print("Invalid input. Please enter a valid non-negative integer.")

step_count = 0
while number > 9:
    digits = str(number)
    product = 1
    step_display = ""
    index = 0
    while index < len(digits):
        product *= int(digits[index])
        step_display += digits[index] + (" * " if index < len(digits) - 1 else f" = {product}")
        index += 1
    print(step_display)
    number = product
    step_count += 1

# No more steps.
print("No more steps.")
# This program took x step(s)
print(f"\nThis program took {step_count} step(s)")
# Program ending.
print("\nProgram ending.")