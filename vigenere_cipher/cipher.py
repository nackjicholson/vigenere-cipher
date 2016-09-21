def combine_character(plain, keyword):
    plain = plain.upper()
    keyword = keyword.upper()
    start_ord = ord('A')
    plain_num = ord(plain) - start_ord
    keyword_num = ord(keyword) - start_ord
    relative_ord = (plain_num + keyword_num) % 26
    return chr(start_ord + relative_ord)


def extend_keyword(keyword, number):
    repeats = number // len(keyword) + 1
    return (keyword * repeats)[:number]


class VigenereCipher:
    def __init__(self, keyword):
        self.keyword = keyword

    def encode(self, plaintext):
        cipher = []

        plaintext = plaintext.replace(' ', '').upper()
        extended_keyword = extend_keyword(self.keyword, len(plaintext))

        for p, k in zip(plaintext, extended_keyword):
            cipher.append(combine_character(p, k))

        return "".join(cipher)

