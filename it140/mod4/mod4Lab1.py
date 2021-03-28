#4.14 LAB: Count input length without spaces, periods, or commas
#Given a line of text as input, output the number of characters excluding spaces, periods, or commas.

user_text = input()

count = 0
for x in user_text:
    if not(x in " .,"):
        count += 1
print(count)