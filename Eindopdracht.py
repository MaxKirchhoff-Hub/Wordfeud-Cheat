#Max Kirchhoff
#Wordfeud cheat programma

from inlezen import *
from letterwaarde import *

lees_woorden()


letters = input("Wat zijn jou letters? = ")

antwoorden = zoek(letters.upper())

#beste = hoogste_waarde(antwoorden)
#print(beste)

#beste_waarde = bereken(beste)
#print(beste_waarde)

top3 = top_drie(antwoorden)
print(top3)