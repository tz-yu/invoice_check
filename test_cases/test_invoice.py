from src.invoice import get_last_n_digits, get_max_matches_for_win_num

# 測試函式 get_last_n_digits
def test_get_last_n_digits():
    ticket = '04667172'
    assert get_last_n_digits(ticket, 4) == '7172'
    assert get_last_n_digits(ticket, 3) == '172'
    assert get_last_n_digits(ticket, 2) == '72'
    assert get_last_n_digits(ticket, 1) == '2'

# 測試函式 get_max_matches_for_win_num
def test_get_max_matches_for_win_num():
    ticket = '04667172'
    winning_numbers = ['04667172', '12999667', '77607087']
    assert get_max_matches_for_win_num(ticket, winning_numbers[0]) == 8
    assert get_max_matches_for_win_num(ticket, winning_numbers[1]) == 0
    assert get_max_matches_for_win_num(ticket, winning_numbers[2]) == 1

# 檢查是否在主要程式碼中執行測試檔案
if __name__ == "__main__":
    test_get_last_n_digits()
    test_get_max_matches_for_win_num()
    print("所有測試通過！")
