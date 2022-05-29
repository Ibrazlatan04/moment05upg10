with open('utskrift.txt', 'w') as fw:   
# I denna funktion skrivs de in en fil som du vill läsa/skriva/lägga till osv...
# Istället för att i resten av koden skriva hela filens namn kommer den skrivas som fw 
  fw.write('''1 2 3                     
4 5 6
7 8 9                
''')                                    # Skrivs de in siffror i filen 
  fw.write('\nHär var det rutigt!')     # Skrivs de in en mening på raden under siffrorna 

with open('utskrift.txt', 'r') as fr:   # Här öppnas filen så att man kan läsa den, ger den variabeln fr
  print(fr.read())                      # Printar det som är i filen 