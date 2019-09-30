def noe(s):
    index = 0
    while index < len(s):
        letter = s[index].lower()
        if letter.lower() == 'e':
            return False
        index += 1
    return True

count = 0
total = 0
fin = open('words.txt')

for line in fin:
    total += 1
    word = line.strip().strip(' ')
    if noe(word):
        count += 1
        print(word)

print(count/total)