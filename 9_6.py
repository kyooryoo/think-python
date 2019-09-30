def is_abecedarian(s):
    for index in range(len(s)-1):
        if s[index] > s[index+1]:
            return False
    return True

count = 0
fin = open('words.txt')

for line in fin:
    word = line.strip().strip(' ')
    if is_abecedarian(word):
        count += 1

print("there are {} abecedarian".format(count))