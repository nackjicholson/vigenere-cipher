import unittest
from vigenere_cipher.cipher import VigenereCipher, combine_character, extend_keyword

class TestVigenereCipher(unittest.TestCase):
    def test_encode(self):
        keyword = 'TRAIN'
        plaintext = 'ENCODEDINPYTHON'
        cipher = VigenereCipher(keyword)

        actual = cipher.encode(plaintext)
        expected = 'XECWQXUIVCRKHWA'

        msg = 'should encode plaintext against keyword'
        self.assertEqual(actual, expected, msg=msg)

    def test_encode_character(self):
        keyword = 'TRAIN'
        plaintext = 'E'
        cipher = VigenereCipher(keyword)

        actual = cipher.encode(plaintext)
        expected = 'X'

        msg = 'should encode single character against keyword'
        self.assertEqual(actual, expected, msg=msg)

    def test_encode_spaces(self):
        keyword = 'TRAIN'
        plaintext = 'ENCODED IN PYTHON'
        cipher = VigenereCipher(keyword)

        actual = cipher.encode(plaintext)
        expected = 'XECWQXUIVCRKHWA'

        msg = 'should strip plaintext of spaces before encoding'
        self.assertEqual(actual, expected, msg=msg)

    def test_encode_lowercase(self):
        keyword = 'TRAIN'
        plaintext = 'encoded IN PYTHON'
        cipher = VigenereCipher(keyword)

        actual = cipher.encode(plaintext)
        expected = 'XECWQXUIVCRKHWA'

        msg = 'should convert plaintext to uppercase before encoding'
        self.assertEqual(actual, expected, msg=msg)

class TestCombineCharacter(unittest.TestCase):
    def test_combine_character(self):
        self.assertEqual(combine_character('E', 'T'), 'X')
        self.assertEqual(combine_character('N', 'R'), 'E')

class TestExtendKeyword(unittest.TestCase):
    def test_extend_keyword(self):
        actual = extend_keyword('TRAIN', 16)
        expected = 'TRAINTRAINTRAINT'

        msg = 'should extend keyword by desired length'
        self.assertEqual(actual, expected, msg=msg)
