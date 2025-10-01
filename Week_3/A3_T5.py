#Create a temperature unit conversion program.

#Start the program by listing options for the user:

#    Celsius to Fahrenheit
#    Fahrenheit to Celsius
#    Exit

#Prompt user to insert choice. After the decision to convert, ask the amount of current temperature (use the floating point datatype). Lastly show the converted value to the user.

#For the unit conversions, use the formula Celsius = (Fahrenheit - 32) / 1.8

#Data representation examples:

#    50.0 °F
#    10.0 °C

#If the user chooses option Exit, notify the user: Exiting...

#Use 1 decimal precision to round the converted value.

#Example program runs

#Program starting.
print("Program starting.")

#Options:
print("Options")
#1 - Celsius to Fahrenheit
print("1 - Celsius to Fahrenheit")
#2 - Fahrenheit to Celsius
print("2 - Fahrenheit to Celsius")
#0 - Exit
print("0 - Exit")
#Your choice: 1
choise = int(input("Your Choise: "))
#Insert the amount of Celsius: 23
if (choise ==1):
    Celsius = float(input("Insert the amount of Celsius: "))
    Fahrenheit = Celsius * 1.8 + 32
    print(f"{Celsius:.1f} °C equals to {Fahrenheit:.1f} °F")
#23.0 °C equals to 73.4 °F
#Insert the amount of Fahrenheit: 100
if (choise ==2):
    Fahrenheit = float(input("Insert the amount of Fahrenheit: "))
    Celsius = (Fahrenheit - 32) / 1.8
    print(f"{Fahrenheit:.1f} °F equals to {Celsius:.1f} °C")
#100.0 °F equals to 37.8 °C
elif(choise ==0):
    print("Exiting...")
#Program ending.
print("#Program ending.")


