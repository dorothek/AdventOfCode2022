sum=0
compartments=0

#TODO: part 2 -zliczanie przedziałów
def count_inter(part1, part2):
    count=0

    return count


def if_included(part1, part2):
    left_part1, right_part1 = map(int, part1.split('-'))
    left_part2, right_part2 = map(int, part2.split('-'))
    if (left_part2 <= left_part1 and right_part1 <= right_part2) or (left_part1 <= left_part2 and right_part2 <= right_part1):
        return True
    return False

with open('input.txt') as f:
    while True:
        line = f.readline()
        if not line:
            break
        part1, part2=line.split(',')
        if if_included(part1, part2):
            compartments=compartments+count_inter(part1,part2)
            sum=sum+1

print(sum)
print(compartments)