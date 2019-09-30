def is_anagram(s1,s2):
    t1 = list(s1)
    t2 = list(s2)
    return sorted(t1) == sorted(t2)

print(is_anagram('abcd','dcba'))
print(is_anagram('abcd','bcde'))