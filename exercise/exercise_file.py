file = open('fi.txt','w')
file.write('my first file')
file.close()
file = open('fi.txt', 'w')
file.write('20186.10')
file.close()
file = open('fi.txt')
print(file.read())
file3 = open('fi.txt', 'a')
file3.write('2000.5.6')
file3.close()
file3 = open('fi.txt')
print(file3.read(7))
#print(file3.read())




