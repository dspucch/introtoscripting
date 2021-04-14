user_input = input()

user_list = [int(num) for num in user_input.split() if int(num) >= 0]
user_list.sort()

for value in user_list:
    print(value, end=' ')




