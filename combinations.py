
def c(n, k):
    return 1 if k == 0 else 0 if k > n else c(n-1,k)+c(n-1,k-1)

print(c(*(map(int, input().split()))))