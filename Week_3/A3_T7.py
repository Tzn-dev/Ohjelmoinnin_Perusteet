#Program starting.
print("Program starting.")
##Testing decision structures.
print("Testing decision structures.")
Num = int(input("Insert an integer: "))
print("Options:\n 1 - In one multi-branched decision\n 2 - In multiple independent if-statements\n 0 - Exit")
#Insert an integer: 250
Choice = int(input("Your choice: "))
if Choice ==1:
    print("Using one multi-branched decision structure.")
    if Num >= 400:
        Num = Num + 44
    elif Num >= 200:
        Num = Num + 22
    elif Num >= 100:
        Num = Num + 11
    print(f"Result is {Num}")
#Using multiple independent if-statements structure.
elif Choice ==2:
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
print("\nProgram ending.")

