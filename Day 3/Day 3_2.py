sum=0
with open('input.txt') as f:
    while True:
        line1 = f.readline()
        if not line1:
            break
        line2 = f.readline()
        line3 = f.readline()
        for l in line1:
            if (l in line2) and (l in line3):
                print(l)
                if l.isupper():
                    sum = sum + ord(l) - ord('A') + 27
                else:
                    sum = sum + ord(l) - ord('a') + 1
                break

print(sum)