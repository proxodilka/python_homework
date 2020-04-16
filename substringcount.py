s, t = input(), input()
g = 0
ans = 0
while t in s[g:]:
    ans += 1
    g = s.find(t, g) + 1
print(ans)