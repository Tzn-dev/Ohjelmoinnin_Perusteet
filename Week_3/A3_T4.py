#Create a program with a plain menu.

##    Make program menu with following options:
#       Print welcome message
#            Welcome {Name}!
#        Exit
#            Exiting...
#    Prompt user to choose option “Your choice:”
#    Perform actions based on the user input

#Creating menus like this is a really handy way to make tiny text-based programs and there will be more exercises like this in the future.

#The expectation at this point is that the user is able to choose option by inserting corresponding number. No error handling is required, it will be introduced later.

#Other possible output variats:

#    Unknown option.

#Example program runs

#Program starting.
print("Program starting.")
#This is a program with simple menu, where you can choose which operation the program performs.
print("This is a program with simple menu, where you can choose which operation the program performs.")
#Before the menu, please insert your name: John
Name = input("Before the menu, please insert your name: ")
#Options:
print("Options:")
#1 - Print welcome message
print("1 - Print welcome message")
#2 - Print the name backwards
print("2 - Print the name backwards")
#3 - Print the first character
print("3 - Print the first character")
#4 - Show the amount of characters in the name
print("4 - Show the amount of characters in the name")
#0 - Exit
print("#0 - Exit")
#Your choice: 1
Choise = int(input("Your choice: "))

if (Choise ==1):
    print(f"Welcome {Name}!")
if (Choise ==2):
    print(Name[::-1])
if (Choise ==3):
    print(Name[0])
if Choise ==4:
    print(len(Name))
elif(Choise ==0):
    print("Exiting...")
else:
    print("Unknown option")
#Welcome John!
print(f"Welcome {Name}!")
#Program ending.
print("Program ending.")

