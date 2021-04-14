user_input = input()
user_list = user_input.split()

for i in range(len(user_list)):
    user_list[i] = int(user_list[i])

average = sum(user_list) // len(user_list)
print(average, max(user_list))



