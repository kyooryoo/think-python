def cumsum(t):
    res = []
    for i in range(len(t)):
        sum = 0
        for j in range(i+1):
            sum += t[j]
        res.append(sum)
    return res

t = [1,2,3]
print(cumsum(t))