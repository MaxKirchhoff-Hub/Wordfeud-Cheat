# Max Kirchhoff

letterwaarden = {"A": 1, "B": 4, "C": 5, "D": 2, "E": 1, "F": 4, "G": 4, "H": 4, "I": 2, "J": 4, "K": 3, "L": 3, "M": 3,
                "N": 1, "O": 1, "P": 4, "Q": 10, "R": 2, "S": 2, "T": 2, "U": 2, "V": 4, "W": 5, "X": 8, "Y": 8, "Z": 5}

#de waarden van het word berekenen
def bereken(woord: str):
    waarde = 0
    for letter in woord:
        w = letterwaarden.get(letter,0)
        waarde += w
        #de waarde optellen van de letters in het wordt
    return waarde


#het wrood met de hoogste warden ophalen
def hoogste_waarde(woorden):
    hoogste = 0
    hoogste_woord = ""
    for woord in woorden:
        waarde = bereken(woord)
        if waarde > hoogste:
            hoogste_woord = woord
            hoogste = waarde
    return hoogste_woord

#een top drie aanmaken van de worden met de hoogste warden
def top_drie(woorden):
    woordenlijst = []
    for woord in woorden:
        waarde = bereken(woord)
        woord_met_waarde = (woord, waarde)
        woordenlijst.append(woord_met_waarde)
    woordenlijst.sort(key=lambda x: x[1], reverse=True)
    #functie om de drie beste worden te krijgen door het verglijken van de punten
    return woordenlijst[:3]
