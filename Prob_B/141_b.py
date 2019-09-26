s = list(input())

flag = 0
for i in range(len(s)):
    if i%2 == 1:
        if s[i] == "R":
            flag = 1
    else:
        if s[i] == "L":
            flag = 1

string="No" if flag else "Yes"
print(string)