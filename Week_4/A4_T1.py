#Create a Python program which prompts user to insert two integers. Use these integers together with the “for-loop” structure to create behaviour like in the example program example run below.

#Note! the autograding tool will test that the correct structure has been applied.

#Example program runs

#Program starting.
print("Program starting.\n")
#Insert starting value: 11
start = int(input("Insert starting value: "))
#Insert stopping value: 13
stop = int(input("Insert stopping value: "))

#Starting for-loop:
print("\nStarting for-loop:")
if start < stop:
    for i in range(start, stop + 1):
        print(i)
elif start > stop:
    for i in range(start, stop - 1, -1):
        print(i)
else:
    print(start)
#Program ending.
print("\nProgram ending.")

