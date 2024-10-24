# lees alle woorden in geheugen
alle_woorden = []
#uitzoeken van worden die gebruikt kunnen worden
def lees_woorden():
    with open('wordlist.txt', 'r') as file:
        for line in file:
            woord = line.strip() #zonder spaties eromheen
            #alleen A-Z is geschikt
            if woord.isalpha() and len(woord) > 1:
                #bewaar in hoofletter vorm
                alle_woorden.append(woord.upper())
    print("aantal woorden gelezen:", len(alle_woorden))

#de gebruikte letters verweideren uit de loop
def zonder_letter(letters, gebruikte_letter):
    return letters.replace(gebruikte_letter, '',1)

#het woodt samen stellen op basis van de letters die ingevoerd zijn
def heeft_alle_letters(woord, letters: str):
    ongebruikte_letters = letters
    for letter in woord:
        if letter not in ongebruikte_letters:
            return False
        ongebruikte_letters = zonder_letter(ongebruikte_letters, letter)#voorkomen dat letter dubbel gebruikt worden
    return True

#het woord opzoek in de wordlist
def zoek(letters):
    juiste_woorden = []
    for woord in alle_woorden:
        if len(letters) >= len(woord):#het woord kan niet langer zijn dan het aantal letters
            if heeft_alle_letters(woord, letters):
                juiste_woorden.append(woord)
    return juiste_woorden

#print(zonder_letter("AB", "B"))

#print(heeft_alle_letters("ABBA", "AB"))
