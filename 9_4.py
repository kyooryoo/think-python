def uses_only(s,ls):
    idxs = 0
    while idxs < len(s):
        idxl = 0
        flag = False
        while idxl < len(ls):
            if s[idxs] == ls[idxl]:
                flag = True
            idxl += 1
        idxs += 1
    return flag

print(uses_only('abcdabcd', 'abcd'))
print(uses_only('abcdabcd', 'abc'))