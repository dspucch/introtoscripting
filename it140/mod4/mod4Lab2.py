#Many user-created passwords are simple and easy to guess. Write a program that takes a simple password and makes it stronger by replacing characters using the key below, and by appending "q*s" to the end of the input string.

#i becomes !
#a becomes @
#m becomes M
#B becomes 8
#o becomes .

word = input()

word = word.replace('i','!')
word = word.replace('a','@')
word = word.replace('m','M')
word = word.replace('B','8')
word = word.replace('o','.')

word = word + 'q*s'

print(word)