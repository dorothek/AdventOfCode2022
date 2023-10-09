
def wczytaj_zawartosc():
    with open("input.txt", 'r') as file:
        input=file.read().splitlines()
        return input

#tworzy slownik z katalogami
def file_schema(lines):
    path=""
    directories={}
    for line in lines:
        line=line.split()
        if line=="$ ls":
            pass
        elif line[1]=="cd":
            if line[2]=="..":
                path = path[:path.rindex("/")]
            else:
                sum=0
                path=path+'/'+line[2]
                directories[path]=sum
        elif line[0]=="dir":
            pass
        elif line[0].isdigit():
            directories[path]+=int(line[0])
    return directories


dirs=file_schema(wczytaj_zawartosc())

sum_dirs={}
for klucz in dirs:
    #kopiuje ten klucz do nowego słownika a nastepnie sumuje wartosci wszystkich kluczy w slowniku, ktorych klucze zaczynają się na ten iterał
    sum_dirs[klucz]=0
    prefiks_do_wyszukania=klucz
    for klucz2, wartosc2 in dirs.items():
        if klucz2.startswith(prefiks_do_wyszukania):
            sum_dirs[klucz] += wartosc2


solution=0
for dir in dirs.values():
    solution = solution + dir

miejsce=70000000-solution
need=30000000-miejsce
print(f'suma wszystkich katalogów:{solution}, zostalo miejscaa: {miejsce}, a więc potrzebuję jeszcze co najmniej: {need}')

#posortowac sum_dirs

min=0
for dir in sum_dirs.values():
    if dir >= need:
        if min==0 or dir<min:
            min=dir

print(f'Directory o minimalnej wielkosci jest rowny {min}')