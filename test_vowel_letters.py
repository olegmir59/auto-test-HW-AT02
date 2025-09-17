import pytest
from main_vowel_letters import count_vowels
@pytest.fixture
def vowel_counter():
    return count_vowels

def test_only_vowels(vowel_counter):
    assert vowel_counter('aaaaAAEEEuuu') == 12

def test_no_vowels(vowel_counter):
    assert vowel_counter('bcdfghjklmnpqrstvwxyz') == 0

def test_mixed_case_string(vowel_counter):
    assert vowel_counter('Hello World!') == 3

def test_empty_string(vowel_counter):
    assert vowel_counter('') == 0

def test_non_ascii_characters(vowel_counter):
    assert vowel_counter('äöüÄÖÜ') == 6  # Специфичные немецкие гласные включены

def test_special_chars_and_numbers(vowel_counter):
    assert vowel_counter('123 !@#$%^&*()_+=-') == 0

def test_german_vowels(vowel_counter):
    assert vowel_counter('Straße äöü') == 5  # Дополнительно учтены специфичные немецкие гласные

def test_polish_vowels(vowel_counter):
    assert vowel_counter('Piękny dzień znaków specjalnych') == 7  # Учет польских гласных

def test_finnish_vowels(vowel_counter):
    assert vowel_counter('Hyvää päivää Suomi!') == 9  # Финские гласные

def test_russian_vowels(vowel_counter):
    assert vowel_counter('Москва красивая столица') == 9  # Российские гласные

