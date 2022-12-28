stack1=['H','C','R']
stack2=['B','J','H','L','S','F']
stack3=['R','M','D','H','J','T','Q']
stack4=['S','G','R','H','Z','B','J']
stack5=['R','P','F','Z','T','D','C','B']
stack6=['T','H','C','G']
stack7=['S','N','V','Z','B','P','W','L']
stack8=['R','J','Q','G','C']
stack9=['L','D','T','R','H','P','F','S']


# stack1=['Z', 'N']
# stack2=['M', 'C', 'D']
# stack3=['P']

def find_match(argument):
        if argument==1:
            return stack1
        elif argument==2:
            return stack2
        elif argument==3:
            return stack3
        elif argument==4:
            return stack4
        elif argument==5:
            return stack5
        elif argument==6:
            return stack6
        elif argument==7:
            return stack7
        elif argument==8:
            return stack8
        elif argument==9:
            return stack9

def no_loss(argument, match):
        if argument == 1:
            stack1=[]
            stack1 = match.copy()
        elif argument == 2:
            stack2=[]
            stack2=match.copy()
        elif argument == 3:
            stack3=[]
            stack3=match.copy()
        elif argument == 4:
            stack4=[]
            stack4=match.copy()
        elif argument == 5:
            stack5=[]
            stack5=match.copy()
        elif argument == 6:
            stack6=[]
            stack6=match.copy()
        elif argument == 7:
            stack7=[]
            stack7=match.copy()
        elif argument == 8:
            stack8=[]
            stack8=match.copy()
        elif argument == 9:
            stack9=[]
            stack9=match.copy()

with open('input_t.txt') as f:
    while True:
        line = f.readline()
        if not line:
            break
        s_line = line.split(' ')
        from_z = find_match(int(s_line[3]))
        into = find_match(int(s_line[5]))
        popping=[]
        for i in range (0, int(s_line[1])):
            # czesc1:
            # popping=from_z.pop()
            # into.append(popping)
            popping.append(from_z.pop())
        for i in range (0, len(popping)):
            into.append(popping.pop())
        no_loss(int(s_line[3]), from_z)
        no_loss(int(s_line[5]), into)

print(stack1[-1], stack2[-1], stack3[-1], stack4[-1],stack5[-1], stack6[-1], stack7[-1], stack8[-1], stack9[-1])
# print(stack1, stack2, stack3)


