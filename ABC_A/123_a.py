dist = [0]*5
for i in range(5):
    dist[i] = int(input())
k = int(input())

for i in range(5):
    for j in range(i):
        if abs(dist[j]-dist[i]) > k:
            print(":(")
            exit()

print("Yay!")