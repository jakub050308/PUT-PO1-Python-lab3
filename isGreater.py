t = int(input())

for i in range(t):
    n, m = [int(d) for d in input().split()]
    if n>m:
        print(f"{n}  is greater than  {m}")
    elif n<m:
        print(f"{n}  is smaller than  {m}")
    else:
        print(f"n is equal m:  {n}")
