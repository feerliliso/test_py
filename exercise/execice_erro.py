a = 'abcde'

try:
    a[10]
except Exception as e:
    print("这个错误是 %s" % e)
a = ["a", "c", "d"]

try:
    a[10]
except Exception as e:
    print("这个错误是 %s" % e)
