# Create a Python program with two functions:

#    main-function
#        Does the routines ("Program starting." and "Program ending.")
#        Utilizes askName-function.
#        Utilizes greetUser-function.
#        Returns None
#    askName-function
#        Prompts the user to insert name
#        Returns name
#    greetUser-function
#        Which takes PName as an argument
#        Greets the user "Hello {PName}!"
#        Returns None

# Note! Tests for this task relies on properly defined functions and may fail if the program is not written according to the instructions.

# Program starting.
# Insert name: John
# Hello John!
# Program ending.

def main():
    # Program starting.
    print("Program starting.")
    # Insert name: 
    name = askname()
    # Hello Name!
    greetUser(name)
    # Program ending.
    print("Program ending.")
    return None

def askname():
    # Insert name: 
    name = input("Insert name: ")
    return name

def greetUser(PName):
    # Hello Name!
    print(f"Hello {PName}!")
    return None

main()
