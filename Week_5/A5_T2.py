# A5_T2 Pass argument

# Create Python program which is able to print user input with a decorative frame.

# Program must consist of two functions:

#    main-function
#        Print starting and ending statements.
#        Print any empty row (see example program run)
#        Prompt user to insert a word.
#        Pass the inserted word into the frameWord-function.
#        Returns None
#    frameWord
#        Takes PWord as a parameter.
#        Prints the framing and the PWord
#            Hint: Multiply the asterisk '*'-character.
#        Returns None

# Note! Tests for this task relies on properly defined functions and may fail if the program is not written according to the instructions.

# Example program runs

# Program starting.
# Insert word: Beautiful
#
# *************
# * Beautiful *
# *************
#
# Program ending.

def main():
    # Program starting.
    print("Program starting.")
    print() #
    # Insert word:
    word = input("Insert word: ")
    frameWord(word)
    print() #
    # Program ending.
    print("Program ending.")
    return None

def frameWord(PWord):
    border = "*" * (len(PWord) + 4)
    # *************
    print(border)
    #* word *
    print(f"* {PWord} *")
    # *************
    print(border)
    return None

main()

