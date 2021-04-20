def readInputFile(filename):
   shows_dict = {}                                   #create an empty dictionary
   infile = open(filename, 'r')                   #open input file
   lines = infile.readlines()                       #read all lines of the file
   for i in range(0, len(lines), 2):               #loop for all lines, with increment of 2
       numOfSeasons = int(lines[i].strip())       #get number of seasons from ith line
       show = lines[i+1].strip()                   #get show name from (i+1)th line
       if numOfSeasons not in shows_dict.keys():   #create a key for numOfSeasons if it not exists
           shows_dict[numOfSeasons] = []
       shows_dict[numOfSeasons].append(show)        #add the show to the list of values for that key
   #print(shows_dict)
   return shows_dict                               #return the dictionary


def outputSortedbyKeys(dict, filename):
   print("Sorting by keys: ")
   outfile = open(filename,'w')                   #open output file for writing
   for key in sorted(dict.keys()):                   #sort the keys
       outfile.write('{}: {}\n'.format(key,'; '.join(dict.get(key))))   #write the key: values separated by ;
       print('{}: {}'.format(key,'; '.join(dict.get(key))))
   print(filename + " written successfully\n")


def outputSortedbyValues(dict, filename):
   titles = []
   for key in dict.keys():                           #get all the values and store in titles list
       for val in dict[key]:
           titles.append(val)
   outfile = open(filename,'w')                   #open output file for writing
   for title in sorted(titles):                   #sort the titles list and write to file
       outfile.write('{}\n'.format(title))
       print(title)
   print(filename + " written successfully\n")

def main():
   filename = input("Enter the input filename: ")       #read name of inputfile
   shows_dict = readInputFile(filename)               #read data from file and get the dictionary
   outputSortedbyKeys(shows_dict , 'output_keys.txt')   #sort and output dictionary sorted by keys
   outputSortedbyValues(shows_dict , 'output_titles.txt') #sort and output dictionary sorted by values

main()