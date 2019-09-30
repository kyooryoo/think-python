fin = open('words.txt')
for line in fin:
    word = line.strip().strip(' ')
    if len(word) > 20:
        print(word)