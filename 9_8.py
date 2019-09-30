def is_palindrome(word):
    index = 0
    while index < len(word)//2:
        if word[index] != word[len(word)-index-1]:
            return False
        index += 1
    return True

count = 0
for num in range(100000,999996):
    num1 = str(num)[2:]
    num2 = str(num+1)[1:]
    num3 = str(num+2)[1:-1]
    num4 = str(num+3)

    if is_palindrome(num1) & is_palindrome(num2) \
        & is_palindrome(num3) & is_palindrome(num4):
        print(num)
        count += 1
    
print("there are {} numbers!".format(count))