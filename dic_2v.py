chinese_zodiac = "猴鸡狗猪鼠牛虎兔龙蛇马羊"
zodiac_name = (u"白羊座", u"金牛座", u"双子座", u"巨蟹座", u"狮子座", u"处女座", u"天秤座",
               u"天蝎座", u"射手座", u"魔羯座", u"水瓶座", u"双鱼座")
zodiac_days = ((1, 20), (2, 10), (4, 21), (5, 21), (6, 22), (7, 23), (9, 23), (10, 23), (11, 23), (12, 23))
# 用户输入月份和日期
year = int(input('请输入年份'))
month = int(input('输入月份'))
day = int(input('输入日期'))
cz_num = {}
for i in chinese_zodiac:
    cz_num[i] = 0

n = 0
while zodiac_days[n] < (month, day):
    if month == 12 and day > 23:
        break
    n += 1
print(zodiac_name[n])
print('%s 年的生肖是 %s' % (year, chinese_zodiac[year % 12]))






