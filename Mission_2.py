from collections import deque

def get_neighbors(state):
    neighbors = []
    zero_index = state.index(0)
    row, col = zero_index // 4, zero_index % 4

    for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        new_row, new_col = row + dr, col + dc
        if 0 <= new_row < 4 and 0 <= new_col < 4:
            new_index = new_row * 4 + new_col
            new_state = state[:]
            new_state[zero_index], new_state[new_index] = new_state[new_index], new_state[zero_index]
            neighbors.append(new_state)

    return neighbors

# Проверить число инверсий: сколько меньших чисел
# стоят на местах с более высоким индексом
def count_inversions(state):
    inversions = 0
    for i in range(len(state)):
        for j in range(i+1, len(state)):
            if state[i] != 0 and state[j] != 0 and state[i] > state[j]:
                inversions += 1
    return inversions

def is_solvable(state):
    inversions = count_inversions(state)
    zero_index = state.index(0) # Определить индекс пустой клетки
    # Если пустая клетка в первом или третьем ряду, то для решаемости
    # число инверсий должно быть нечетным
    # Если во 2-м или 4-м ряду, то число инверсий должно быть четным
    if zero_index in [0,1,2,3,8,9,10,11]:
        return inversions % 2 == 1
    else:
        return inversions % 2 == 0

def solve_puzzle(initial_state):
    if not is_solvable(initial_state):
        return [] # Вернуть пустой массив, если задача нерешаема

    target_state = list(range(1, 16)) + [0] # Позиция для решения задачи
    visited = set() # Множество для записи уникальных положений поля
    queue = deque([(initial_state, [])])

    while queue:
        state, path = queue.popleft()
        if state == target_state:
            return path
        if tuple(state) in visited:
            continue
        visited.add(tuple(state))

        for neighbor in get_neighbors(state):
            queue.append((neighbor, path + [neighbor]))

    return []

# Функция для вывода в виде двумерного массива
def print_puzzle(state):
    for i in range(0, 16, 4):
        row = state[i:i+4]
        row_str = [f" {num}" if num < 10 else str(num) for num in row]
        print(row_str)


# Начальное состояние
initial_state = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 0, 13, 15, 14, 11]
result = solve_puzzle(initial_state)
#print(result) # Вывод в виде одномерного массива
# Вывод в виде двумерного массива
print("Исходные данные:")
print_puzzle(initial_state)
print()
if result:
    print("Решение задачи:")
    for step in result:
        print_puzzle(step)
        print()
else:
    print("Задача нерешаема")
    print(result)