#write program whos input is two integers and whos output is the two integers swapped

def swap_values(user_val1, user_val2):
    temp = user_val1
    user_val1 = user_val2
    user_val2 = temp
    return user_val1, user_val2

if __name__ == '__main__':
    user_val1 = int(input())
    user_val2 = int(input())
    a, b = swap_values(user_val1, user_val2)
    print(a, b)