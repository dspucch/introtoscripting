num1 = int(input())

num_dollars = num1 // 100
num1 %= 100
num_quarters = num1 // 25
num1 %= 25

print(num_dollars, 'Dollars')
print(num_quarters, 'Quarters')