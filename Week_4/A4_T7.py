#This mathematical problem is described in the following video: youtu.be/Wim9WJeDTHQ
#Video Thumbnail

#Click to play in YouTube

#lso at the wikipedia: en.wikipedia.org/wiki/Persistence_of_a_number

#reate program which prompts the user to insert an integer and then display the steps to calculate the multiplicative persistency based on the user input.

#In short, the steps in the multiplicative persistency is calculated by multiplying digits together in a given integer. This process is then repeated for the result which makes the result value smaller on each iteration till the result contains only one digit.

#The program must stop the iteration when the result contains only one digit. Finally before the program closes, it shows the steps taken.

#Example program runs

#Program starting.

#heck multiplicative persistence.
#Insert an integer: 277777788888899
#2 * 7 * 7 * 7 * 7 * 7 * 7 * 8 * 8 * 8 * 8 * 8 * 8 * 9 * 9 = 4996238671872
#4 * 9 * 9 * 6 * 2 * 3 * 8 * 6 * 7 * 1 * 8 * 7 * 2 = 438939648
#4 * 3 * 8 * 9 * 3 * 9 * 6 * 4 * 8 = 4478976
#4 * 4 * 7 * 8 * 9 * 7 * 6 = 338688
#3 * 3 * 8 * 6 * 8 * 8 = 27648
#2 * 7 * 6 * 4 * 8 = 2688
#2 * 6 * 8 * 8 = 768
#7 * 6 * 8 = 336
#3 * 3 * 6 = 54
#5 * 4 = 20
#2 * 0 = 0
#No more steps.

#This program took 11 step(s)

#Program ending.

#Pyydä arvo ja muuta se integeriksi
#Alusta muuttuja, joka laskee kierroksia
#Tee While loop, joka looppaa, niin kauan kun arvo ei ole 0
#    Testaa onko arvo pienempi kuin 10 > break
#    Muuta arvo integeriksi, jotta saaammme yksittäiset numerot esiin
#    Tee for loop joka käy läpi jokaisen stringiksi muutetun luvun
#        Testaa , onko numero viimeinen
#        Tee laskutoimitus
#    printtaa kertolaskun tulos
#    Muuta arvoksi edellisen kierroksen kertolaskun tulos
#   Jos arvo on nolla, printtaa No more steps
#    Lisää kierroslaskuriin +1
#printtaa kierrokset "This program took kierrokset step(s)"
#printtaa program ending