max_error_count = 3
ans = 'a123456'
while True:
    # 1. 取得使用者輸入
    userIn = input('請輸入密碼: ')

    # 2. 驗證正確性
    if userIn == ans:
        # 2.1 正確則離開迴圈
        print('正確')
        break
    # 2.2. 錯誤時減少可嘗試次數
    max_error_count -= 1

    # 3. 檢核可嘗試次數
    if max_error_count == 0:
        # 3. 若可嘗試次數歸零則退出迴圈
        print('掰掰')
        break

    # 3. 若還可輸入則告知剩餘可嘗試次數
    print('密碼錯誤.還有 ', max_error_count, ' 次機會')
