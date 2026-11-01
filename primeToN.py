def prime(x:int):
    if x == 1:
        return False
    if x<3:
        return True
    for s in range(2, int(x**0.5)+1):
        if x%s == 0:
            return False
    return True

n = int(input())
tab = []

for i in range(1, n+1):
    if prime(i):
        print(i)

