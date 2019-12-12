import sys
input = sys.stdin.readline

n = int(input())
tasks = []
for _ in range(n):
    a,b = map(int, input().split())
    tasks.append((a,b))

tasks = sorted( tasks, key = lambda a: a[1] )

time = 0
for task in tasks:
    time += task[0]
    if time > task[1]:
        print('No')
        break
else:
    print( 'Yes' )