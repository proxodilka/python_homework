def chek(p, k, tree) : 
    if p == k or p in tree[k] :
        return "Yes"
    else: 
        for i in tree[k] : 
            if chek(p, i, tree) == "Yes" :
                return "Yes"
        return "No"        
     
inher = {}
for _ in range(int(input())) :
    s = input().split()
    inher[s[0]] = []
    if (len(s) > 1) :
        parents = s[2:]
        for i in parents :
            inher[s[0]].append(i)
for _ in range(int(input())) :
    parent, kid = input().split()
    print(chek(parent,kid, inher))