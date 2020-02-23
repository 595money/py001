country = input('哪國: ')
age = int(input('幾歲: '))
if country == '台灣':
    if age >= 18:
        print('你可以開車')
elif country == '美國':
    if age >= 16:
        print('你可以開車')
else:
    print('你不可以開車')
x = 0
while x < 10:
    x += 1
    print('x = ', x)

