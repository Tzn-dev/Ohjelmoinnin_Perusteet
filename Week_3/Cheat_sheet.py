#print("Welcome to the temp app!")
#Temp = int(input("What is the temperature of CPU?"))

#if(Temp > 80):
#    print("Warning, temperature too high!")
#else:
#    print ("All cool, keep going!")

#Tee ohjelma, joka testaa, onko annettu numero parillinen vai pariton.

#Num = int(input("Anna numero: "))
#Answer = Num % 2
#if Answer == 0:
#   print(f"Numero on parillinen: {Answer}")
#else:
#    print(f"Numero on pariton:{Answer}")

#if(Temp > 80):
#    if(Temp > 90)
#        print("You are toast.")
#    else:
#        print("Warning.")
#else:
#    print("You are ok.")

#if(Temp > 90):
#    print("You are toast.")
#elif (Temp > 80):
#    print("Warning!")
#else:
#    print("You are ok.")

# Tee ohjelma, joka kysyy kahta nimeä. Testaakumpi nimistä on pidempi, vai onko ne saman mittaisia. Vinkki: len()

#name1=input("Anna nimi 1: ")
#name2=input("Anna nimi 2: ")
#if len(name1)>len(name2):
#    print("Nimi1 on pidempi kuin nimi2.")
#elif len(name1) < len(name2):
#    print("Nimi2 on pidempi kuin nimi1.")
#else:
#    print("Nimet ovat yhtä pitkiä.")


#Town = "Lahti"
#Street = "Mulkkulakatu"
#Building = 19

#if ((Town == "Lahti" or "Lahtis") and Street == "Mulkkulakatu" and Building == 19):
#    print ("You are at LAB")
#elif (Town == "Lahti" and (Street != "Mulkkulakatu" or Building != 19)):
#    print("You are in the correct town, but check the street address again")
#elif not(Town == "Lahti" and Street == "Mulkkulakatu" and Building == 19):
#    print("You are lost...")

import random

#print(random.random())
print(random.randint(1,6))

# Tehtävä, tee yksin kertainnen kivi, sakset, paperi peli random -metodia käyttäen.
import random
pelaaja=int(input("Pelataan Kivi paperi sakset. \n1 - Kivi \n2 - Paperi\n3 - Sakset\n"))
vastustaja= random.randint(1,3)
print(f"pelasit {pelaaja}, vastutajasi pelasi {vastustaja}:")
if pelaaja==vastustaja:
    print("tasapeli")
elif 
