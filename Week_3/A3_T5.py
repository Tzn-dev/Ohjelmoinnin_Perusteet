print("Program starting.\n")
print("Options:")
print("1 - Celsius to Fahrenheit")
print("2 - Fahrenheit to Celsius")
print("0 - Exit")
choice = int(input("Your Choice: "))
if choice ==1:
    Celsius = float(input("Insert the amount of Celsius: "))
    Fahrenheit = (Celsius * 1.8) + 32
    print(f"{Celsius:.1f} °C equals to {Fahrenheit:.1f} °F\n")
elif choice ==2:
    Fahrenheit = float(input("Insert the amount of Fahrenheit: "))
    Celsius = (Fahrenheit - 32) / 1.8
    print(f"{Fahrenheit:.1f} °F equals to {Celsius:.1f} °C\n")
elif choice ==0:
    print("Exiting...\n")
else:
    print("Unknown option.\n")
print("Program ending.")