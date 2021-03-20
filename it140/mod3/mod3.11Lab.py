a = int(input())
b = int(input())
c = int(input())

smallest = 0

if a < b and a < c:
        smallest = a
if b < c and b < a:
    smallest = b
if c < b and c < a:
    smallest = c
if (a == b) and (b == c) and (a == c):
    smallest = a
print(smallest)