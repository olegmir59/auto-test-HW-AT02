import pytest
from main2 import is_palindrome  # замените my_module на имя вашего модуля

def test_is_palindrome_true():
   assert is_palindrome("madam") == True

def test_is_palindrome_false():
   assert is_palindrome("hello") == False

@pytest.mark.parametrize("s, expected", [
   ("racecar", True),
   ("python", False),
   ("level", True),
   ("", True),  # Пустая строка является палиндромом
])
def test_is_palindrome_parametrized(s, expected):
   assert is_palindrome(s) == expected