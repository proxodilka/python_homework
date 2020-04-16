def look(d, var, name):
    if var in d[name]:
        return name
    k = 'None'
    for i in d[name]:
       if(i in d):
            k = look(d, var, i)
       if k != 'None':
            return k
    return 'None'
    
namesp = {'global':[]}
out= []
for _ in range(int(input())):
    com = input().split()
    if com[0] == 'add':
        namesp[com[1]].append(com[2])
    elif com[0] == 'create':
        namesp[com[1]] = []
        namesp[com[1]].append(com[2])
    elif com[0] == 'get':
       out.append(look(namesp, com[2], com[1]))

for i in out:
    print(i)
