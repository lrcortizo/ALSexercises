def format(num):
    for ch in ['+', '-', ' ', '(', ')']:
        if ch in num:
            num = num.replace(ch, '')

    #num = num.replace('-', '')
    #num = num.replace('+', '')
    #num = num.replace('-', '')
    #num = num.replace(' ', '')
    #num = num.replace('(', '')
    #num = num.replace(')', '')

    if num[0:2] == "00":
        num = num[2:]

    return num
    #if len(num) == 9:
    #    return str.format("{0} {1} {2}", num[0:2], num[3:5], num[6:8])
    #else:
     #   if num[0:1] == "00":
     #       return str.format("++{0} {1} {2} {3}", num[2:3], num[4:6], num[7:9], num[10:11])

print(format("123456789"))
print(format("0001-999-123456"))
print(format("+34 (988) 387 000"))
print(format("34(988)ESEI00"))