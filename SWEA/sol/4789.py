for tc in range(1, int(input())+1):
    num = input()
    result = count = 0
    for i in range(len(num)):
        if num[i] != '0':
            if i > count:
                result += i - count
                count += i - count
            count += int(num[i])
    print("#{} {}".format(tc, result))
