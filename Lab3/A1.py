x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
def check(x, y):
    if ((x > 0) and (y > 0)):
        return 1
    elif ((x < 0) and (y > 0)):
        return 2
    elif ((x < 0) and (y < 0)):
        return 3
    elif ((x > 0) and (y < 0)):
        return 4
    else:
        print("input error")
if check(x1,y1) == check(x2, y2):
    print("Yes \n")
    print(check(x1, y1))
else:
    print("No")