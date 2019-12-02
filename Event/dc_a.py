x, y = map(int, input().split())

prize = 0
if x==1:
    prize += 300000
elif x==2:
    prize += 200000
elif x==3:
    prize += 100000

if y==1:
    prize += 300000
elif y==2:
    prize += 200000
elif y==3:
    prize += 100000

if x==1 and y==1:
    prize += 400000

print(prize)