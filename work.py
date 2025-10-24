# ==========================================
#       ТЕМА: ШВИДКЕ СОРТУВАННЯ (Quick Sort)

# ---------------------------------------------------
# Завдання 1.
# Реалізуйте класичний алгоритм Quick Sort для списку чисел.
# Вхід: [5, 2, 9, 1, 7]
# Вихід: [1, 2, 5, 7, 9]
# ---------------------------------------------------

def quick_sort(arr):
# TODO: напишіть свій код тут
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

print(quick_sort([5, 2, 9, 1, 7]))

# ---------------------------------------------------
# Завдання 2.
# Використайте Quick Sort, щоб відсортувати список імен
# за алфавітом.
# Вхід: ["Олег", "Іван", "Марія", "Андрій"]
# Вихід: ["Андрій", "Іван", "Марія", "Олег"]
# ---------------------------------------------------

names = ["Олег", "Іван", "Марія", "Андрій"]
# TODO: застосуйте функцію quick_sort() для списку names
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

sorted_names = quick_sort(names)
print(sorted_names)

# ---------------------------------------------------
# Завдання 3.
# Відсортуйте список чисел у спадаючому порядку.
# Використайте Quick Sort, але змініть умову порівняння.
# Вхід: [3, 1, 6, 2, 9]
# Вихід: [9, 6, 3, 2, 1]
# ---------------------------------------------------

def quick_sort_desc(arr):
    # TODO: реалізуйте quick sort для сортування за спаданням
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x > pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x < pivot]
    return quick_sort_desc(left) + middle + quick_sort_desc(right)
print(quick_sort_desc([3, 1, 6, 2, 9]))

# ---------------------------------------------------
# Завдання 4.
# Порахуйте кількість кроків (рекурсій), які виконує Quick Sort.
# Для цього додайте лічильник у функцію.
# ---------------------------------------------------

steps = 0

def quick_sort_count(arr):
    global steps
    # TODO: реалізуйте quick sort і рахуйте кроки
    steps += 1
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort_count(left) + middle + quick_sort_count(right)

nums = [3, 1, 6, 2, 9]
steps = 0
quick_sort_count(nums)

print(steps)  # виводимо тільки кількість кроків
# ---------------------------------------------------
# Завдання 5.
# Є список пар (ім’я, бал):
# [("Іван", 85), ("Марія", 90), ("Олег", 70)]
# Відсортуйте за балом у зростаючому порядку.
# Вихід: [("Олег", 70), ("Іван", 85), ("Марія", 90)]
# ---------------------------------------------------

students = [("Іван", 85), ("Марія", 90), ("Олег", 70)]

def quick_sort_by_score(data):
    # TODO: реалізуйте quick sort для сортування за другим елементом кортежу
    if len(data) <= 1:
        return data
    pivot = data[len(data) // 2][1]  # опорний елемент — бал (другий елемент)
    left = [x for x in data if x[1] < pivot]  # менші бали
    middle = [x for x in data if x[1] == pivot]  # рівні бали
    right = [x for x in data if x[1] > pivot]  # більші бали
    return quick_sort_by_score(left) + middle + quick_sort_by_score(right)

print(quick_sort_by_score(students))
# ---------------------------------------------------
# ТЕСТИ (після виконання всіх завдань)
# ---------------------------------------------------

if __name__ == "__main__":
    print("Тест 1:", quick_sort([5, 2, 9, 1, 7]))
    print("Тест 2:", quick_sort(names))
    print("Тест 3:", quick_sort_desc([3, 1, 6, 2, 9]))
    steps = 0
    quick_sort_count([5, 3, 8, 1, 9])
    print("Кількість кроків (Завдання 4):", steps)
    print("Тест 5:", quick_sort_by_score(students))
