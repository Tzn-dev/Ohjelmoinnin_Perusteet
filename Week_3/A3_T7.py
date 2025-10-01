#In this task the idea is to create a program where user can define an integer and choose the decision structure being applied to the inserted integer. Certain rules must be applied to specified value tresholds and the decision structure has partial role in the end results. Structure, order and operators matter, so do exactly as the task describes.

#    Prompt user to insert value as an integer.
#    Display menu
#        option 1 - In one multi-branched decision
#        option 2 - Independent if-statement decisions
#        option 0 - Exit
#    Prompt user to choose option
#    Apply following math operations in the options 1 & 2
#        One multi-branched decision structure:
#            Value is 400 or more => add 44 to the existing value
#            Value is 200 or more => add 22 to the existing value
#            Value is 100 or more => add 11 to the existing value
#        Independent if-statement decisions one after another:
#            Value is 400 or more => add 44 to the existing value
#            Value is 200 or more => add 22 to the existing value
#            Value is 100 or more => add 11 to the existing value
#        Exit: “Exiting…”
#    At the end of the options 1 & 2, show the results like in the example program runs.


#Other possible output variats:

 #   “Unknown option.”

#Program starting.
print("Program starting.")
##Testing decision structures.
print("Options:\n 1 - In one multi-branched decision\n 2 - In multiple independent if-statements\n 0 - Exit")

#Insert an integer: 250
Num = int(input("Insert an integer: "))
#Options:
#1 - In one multi-branched decision
#0 - Exit
Choise = int(input("Your choice: "))

if Choise ==1:
    print("Using one multi-branched decision structure.")
    if Num >= 400:
        Num = Num + 44
    elif Num >= 200:
        Num = Num + 22
    elif Num >= 100:
        Num = Num + 11
    print(f"Result is {Num}")
#Using multiple independent if-statements structure.
elif Choise ==2:
    print("Using multiple independent if-statements structure.")
    if Num >= 400:
        Num = Num + 44
    if Num >= 200:
        Num = Num + 22
    if Num >= 100:
        Num = Num + 11
    print(f"Result is {Num}")
#Exiting... 0
elif Choice ==0:
    print("Exiting...")

#Unknown option.
else:
    print("Unknown option.")
#Program ending.
print("Progream ending.")

