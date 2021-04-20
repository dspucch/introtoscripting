#Dominic Spucches

import csv

file_input = input('')

wordsFreq = {}

with open(file_input, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    for row in csvreader:
        for word in row:
            if word not in wordsFreq.keys():
                wordsFreq[word] = 1
            else:
                wordsFreq[word] += 1

    for key in wordsFreq.keys():
        print(key, str(wordsFreq[key]))
