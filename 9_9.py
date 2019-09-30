def rev(word):
    result = ''
    for letter in word:
        result = letter + result
    return result

for gap in range(10, 60):
    age = []
    count = 0
    for mom in range(10,120):
        child = mom - gap
        schild = str(child)
        smom = str(mom)
        if child > 0:
            if child < 10:
                schild = '0' + str(child)
            if smom == rev(schild):
                age.append(smom + ' and ' + str(child))
                count += 1
    if count >= 8:
        for pair in age:
            print(pair)