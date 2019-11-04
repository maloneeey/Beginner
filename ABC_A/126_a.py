n, k = map(int, input().split())
s = input()

string = (s[:k-1]+s[k-1].lower()+s[k:])
print(string)