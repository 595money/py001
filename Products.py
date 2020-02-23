import random

# for i in range(10):
#     print('第',i + 1 ,'次，數字為:', random.randint(1, 100))
#
# data = []
# with open('G:\Work\source\\file\\amazon_reviews.txt','r') as f:
#     data = [line for line in f if 'bad' in line]
#
# print(len(data))
data = []
while True:
    noodle_name = input('輸入麵: ')
    if noodle_name == 'q':
        print('結束')
        break
    noodle_price = input('輸入價格: ')
    data.append([noodle_name, noodle_price])

total_amt = 0
for price in data:
    total_amt += int(price[1])

print('總共花費: ', total_amt, '元')