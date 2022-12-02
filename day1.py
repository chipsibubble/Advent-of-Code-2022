datei = open("test.txt", "r")
gelesen = datei.readlines()

alle = ""
ergebnisalle = []

for zeile in gelesen:
    alle = alle + zeile
print("Alle Zeilen: ", alle)

gesplittetInEinzelneElfen = alle.split("\n\n")

print("GesplittetInEinzelneZahlen", gesplittetInEinzelneElfen)

for elf in gesplittetInEinzelneElfen:

    EineZahlVonElf = elf.split("\n")

    print("\nErgebnis : ", EineZahlVonElf)
    
    innerList = []

    #Summe jedes Elfen und in die ergebnisalle hinzufügen.
    for x in range(len(EineZahlVonElf)): 
        print("IntZahlen: ", int(EineZahlVonElf[x]))

        innerList.append(int(EineZahlVonElf[x]))
        print("akutelleInnerList: ", sum(innerList))
    
    ergebnisalle.append(sum(innerList))
    
print("\nErgebnisalle", ergebnisalle)
print("\answer", max(ergebnisalle))
sortedErgebnisalle = sorted(ergebnisalle, reverse=True)
print("\nSortedAll", sortedErgebnisalle)
getSumThreeHighest = sortedErgebnisalle[0]+sortedErgebnisalle[1]+sortedErgebnisalle[2]
print("SumThreeHighest:", getSumThreeHighest)