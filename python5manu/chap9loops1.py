marks = [3, 8, 19, 6, 18, 29, 15]
ages = [12, 17, 14, 18, 11, 10, 16]
mileage = [15, 67, 89, 123, 76, 83]
cups = [7, 10, 3, 5, 8, 16, 13]

sum = 0

for i in range(0, len(marks)):
    sum = sum + marks[i]
for i in range(0, len(ages)):
    sum = sum + ages[i]
for i in range(0, len(mileage)):
    sum = sum + mileage[i]
for i in range(0, len(cups)):
    sum = sum + cups[i]

print(sum)