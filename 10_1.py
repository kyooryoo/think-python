def nested_sum(ts):
    total = 0
    for t in ts:
        for num in t:
            total += num
    return total

ts = [[1,2],[3],[4,5,6]]
print(nested_sum(ts))