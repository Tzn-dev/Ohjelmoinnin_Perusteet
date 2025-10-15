# Create a Python program which collects words in a collectWords-function and analyses the words in a analyseWords-function. Use main-function to define the main logic.
# 
# Separate words with comma ',' delimiter. Define DELIMITER at the beginning of the program on the top-level as a constant variable.
# 
# Main logic
# 
# Call the collectWords-function and store the words into a local variable. Next pass the collected words to the analyseWords-function.
# 
# Word collecting:
# 
# Prompt user to insert word. Repeat the prompt till the user enters an empty word. Collect all words into one variable where each word is separated by a DELIMITER. At the end of the function, return the string variable holding all of the words.
# 
# Analysing words:
# 
# Takes one parameter containing words wrapped into one string. Calculates the amount of words, characters and the average word length. Separating words must happen by utilizing the DELIMITER. Finally displays the results. Average word length must be presented in 2 decimal precision. This function should not return anything.
# 
# Use print("- {:.2f} Average word length".format(Avg)) to print average word length in 2 decimal precision.
# 
# Example program runs
# 
# Program starting.
# Insert word(empty stops): challenges
# Insert word(empty stops): help
# Insert word(empty stops): us
# Insert word(empty stops): grow
# Insert word(empty stops): stronger
# Insert word(empty stops): 
# - 5 Words
# - 28 Characters
# - 5.60 Average word length
# Program ending.
# 
# 
# 