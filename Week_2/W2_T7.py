#Create a Python program to convert Fahrenheit to Celcius. Round the Celsius to 1 decimal precision.

#Formula to calculate Celcius from Fahrenheit is (Fahrenheit - 32) / 1.8

#Example program run:

#Program starting.
print("Program starting.")
#Insert fahrenheits: 50
Fahrenheit = float(input("Insert fahrenheits: "))
Celsius = (Fahrenheit - 32) / 1.8   
#50.0°F is 10.0°C
print(f"{Fahrenheit}°F is {round(Celsius, 1)}°C")
#Program ending.
print("Program ending.")

