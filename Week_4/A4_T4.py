print("Program starting.")
print("")
WordCount = 0
Charcount = 0

Word = input("Insert word (empty stops):")
while Word != '':
    WordCount += 1
    Charcount += len(Word)
    Word = input("Insert word (empty stops):")

print("")
print("You inserted:")
print(f"- {WordCount} words")
print(f"- {Charcount} characters")
print("")
print("Program ending.")

