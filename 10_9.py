def tolist1():
    res = []
    fin = open('words.txt')
    for line in fin:
        word = line.strip().strip(' ')
        res.append(word)
    return res

def tolist2():
    res = []
    fin = open('words.txt')
    for line in fin:
        word = line.strip().strip(' ')
        res += [word]
    return res

# uncomment to compare two results
#print(tolist1() == tolist2())

# toggle comment below to test performance
tolist1()
#tolist2()

