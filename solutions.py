n, x, y = [int(z) for z in input().split()]

count = 0
n += 1

for a in range(n):
    for b in range(n):
        for c in range(n):
            for d in range(n):
                if (x*a**2 + y*b**2) == (x*c**2 + y*d**2):
                    count += 1
print(count)