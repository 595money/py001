# 產生一個隨機整數1~100 (不要印出來)
# 讓使用者重複輸入數字去猜
# 猜對的話 印出"終於猜對了"
# 猜錯的話 要告訴他 比答案大/小
import random

# 1. 隨機出正確答案
r = random.randint(1, 100)

# 2. 進入迴圈正確則離開
while True:
    # 3. 取得user 輸入
    userIn = int(input('請輸入數字: '))
    if  userIn == r:
        break
# 4.1 數字大則印"比答案大"，並回到 2
    if  userIn > r:
        print('比答案大')
# 4.2 數字小則印"比答案小"，並回到 2
    else:
        print('比答案小')
# 5. 印出"終於猜對了"
print('終於猜對了')

