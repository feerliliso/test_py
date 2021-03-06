from pandas import Series, DataFrame
import pandas as pd

# obj = Series([3, 4, 5, 6, -7])
# print(obj)
# print(obj.index)
# print(obj.values)
data = {'city': ['beijing', 'shanghai', 'shanghai', 'beijing', 'beijing'],
        'year': [2016, 2017, 2018, 2018, 2019],
        'pop': [1.5, 1.7, 3.6, 2.4, 2.9]
        }

frame = DataFrame(data)
frame2 = DataFrame(data, columns=['year', 'city', 'pop'])
# print(frame)
# print(frame2)
# print(frame2.city)
# print(frame2['city'])
frame2['new'] = 100
# print(frame2)
frame2['cap'] = frame2.city == 'beijing'
# print(frame2)
pop = {'beijing': {2008: 1.5, 2009: 2.0},
       'shanghai': {2008: 2.0, 2009: 3.0}

       }
frame3 = DataFrame(pop)
print(frame3)
print(frame3.T)
