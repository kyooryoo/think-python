def uses_only(s,ls):
    for idxl in range(len(ls)):
        flag = False
        for idxs in range(len(s)):
            if s[idxs] == ls[idxl]:
                flag = True
            idxs += 1
        idxl += 1
    return flag

print(uses_only('abcdabcd', 'abcd'))
print(uses_only('abcdabcd', 'abce'))