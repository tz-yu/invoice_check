from src.invoice import get_last_n_digits ,import get__max_maches_for_win_num
def test_get_lastp_3_digits():
    ticket = '1234567890'
    last_3_digits = get_last_n_digits(ticket, 3)
    assert last_3_digits == '890'

def test_get_last_8_digits():
    ticket = '1234567890'
    last_8_digits = get_last_n_digits(ticket, 8)
    assert last_8_digits == '1234567890'



def test_max_3_match():
    ticket = '1234567890'
    win_num = '1234567890'
    max_matches = max_matches_for_win_num(ticket, win_num)
    assert max_matches == 3

def test_max_no_match():
    ticket = '1234567890'
    win_num = '1234567890'
    max_matches = max_matches_for_win_num(ticket, win_num)
    assert max_matches == 0

def test_max_8_match():
    ticket = '1234567890'
    win_num = '1234567890'
    max_matches = max_matches_for_win_num(ticket, win_num)
    assert max_matches == 0
