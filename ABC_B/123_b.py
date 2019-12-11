from math import ceil
mnu = []
idx = []
for _ in range(5):
    tim = input()
    mnu.append(int(tim))
    idx.append(10) if tim[-1] == "0" else idx.append(int(tim[-1]))

lst = idx.index(min(idx))
res = mnu[lst]
for i in range(5):
    if lst == i:
        continue
    res += (ceil(mnu[i]/10)*10)
print(res)