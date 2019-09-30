def avoids(s, ls):
    idxs = 0
    while idxs < len(s):
        idxl = 0
        while idxl < len(ls):
            if s[idxs] == ls[idxl]:
                return False
            idxl += 1
        idxs += 1
    return True

total = 0
count = 0
fin = open('words.txt')

for line in fin:
    word = line.strip().strip(' ')
    if avoids(word, 'abcts'):
        print(word)
        count += 1
    total += 1

print(count/total)

