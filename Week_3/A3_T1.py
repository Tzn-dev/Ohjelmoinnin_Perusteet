#Other possible output variants:

#   Integer comparison
#        Integers are the same.
#        First integer is greater.
#    Parity check
#        Sum is even.

#Example program run

#Program starting.
print("Program starting.")
#Insert two integers.
print("Insert two integers.")
#Insert first integer: 5
Int1 = int(input("Insert first integer: "))
#Insert second integer: 5
Int2 = input("Insert second integer: ")
#Comparing inserted integers.
print(f"Comparing inserted integers.")
#Integers are the same
if Int1==Int2:
    print(f"Integers {Int1} and {Int2} are the same.")
if Int1>Int2:
    print(f"Interger {Int1} is greater than {Int2}.")
if Int1<Int2:
    print(f"Interger {Int2} is greater than {Int1}.")
#Adding integers together
print(f"Sim is {Int1} + {Int2} = {Int1+Int2}\n")
#5 + 5 = 10

#Checking the parity of the sum...
print("Checking the parity of the sum...")
#Sum is even.
if (Int1+Int2)%2==0:
    print("Sum is even")
else:
    print("Sum is un even.")
#Program ending.
print("Program ending.")


