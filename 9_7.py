def trible(word):
    for index in range(len(word)-5):
        if word[index]  == word[index+1]:
            if word[index+2]  == word[index+3]:
                if word[index+4]  == word[index+5]:
                    return True
    return False

count = 0
fin = open('words.txt')

for line in fin:
    word = line.strip().strip(' ')
    if trible(word):
        count += 1
        print(word)

print("there are {} trible words!".format(count))