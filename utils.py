import string


def get_word_at_pos(str, pos):
    if pos < 0:
        return None
    word_chars = string.ascii_letters + string.digits + "._"
    if str[pos] not in word_chars:
        return None
    beg = pos
    while beg >= 1 and str[beg - 1] in word_chars:
        beg -= 1
    end = pos
    while end < len(str) - 1 and str[end + 1] in word_chars:
        end += 1
    return str[beg:end + 1]
