#Write a Python program which asks user to insert hex color.
#In this case hex color is expected to be the 7 character representation starting with # # and followed by 6 0-F characters to represent RGB colors.
#More about hex colors at https://en.wikipedia.org/wiki/Web_colors
#Slice the amount of red, green and blue from that inserted color and display each color as shown below.
#Example program run:

#Program starting.
print("Program starting.")
#Insert a hex color: #FFA500
HexColor = input("Insert a hex color: ")
#Colors
#- Red FF
Red = HexColor[1:3]
#- Green A5
Green = HexColor[3:5]
#- Blue 00
Blue = HexColor[5:7]
print(f"Colors\n- Red {Red}\n- Green {Green}\n- Blue {Blue}")
#Program ending.
print ("Program ending.")

