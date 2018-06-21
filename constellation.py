zodiac_name = (u"白羊座", u"金牛座", u"双子座", u"巨蟹座", u"狮子座", u"处女座", u"天秤座",
               u"天蝎座", u"射手座", u"魔羯座", u"水瓶座", u"双鱼座")
zodiac_days = ((1, 20), (2, 10), (4, 21), (5, 21), (6, 22),
               (7, 23), (9, 23), (10, 23), (11, 23), (12, 23))

(month, day) = (12, 31)
zodiac_day = filter(lambda x: x <= (month, day), zodiac_days)
zodiac_len = len(list(zodiac_day))
print(zodiac_name[zodiac_len])
