from unittest import TestCase
from fibonacci import do_fibonacci
import pytest


class TestCaseFibonacci(TestCase):

    def test_list_positive(self):
        assert do_fibonacci(10) == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
        assert do_fibonacci('20') == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181]

    def test_exception(self):
        with pytest.raises(TypeError):
            do_fibonacci()
        with pytest.raises(ValueError):
            do_fibonacci('qwerty')
        with pytest.raises(ValueError):
            do_fibonacci(0)
        with pytest.raises(ValueError):
            do_fibonacci(-6)
