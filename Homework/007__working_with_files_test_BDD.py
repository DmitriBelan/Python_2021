# Домашнее задание:
# Написать программу, которая открывает файл с книгой (любая на выбор, можно использовать trimushketera.txt)
# Программа подсчитывает общее кол-во слов, а так же кол-во уникальных слов.
# Условия:
# Регистр букв не влияет на уникальность: Программа и программа - одно и то же слово
# Знаки препинания не должны влиять на уникальность: "прогрмма" и "программа," - одно и то же слово (договорились что точка, запятая, восклицательный знак, вопросительный знак)
# Результаты записывает в новый файл.
# Дополнительно:
# Записать все уникальные слова в тот-же файл, в алфавитном порядке

with open('../text_files/trimushketera.txt', 'r', encoding='UTF8') as file:
    file_content = file.read()

    # Очистка данных
    content_cleaned = file_content.split(' ')

    for word in content_cleaned:
        word.strip()
        word.replace("-", "").replace(",", "").replace(":", "").replace(";", "")\
            .replace("!", "").replace("?", "").replace("-", "").replace("\n", "")
        word.lower()

    # Количество слов в тексте
    words_amount = len(content_cleaned)
    print('Text consists of: ', words_amount, " words")

    # Количество уникальных слов в тексте
    unique = set(content_cleaned)
    unq_words_amount = len(unique)

    print('Unique words qty: ', unq_words_amount, " words")

    # Отсортировать список уникальных слов
    unique_sorted = sorted(unique)

    #Создать новый файл и записать в него результаты подсчетов

with open('../text_files/trimushketera_result.txt', 'w', encoding='UTF8') as new_file:
    new_file.write('Text consists of: \n')
    new_file.write(str(words_amount))
    new_file.write(' words')
    new_file.write('Unique words qty: \n')
    new_file.write(str(unq_words_amount))
    new_file.write(' words\n')
    new_file.write('List of unique words: \n')
    new_file.write(str(unique))

