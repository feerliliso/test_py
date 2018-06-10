chinese_zodiac = "猴鸡狗猪鼠牛虎兔龙蛇马羊"
zodiac_name = (u"白羊座", u"金牛座", u"双子座", u"巨蟹座", u"狮子座", u"处女座", u"天秤座",
               u"天蝎座", u"射手座", u"魔羯座", u"水瓶座", u"双鱼座")
zodiac_days = ((1, 20), (2, 10), (4, 21), (5, 21), (6, 22), (7, 23), (9, 23), (10, 23), (11, 23), (12, 23))

cz_num = {i: 0 for i in chinese_zodiac}
#for i in chinese_zodiac:
    #cz_num[i] = 0

z_num = {i: 0 for i in zodiac_name}
#for i in zodiac_name :
    #z_num[i] = 0
while True:
    # 用户输入月份和日期
    year = int(input('请输入年份'))
    month = int(input('输入月份'))
    day = int(input('输入日期'))

    n = 0
    while zodiac_days[n] < (month, day):
        if month == 12 and day > 23:
            break
        n += 1
    print(zodiac_name[n])
    print('%s 年的生肖是 %s' % (year, chinese_zodiac[year % 12]))
    cz_num[chinese_zodiac[year % 12]] += 1
    z_num[zodiac_name[n]] += 1
#输出生肖和星座的统计
    for each_key in cz_num.keys():
        print('%s 生肖有 %d 个' % (each_key, cz_num[each_key]))
    for each_key in z_num.keys():
        print('%s 的星座有 %d 个' % (each_key, z_num[each_key]))


