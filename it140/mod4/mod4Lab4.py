#Mad Lib - loops

#Mad Libs are activities that have a person provide various words,
# which are then used to complete a short story in unexpected (and hopefully funny) ways.

#Write a program that takes a string and integer as input,
# and outputs a sentence using those items as below. The program repeats until the input string is quit.

string = input('')
noun, count = string.split()
while noun != 'quit':
    print('Eating {} {} a day keeps the doctor away.'.format(count, noun))
    string = input('')
    noun, count = string.split()