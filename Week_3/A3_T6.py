#Create menu program with submenus. Mainly for unit conversions. Use the values from the following table for unit conversions https://www.isa.org/getmedia/192f7bda-c77c-480a-8925-1a39787ed098/CCST-Conversions-document.pdf

#Menu options:

#    Length
#        Meters to kilometers
#        Kilometers to meters
#    Weight
#        Grams to pounds
#        Pounds to grams
#    Exit
#        “Exiting...”

#Handle all the data in floating point datatype. Remember to round every value in 1 digit precision right before displaying.

#Other possible prints:

#    “Unknown option.”

#Example run - weight conversion 1

#Program starting.
print("#Program starting.")
#Welcome to the unit converter program!
print("#Welcome to the unit converter program!")
#Follow the menu instructions below.
print("#Follow the menu instructions below.")
#Options:
print("#Options:")
#1 - Length
print("1 - Length")
#2 - Weight
print("2 - Weight")
#0 - Exit
print("0 - Exit")
#Your choice: 0
choise1 = int(input("Your choice: "))
#Exiting...
if (choise1 ==0):
    print("Exiting...")

#Length options:
if (choise1 ==1):
    print("Length options:")
#1 - Meters to kilometers
    print("1 - Meters to kilometers")
#2 - Kilometers to meters
    print("2 - Kilometers to meters")
#0 - Exit
    print("0 - Exit")
#Your choice: 2
    choise = int(input("Your choice: "))
#Insert kilometers: 20
input = float(input("Insert kilometers: "))
#20.0 km is 20000.0 m
if (choise ==1):
        print(f"{input:.1f} m is {input/1000:.1f} km")  
if (choise ==2):
        print(f"{input:.1f} km is {input*1000:.1f} m")
#Exiting...
if(choise ==0):
    print("Exiting...")
else:
    print("Unknown option.")
#Weight options:
if (choise1 ==2):
    print("Weight options:")
#1 - Grams to pounds
    print("1 - Grams to pounds")
#2 - Pounds to grams
    print("2 - Pounds to grams")
#0 - Exit
    print("0 - Exit")
#Your choice: 1
choise2 = int(input("Your choise: "))
#Insert grams: 100
if (choise2 ==1):
     grams = float(input("Insert grams: "))
#100.0 g is 0.2205 lb
     print(f"{grams:.1f} g is {grams*0.002205:.4f} lb")
#Insert pounds: 1
if (choise2 ==2):
     pounds = float(input("Insert pounds: "))
#1.0 lb is 453.6 g
     print(f"{pounds:.1f} lb is {pounds*453.6:.1f} g")
#Exiting...
if (choise2 ==0):
    print("Exiting...")
#Unknown option.
else:
    print("Unknown option.")
#Program ending.
print("#Program ending.")


