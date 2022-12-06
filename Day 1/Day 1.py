elf_sum=[]
sum=0

with open('input.txt') as f:
    while True:
        line = f.readline()
        if not line:
            break
        print(line)
        if line=="\n":
            elf_sum.append(sum)
            sum=0
        else:
            line = int(line)
            sum = sum + line

    print("result 1", max(elf_sum))
    elf_sum.sort(reverse=True)
    print("result 2", elf_sum[0]+elf_sum[1]+elf_sum[2])




