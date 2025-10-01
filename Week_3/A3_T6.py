print("Program starting.")
print("Welcome to the unit converter program!")
print("Follow the menu instructions below.")

print("\nOptions:")
print("1 - Length")
print("2 - Weight")
print("0 - Exit")
Choice = int(input("Your choice: "))
if (Choice ==1):
    print("\nLength options:")
    print("1 - Meters to kilometers")
    print("2 - Kilometers to meters")
    print("0 - Exit")
    Choice2 = int(input("Your choice: "))
    if (Choice2 == 1):
        Meters = float(input("Insert meters: "))
        Answer1 = Meters / 1000
        print(f"{round(Meters, 1)} m is {round(Answer1, 1)} km")
    elif (Choice2 == 2):
        Kilometers = float(input("Insert kilometers: "))
        Answer2 = Kilometers * 1000
        print(f"{round(Kilometers, 1)} km is {round(Answer2, 1)} m")
    elif (Choice2 == 0):
        print("Exiting...")
    else:
        print("Unknown option.")
elif (Choice == 2):
    print("\nWeight options:")
    print("1 - Grams to pounds")
    print("2 - Pounds to grams")
    print("0 - Exit")
    Choice3 = int(input("Your choice: "))
    if (Choice3 == 1):
        Grams = float(input("Insert grams: "))
        Answer3 = Grams / 453.59237
        print(f"{round(Grams, 1)} g is {round(Answer3, 1)} lb")
    elif (Choice3 == 2):
        Pounds = float(input("Insert pounds: "))
        Answer4 = Pounds * 453.59237
        print(f"{round(Pounds, 1)} lb is {round(Answer4, 1)} g")
    elif (Choice3 == 0):
        print(f"Exiting...")
    else:
        print("Unknown option.")
elif (Choice ==0):
    print("\nExiting...")
else:
    print("Unknown option.")
print("\nProgram ending.")