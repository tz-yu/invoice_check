
winning_number = ['04667172', '12999667', '77607087']
#unit test
def get_last_n_digits(ticket, n):
    return ticket[-n:]

if __name__ == "_main_":
    ticket = '04667172'
    last_4_digits = get_last_n_digits(check, 4)
    assert(last_4_digits) == '7172'S