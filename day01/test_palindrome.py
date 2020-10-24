from unittest import TestCase
from palindrome import is_palindrome
import pytest


class TestCasePalindrome(TestCase):

    def test_string_positive(self):
        assert is_palindrome('qwertyytrewq')
        assert is_palindrome('1234321')
        assert is_palindrome(' qwerty ytrewq ')
        assert is_palindrome('qwertytrewq')
        assert is_palindrome('QwertytrewQ')

    def test_string_negative(self):
        assert is_palindrome('qwerty') is False

    def test_spaces_check(self):
        assert is_palindrome(' qwerty ytrewq ')
        assert is_palindrome(' qwertyytrewq') is False
        assert is_palindrome('qwertyytrewq ') is False
        assert is_palindrome('qwertyytr ewq') is False

    def test_case_check(self):
        assert is_palindrome('QwertyytrewQ') 
        assert is_palindrome('QWERTYYTREWQ')
        assert is_palindrome('qwertyYTREWQ') is False

    def test_exception(self):
        with pytest.raises(ValueError):
            is_palindrome('')
