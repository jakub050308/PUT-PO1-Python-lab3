t = int(input())
n = [0] * (t+1)
m = [0] * (t+1)

for i in range(t):
    n[i], m[i] = [int(d) for d in input().split()]

for i in range(t):
    n2 = n[i]
    m2 = m[i]
    if n2 > m2:
        print(f"{n2}  is greater than  {m2}")
    elif n2 < m2:
        print(f"{n2}  is smaller than  {m2}")
    else:
        print(f"n is equal m:  {n2}")


