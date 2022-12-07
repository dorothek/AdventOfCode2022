sum=0
letter=''
with open('input.txt') as f:
    while True:
        line = f.readline()
        if not line:
            break
        print(line)
        div=len(line)//2
        part_1=line[:div]
        part_2=line[div:]
        for l in part_1:
            for l2 in part_2:
                if l==l2:
                    letter=l
                    break
        if letter.isupper():
            sum=sum+ord(letter)-ord('A')+27
        else:
            sum=sum+ord(letter)-ord('a')+1

print(sum)