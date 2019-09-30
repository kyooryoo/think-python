import bisect

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

def in_bisect_cheat(wlist, word):
    i = bisect.bisect_left(wlist, word)
    if i == len(wlist):
        return False
    return wlist[i] == word

wlist = to_list()
for word in ['aa', 'alien', 'allen', 'zymurgy']:
    print('in_bisect:', word, 'in list', in_bisect(wlist, word))
    print('in_bisect_cheat:', word, 'in list', in_bisect_cheat(wlist, word))
