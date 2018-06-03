chinese_zodiac = "猴鸡狗猪鼠牛虎兔龙蛇马羊"
#print(chinese_zodiac[-4])
year = int(input("请用户输入出生日期"))
if chinese_zodiac[year % 12] == "狗":
    print("狗年的运气")
for cz in chinese_zodiac:print(cz)


