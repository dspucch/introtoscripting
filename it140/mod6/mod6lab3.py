user_input = input('')
word = user_input.split()

for ele in word:
    freq = word.count(ele)
    print(ele, freq)


