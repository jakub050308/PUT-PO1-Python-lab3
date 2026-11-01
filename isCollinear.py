x1, y1 = [int (d) for d in input().split()]
x2, y2 = [int (d) for d in input().split()]
x3, y3 = [int (d) for d in input().split()]

a1 = (y2-y1)*(x3-x2)
a2 = (y3-y2)*(x2-x1)

print(a1==a2)