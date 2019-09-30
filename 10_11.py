def to_list():
    res = []
    fin = open('words.txt')
    for line in fin:
        word = line.strip()
        res.append(word)
    return res

def in_bisect(wlist, word):
    if len(wlist) == 0:
        return False
    i = len(wlist)//2
    if wlist[i]==word:
        return True
    if wlist[i] > word:
        return in_bisect(wlist[:i],word)
    else:
        return in_bisect(wlist[i+1:],word)

def interlock(wlist, word):
    word1 = word[::2]
    word2 = word[1::2]
    word1in = in_bisect(wlist, word1)
    word2in = in_bisect(wlist, word2)
    return word1in and word2in
        

def interlock_general(wlist, word, n=3):
    for i in range(n):
        inter = word[i::n]
        if not in_bisect(wlist, inter):
            return False
    return True

wlist = to_list()

for word in wlist:
    if interlock(wlist, word):
        print(word, word[::2], word[1::2])

for word in wlist:
    if interlock_general(wlist, word, 3):
        print(word, word[0::3], word[1::3], word[2::3])