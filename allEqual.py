t = int(input())
n = set()

for i in range(t):
    n.add(int(input()))

if len(n) == 1:
    print(True)
else:
    print(False)

