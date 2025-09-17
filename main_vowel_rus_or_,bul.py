def count_vowels(s, language='all'):
    """
    Функция подсчета количества гласных букв в строке.
    :param s: Строка для анализа
    :param language: Язык ('rus', 'bulgar', 'all')
    :return: Количество гласных букв
    """
    if language == 'rus':
        vowels = 'аеёиоуыэюяАЕЁИОУЫЭЮЯ'  # Только русские гласные
    elif language == 'bulgar':
        vowels = 'аеёиоуыэюяАЕЁИОУЫЭЮЯъьЪЬ'  # Включая специфичные болгарские
    else:
        vowels = 'aeiouAEIOU' \
             'äöüæøÄÖÜÆØ' \
             'áéíóúůÁÉÍÓÚŮ' \
             'аеёиоуыэюяАЕЁИОУЫЭЮЯ'  # Общий набор для всех языков(без болгарского)
    return sum(1 for char in s if char in vowels)
