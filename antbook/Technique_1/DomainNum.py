w, h, n = map(int, input().split())
x_1 = list( map(int, input().split()) )
x_2 = list( map(int, input().split()) )
y_1 = list( map(int, input().split()) )
y_2 = list( map(int, input().split()) )

def compress(x_1, x_2, w):
    for i in range(n):
        for d in range(-1, 2):
            tx_1, tx_2 = x_1[i]+d, x_2[i]+d