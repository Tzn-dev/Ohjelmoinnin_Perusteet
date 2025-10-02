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

#import random

#print(random.random())
#print(random.randint(1,6))

# Tehtävä, tee yksin kertainnen kivi, sakset, paperi peli random -metodia käyttäen.
#import random
#pelaaja=int(input("Pelataan Kivi paperi sakset. \Anna valintasi:\n1 - Kivi\n2 - Paperi\n3 - Sakset\n"))
#vastustaja=random.randint(1,3)
#print(f"pelasit {pelaaja}, vastutajasi pelasi {vastustaja}:")
#if pelaaja==vastustaja:
#    print("tasapeli")
#elif (pelaaja==1 and vastustaja==3) or (pelaaja==2 and vastustaja==1) or (pelaaja==3 and vastutaja==2):
#    print("Sinä voitit")
#else:
#   print("Vastutaja voitti")



Children = 3
Hometown = "Lahti"
#Lista
TownsInFinland = ["Lahti", "Helsinki", "Lappeenranta", "Oulu", "Tampere"]

RandomInformation = ["Mira", 48, True, Children, Hometown]

print(TownsInFinland[0])
TownsInFinland.append("Rovaniemi")
print(TownsInFinland)

NumOfTowns = len(TownsInFinland) #vast:6
print(TownsInFinland[NumOfTowns-1])

Municipalities = ["Asikkala", "Hollola", "Karvia", "Kempele"]
Towns = ["Lahti", "Helsinki", "Lappeenranta", "Oulu", "Tampere"]

MunicipalitiesAndTowns = [Municipalities, Towns]
print(MunicipalitiesAndTowns[1][-2])

Towns.sort()
print(Towns)

Teacher = {
    'name': 'Juha',
    'age': 50,
    'city': 'Lahti'
}

print(Teacher["name"])

Teacher['email'] = 'juha.hyytiainen@lab.fi'

print(Teacher)

for key in Teacher:
    print(key, end=' ')
    print(Teacher[key])

Student = [
    {'name':'Mikko', 'age': 25, 'city': 'Tampere'}
    {'name':'Maija', 'age': 30, 'city': 'Espoo'}
    {'name':'Seppo', 'age': 35, 'city': 'Helsinki'}
]

print(Student[0])

Cities = {
    'Finland':['Tampere', 'Espoo', 'Helsinki'],
    'Sweden':['Stockholm', 'Malmö']
}
print(Cities['Finland'][0])

#Towns = ["Lahti", "Helsinki", "Lappeenranta", "Oulu", "Tampere"]
for town in Towns:
    print(f"Town of {town}")
    print(f"All of the towns {Towns}")

for i in range(1,10):
    print(i)

for i in range(1,10):
    print(i, end=' ')

print("")
for i in range(1, 10, 3):
    print(i)

Total = 0
for i in range(1,101):
    Total +=i
    print(Total)

print(Total)

for i in range(9):
    if (i == 3):
        continue
    print(i)

#Opiskele loopit for ja while, sekä niihin liittyvät komennot: continue ja break

#while 1 < 10:
#    print("Do not try me at home xD")
i = 0
while i < 10:
    print(f"Iteration number: {i}")
    i+= 1
    #i= i + 1

continueLoop = True
while continueLoop == True:
    if input("Do you want to continue? ") != "yes":
        continueLoop = False

while True:
    if input("Do you want to continue? ") != "yes":
        break
    else:
        continue
    