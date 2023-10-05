def wczytaj_zawartosc():
    with open("input.txt", 'r') as file:
        input=file.read().splitlines()
        return input

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
print(dirs)

sum_dirs={}
for klucz in dirs:
    #kopiuje ten klucz do nowego słownika a nastepnie sumuje wartosci wszystkich kluczy w slowniku, ktorych klucze zaczynają się na ten iterał
    sum_dirs[klucz]=0
    prefiks_do_wyszukania=klucz
    for klucz2, wartosc2 in dirs.items():
        if klucz2.startswith(prefiks_do_wyszukania):
            sum_dirs[klucz] += wartosc2

solution=0
for dir in sum_dirs.values():
    if dir <= 100000:
        print(dir)
        solution = solution + dir

print(f'suma:  {solution}')




