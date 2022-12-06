suma=0

with open('input.txt') as f:
    while True:
        line = f.readline()
        if not line:
            break
        print(line)
        elf=line[0]
        ja=line[2]
        if ja=='X':
            suma=suma+0
        elif ja=='Y':
            suma=suma+3
        else:
            suma=suma+6
        #przegrać
        if elf=='A' and ja=='X':
            suma=suma+3 #nożyce
        if elf=='B' and ja=='X':
            suma=suma+1 #kamien
        if elf=='C' and ja=='X':
            suma=suma+2 #papier
        #remis
        if elf=='A' and ja=='Y':
            suma=suma+1 #kamien
        if elf=='B' and ja=='Y':
            suma=suma+2 #papier
        if elf=='C' and ja=='Y':
            suma=suma+3 #nozyce
        #wygrac
        if elf=='A' and ja=='Z':
            suma=suma+2 #papier
        if elf=='B' and ja=='Z':
            suma=suma+3 #nożyce
        if elf=='C' and ja=='Z':
            suma=suma+1 #kamien

print('Wynik', suma)