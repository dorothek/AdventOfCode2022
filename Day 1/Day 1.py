
biggest=0
sum=0

with open('input.txt') as f:
    while True:
        line = f.readline()
        if not line:
            break
        print(line)
        if line=="\n":
            if sum>biggest:
                biggest=sum
            sum=0
        #print("hahaha")
        else:
            line = int(line)
            sum = sum + line

    print("Answer below")
    print(biggest)


