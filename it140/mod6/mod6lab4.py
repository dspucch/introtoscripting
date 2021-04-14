def replaceWords():

    replace_words = input()
    sentence = input()

    words = replace_words.split()
    word_dict = {}
    for i in range(0, len(words), 2): word_dict[words[i]] = words[i + 1]
    replaced_line = ''
    for word in sentence.split():
        if word in word_dict:
            replaced_line += word_dict[word] + ' '
        else:
            replaced_line += word + ' '
    print(replaced_line.strip())
replaceWords()