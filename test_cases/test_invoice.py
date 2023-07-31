from src.invoice import get_last_n_digits

def test_get_lastp_3_digits():
    ticket = '1234567890'
    last_3_digits = get_last_n_digits(ticket, 3)
    assert last_3_digits == '890'

def test_get_last_8_digits():
    ticket = '1234567890'
    last_8_digits = get_last_n_digits(ticket, 8)
    assert last_8_digits == '1234567890'