with open('input.txt', 'r') as plik:
    zawartosc = plik.read()

# Teraz zawartosc zawiera całą treść pliku
print(zawartosc)

licznik=13
n=0

while 1:
    lista = list(zawartosc[n:n+14])

    if len(lista) == len(set(lista)):
        print("Wszystkie elementy w liście są unikalne.")
        licznik=licznik+1
        break;
    else:
        print("Lista zawiera duplikaty.")
        n=n+1
        licznik=licznik+1

print(licznik)