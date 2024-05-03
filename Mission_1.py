from datetime import datetime as t

# Функция вывода результатов
def out(index,start_time):
    if index != -1:
        print(f"Подстрока найдена в позиции {index} в строке.")
    else:
        print("Подстрока не найдена в строке.")
    time = t.now() - start_time
    print(f"Время выполнения кода: {time}")

# Алгоритм КМП (Кнута-Морриса-Пратта)
def build_prefix_table(pattern): # Построение префикс таблицы
    prefix_table = [0] * len(pattern)
    j = 0
    for i in range(1, len(pattern)):
        while j > 0 and pattern[i] != pattern[j]:
            j = prefix_table[j - 1]
        if pattern[i] == pattern[j]:
            j += 1
        prefix_table[i] = j
    return prefix_table

def kmp_search(text, pattern):
    prefix_table = build_prefix_table(pattern) # Построить префикс таблицу для подстроки
    n = len(text) # Длина строки
    m = len(pattern) # Длина подстроки
    if m == 0:
        return 0
    i = 0 # Счетчики
    j = 0
    while i<n: # Проверяем посимвольно строку
        if text[i]==pattern[j]: # При совпадении увеличиваем счетчики i, j
            i = i+1
            j = j+1
            if j == m: # Если счетчик j сравнялся с длиной подстроки, то завершить функцию
                return i-j
        else: # При несовпадении символов строки и подстроки
            if j>0:
                j = prefix_table[j-1] # Заменить значение счетчика j на значение предыдущего элемента префикс таблицы
            else:
                i = i+1
    return -1


# Алгоритм БМ (Бойера-Мура)
def boyer_moore_search(text, pattern):
    n = len(text)
    m = len(pattern)
    if m == 0:
        return 0
    # Создаем таблицу сдвигов для каждого символа в подстроке
    shift_table = {}
    for i in range(m - 1):
        shift_table[pattern[i]] = m - i - 1
    i = m - 1  # Индекс в строке
    j = m - 1  # Индекс последнего символа в подстроке
    while i < n:
        if text[i] == pattern[j]:
            if j == 0:
                return i
            else:
                i -= 1
                j -= 1
        else:
            if text[i] in shift_table:
                i += shift_table[text[i]]
                j = m - 1
            else:
                i += m
                j = m - 1
    return -1


# Ввод строки и подстроки с клавиатуры
text = input("Введите строку: ")
pattern = input("Введите подстроку: ")

# Проверка на чувствительность к регистру
sensitive = input("Учитывать регистр? (да/нет): ")
if sensitive.lower() == "нет":
    text.lower()
    pattern.lower()


start_time = t.now()
index = kmp_search(text, pattern)
print("=== Алгоритм Кнута-Морриса-Пратта ===")
out(index,start_time)

start_time = t.now()
index = boyer_moore_search(text, pattern)
print("=== Алгоритм Бойера-Мура ===")
out(index,start_time)

start_time = t.now()
index = text.find(pattern)
print("=== Стандартная функция ===")
out(index,start_time)


# # Выбор метода поиска подстроки
# MFind = input("Выберите метод поиска (КМП (1) /БМ (2)/стд(что-угодно): ")
# MFind = MFind.lower()
# if MFind == "1":
#     start_time = t.now()
#     index = kmp_search(text, pattern)
# elif MFind == "2":
#     start_time = t.now()
#     index = boyer_moore_search(text, pattern)
# else:
#     start_time = t.now()
#     index = text.find(pattern)
#
# # Вывод результатов
# if index != -1:
#     print(f"Подстрока найдена в позиции {index} в строке.")
# else:
#     print("Подстрока не найдена в строке.")
# time = t.now() - start_time
# print(f"Время выполнения кода: {time}")