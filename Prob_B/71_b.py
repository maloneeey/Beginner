from collections import deque
char = deque(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'])

string = list(input())

for i in range(len(string)):
    if string[i] in char:
        char.remove(string[i])

output = char.popleft() if char else "None"
print(output)