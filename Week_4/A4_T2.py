#Copy the previous program and modify the behaviour to match the example program run below. This program must use “for-loop” structure.

#It is recommended to replace the print-command end character with space, so that all the iterations can be printed on the same row. Last iteration might require additional logic to get rid of the extra space at the end.

#Note! the autograding tool will test that the correct structure has been applied.

#Example program runs

#Program starting.
print("Program starting.\n")

#Insert starting value: 1
start = int(input("Insert starting value: "))
#Insert stopping value: 10
stop = int(input("Insert stopping value: "))
#Starting for-loop:
print("\nStarting for-loop:")
#1 2 3 4 5 6 7 8 9 10
if start < stop:
    for i in range(start, stop + 1):
        if i != stop:
            print(i, end=" ")
        else:
            print(i, end="")
elif start > stop:
    for i in range(start, stop - 1, -1):
        if i != stop:
            print(i, end=" ")
        else:
            print(i, end="")
else:
    print(start, end="")
#Program ending.
print("\n\nProgram ending.")