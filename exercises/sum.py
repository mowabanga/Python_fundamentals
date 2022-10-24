digit_1 = int(input("Input digit: "))
digit_2 = int(input("Input digit: "))
digit_3 = int(input("Input digit: "))
sum = digit_1 + digit_2 + digit_3
if digit_1== digit_2 and digit_1 == digit_3:
    print(sum * 3)
else:
    print(sum)