a, b, c = map(int, input().split())
print('Yes') if ( a != b or b != c ) and ( a == b or b == c or c == a ) else print('No')