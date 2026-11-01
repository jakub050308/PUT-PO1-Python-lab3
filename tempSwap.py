def KtoC(temp):
    return temp-273.15

def KtoF(temp):
    return CtoF(KtoC(temp))

def FtoC(temp):
    return (temp-32)/1.8

def FtoK(temp):
    return CtoK(FtoC(temp))

def CtoF(temp):
    return (temp * 1.8) + 32

def CtoK(temp):
    return temp+273.15

#--------------------------------------------

t = int(input())

for i in range(t):
    temp, start, goal = input().split()
    temp = float(temp)
    match start:
        case "Kelvin":
            if temp<0:
                print("NO")
            elif goal == "Celsius":
                print(f"{KtoC(temp):.2f}")
            else:
                print(f"{KtoF(temp):.2f}")
        case "Celsius":
            if CtoK(temp)<0:
                print("NO")
            elif goal == "Fahrenheit":
                print(f"{CtoF(temp):.2f}")
            else:
                print(f"{CtoK(temp):.2f}")
        case "Fahrenheit":
            if FtoK(temp)<0:
                print("NO")
            elif goal == "Celsius":
                print(f"{FtoC(temp):.2f}")
            else:
                print(f"{FtoK(temp):.2f}")