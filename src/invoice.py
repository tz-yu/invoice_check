
winning_number = ['04667172', '12999667', '77607087']
#unit test
def get_last_n_digits(ticket, n):
    return ticket[-n:]

if __name__ == "_main_":
    ticket = '04667172'
    last_4_digits = get_last_n_digits(check, 4)
    assert(last_4_digits) == '7172'

def get__max_maches_for_win_num(ticket,win_num):
    matches = 0
    for i in range(3,9):
        last_n_digits = get_last_n_digits(ticket, i)
        t = get_last_n_digits(ticket, i)
        w = get_last_n_digits(win_num, i)
        if t == w:
            match_count = i
        else:
            break
    return match_count