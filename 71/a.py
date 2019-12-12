x, a, b = map(int, input().split())
string = "A" if abs(x-a) < abs(x-b) else "B"
print(string)