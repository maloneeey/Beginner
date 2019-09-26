L, R = map(int, input().split())
L = L % 2019
R = R % 2019
array = [i for i in range(L, R+1)]

tmp = 2019*2019
for i in range(len(array)):
    for j in range(i+1, len(array)):
        if array[i] * array[j] % 2019 == 0:
            break
        if array[i] * array[j] % 2019 < tmp:
            tmp = array[i] * array[j] % 2019

print(tmp)