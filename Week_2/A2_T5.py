#Make a Python program, which prompts for a compound word.
#    Get following aspects from the word
#        Length
#        First character
#        Reversed version e.g. “Suitcase” is reversed “esactiuS”
#    Display the aspects using print commands.
#    Prompt the user to take substring from the existing compound word.
#    Finally print the user specified substring.

#Example program run:

#Program starting.
print("Program starting.")
#Insert a closed compound word: Moonbanana
compound_word = input("Insert a closed compound word: ")
#The word you inserted is 'Moonbanana' and in reverse it is 'ananabnooM'.
print(f"The word you inserted is '{compound_word}' and in reverse it is '{compound_word[::-1]}'.")
#The first character is 'M' and the last character is 'a'.  
print(f"The first character is '{compound_word[0]}' and the last character is '{compound_word[-1]}'.")                                                                
#The inserted word length is 10
print(f"The inserted word length is {len(compound_word)}")
#Last character is 'a'
print(f"Last character is '{compound_word[-1]}'") 
#Take substring from the inserted word by inserting...
#1) Starting point: 0
Start = int(input("Take substring from the inserted word by inserting...\n1) Starting point: "))
#2) Ending point: 4
End = int(input("2) Ending point: "))
#3) Step size: 1
Step = int(input("3) Step size: "))
#The word 'Moonbanana' sliced to the defined substring is 'Moon'.
print(f"The word '{compound_word}' sliced to the defined substring is '{compound_word[Start:End:Step]}'.")
#Program ending.
print("Program ending.")