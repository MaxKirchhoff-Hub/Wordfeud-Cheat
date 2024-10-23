# lees alle woorden in geheugen
alle_woorden = []
def lees_woorden():
    with open('wordlist.txt', 'r') as file:
        for line in file:
            woord = line.strip() # zonder spaties eromheen
            # alleen A-Z is geschikt
            if woord.isalpha() and len(woord) > 1:
                # bewaar in hoofletter vorm
                alle_woorden.append(woord.upper())
    print("aantal woorden gelezen:", len(alle_woorden))

def zonder_letter(letters, gebruikte_letter):
    return letters.replace(gebruikte_letter, '',1)

def heeft_alle_letters(woord, letters: str):
    ongebruikte_letters = letters
    for letter in woord:
        if letter not in ongebruikte_letters:
            return False
        ongebruikte_letters = zonder_letter(ongebruikte_letters, letter)
    return True

def zoek(letters):
    juiste_woorden = []
    for woord in alle_woorden:
        if len(letters) >= len(woord):
            if heeft_alle_letters(woord, letters):
                juiste_woorden.append(woord)
    return juiste_woorden

#print(zonder_letter("AB", "B"))

#print(heeft_alle_letters("ABBA", "AB"))