def has_duplicates(t):
    for i in range(len(t)):
        for j in range(i+1,len(t)):
            if t[i] == t[j]:
                return True
    return False

t1 = [1,2,3]
t2 = [1,2,2]
res1 = has_duplicates(t1)
res2 = has_duplicates(t2)
print("{} has duplicates: {}".format(t1,res1))
print("{} has duplicates: {}".format(t2,res2))
