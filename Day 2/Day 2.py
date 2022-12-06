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
            suma=suma+1
        elif ja=='Y':
            suma=suma+2
        else:
            suma=suma+3

        if (elf=='A' and ja=='X') or (elf=='B' and ja=='Y') or (elf=='C' and ja=='Z'):
            suma=suma+3
        if (elf=='A' and ja=='Y') or (elf=='B' and ja=='Z') or (elf=="C" and ja=="X"):
            suma=suma+6

print('Wynik', suma)

