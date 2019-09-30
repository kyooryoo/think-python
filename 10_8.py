from random import randint

def has_duplicates(t):
    for i in range(len(t)):
        for j in range(i+1,len(t)):
            if t[i] == t[j]:
                return True
    return False

def birthday():
    count = 0
    for j in range(10000):
        t = []
        for i in range(23):
            t.append(randint(1,365))
        if has_duplicates(t):
            count += 1
    return(count/10000)

print(birthday())