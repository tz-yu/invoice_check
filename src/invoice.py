# 函式：取得發票號碼的最後 n 位數字
def get_last_n_digits(ticket, n):
    return ticket[-n:]

# 函式：計算發票與中獎號碼之間的最大數字配對數目
def get_max_matches_for_win_num(ticket, win_num):
    match_count = 0
    # 迴圈從 3 到 8 之間的數字（包含 3 與 8）
    for i in range(3, 9):
        # 取得發票號碼與中獎號碼的最後 i 位數字
        t = get_last_n_digits(ticket, i)
        w = get_last_n_digits(win_num, i)
        # 比較發票號碼的最後 i 位數字與中獎號碼的最後 i 位數字
        if t == w:
            # 如果相符，將 match_count 變數更新為相符的數字位數 i
            match_count = i
    # 回傳找到的最大數字配對數目
    return match_count
 

if __name__ == "__main__":
    # 讀取使用者輸入的發票號碼
    ticket = input('請輸入發票號碼：')

    # winning_numbers為特別獎的號碼
    winning_numbers = ['04667172', '12999667', '77607087']
    # spe_num_one 和 spe_num_two 為特獎的號碼
    spe_num_one = '29268886'
    spe_num_two = '12912565'

    # 檢查是否中了特獎或特別獎
    if ticket == spe_num_one:
        print('恭喜中 1000 萬元！')
    elif ticket == spe_num_two:
        print('恭喜中 200 萬元！')
    else:
        max_matches = 0
        matching_win_num = ''  # 新增變數來保存找到的中獎號碼
        # 逐一檢查每個中獎號碼，找出給定發票的最大數字配對數目
        for win_num in winning_numbers:
            match_count = get_max_matches_for_win_num(ticket, win_num)
            if match_count > max_matches:
                max_matches = match_count
                matching_win_num = win_num  # 更新找到的中獎號碼

        # 輸出找到的最大數字配對數目及對應的中獎號碼
        print(f"發票號碼 {ticket} 與中獎號碼 {matching_win_num} 的最大數字配對數目：{max_matches}")

        # 根據最大數字配對數目顯示中獎獎金
        if max_matches == 8:
            print('恭喜中 20 萬元！')
        elif max_matches == 7:
            print('恭喜中 4 萬元！')
        elif max_matches == 6:
            print('恭喜中 1 萬元！')
        elif max_matches == 5:
            print('恭喜中 4000 元！')
        elif max_matches == 4:
            print('恭喜中 1000 元！')
        elif max_matches == 3:
            print('恭喜中 200 元！')
        else:
            print('沒中QQ')
