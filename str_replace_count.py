s, a, b = input(), input(), input()
i = 0
while i <= 1000:
    if a in s:
        s = s.replace(a, b)
        i += 1
    else:
        print(i)
        break
if i > 1000:
    print("Impossible")
