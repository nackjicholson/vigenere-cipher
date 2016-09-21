import unittest
from vigenere_cipher.cipher import (
    VigenereCipher,
    combine_character,
    extend_keyword
)


class TestVigenereCipher(unittest.TestCase):
    def test_encode(self):
        """should encode plaintext against keyword"""
        keyword = 'TRAIN'
        plaintext = 'ENCODEDINPYTHON'
        cipher = VigenereCipher(keyword)

        actual = cipher.encode(plaintext)
        expected = 'XECWQXUIVCRKHWA'

        self.assertEqual(actual, expected)

    def test_encode_character(self):
        """should encode single character against keyword"""
        keyword = 'TRAIN'
        plaintext = 'E'
        cipher = VigenereCipher(keyword)

        actual = cipher.encode(plaintext)
        expected = 'X'

        self.assertEqual(actual, expected)

    def test_encode_spaces(self):
        """should strip plaintext of spaces before encoding"""
        keyword = 'TRAIN'
        plaintext = 'ENCODED IN PYTHON'
        cipher = VigenereCipher(keyword)

        actual = cipher.encode(plaintext)
        expected = 'XECWQXUIVCRKHWA'

        self.assertEqual(actual, expected)

    def test_encode_lowercase(self):
        """should convert plaintext to uppercase before encoding"""
        keyword = 'TRAIN'
        plaintext = 'encoded IN PYTHON'
        cipher = VigenereCipher(keyword)

        actual = cipher.encode(plaintext)
        expected = 'XECWQXUIVCRKHWA'

        self.assertEqual(actual, expected)


class TestCombineCharacter(unittest.TestCase):
    def test_combine_character(self):
        """
        should perform lookup of plain and
        keyword chars to get cipher char
        """
        self.assertEqual(combine_character('E', 'T'), 'X')
        self.assertEqual(combine_character('N', 'R'), 'E')


class TestExtendKeyword(unittest.TestCase):
    def test_extend_keyword(self):
        """should extend keyword by desired length"""
        actual = extend_keyword('TRAIN', 16)
        expected = 'TRAINTRAINTRAINT'

        self.assertEqual(actual, expected)
