#判断字符串的长度是否大于10
string = "the number is than ten"
if len(string) > 10:
    print("the string is more than 10 ")
    print(len(string))
elif len(string) == 10:
    print("the string long is 10")
elif len(string) < 10:
    print("the long of string is short 10")

number = int(input("请输入一个 1 到 40 之间的整数"))
if 1 < number <= 10:
    print("这个数在1到10之间")
if 11 <= number <= 20:
    print("这个数在11 到20之间")
if 21 <= number <= 30:
    print("这个数在21 到 30 之间")
if 31 <= number <= 40:
    print("这个数在31 到 40 之间")
if number > 40 or number < 1:
    print("这个数超过了判断范围，请重新输入")









