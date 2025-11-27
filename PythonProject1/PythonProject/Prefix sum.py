# Завдання 1.
# Дано масив цілих чисел a.
# Побудуйте масив префіксних сум prefix, де prefix[i] = a[0] + a[1] + ... + a[i].
# Виведіть отриманий масив.

a = [1, 2, 3, 4, 5]
prefix = []
current_sum = 0
for x in a:
    current_sum += x
    prefix.append(current_sum)

print(prefix)


# Завдання 2.
# Дано масив a та індекси l і r.
# Використовуючи масив префіксних сум, знайдіть суму елементів на відрізку [l, r].

l = 1
r = 3
if l == 0:
    result = prefix[r]
else:
    result = prefix[r] - prefix[l - 1]

print(result)


# Завдання 3.
# Дано масив a і список запитів у вигляді пар (l, r).
# Для кожного запиту знайдіть суму елементів на відрізку [l, r], використовуючи префіксні суми.

queries = [(0, 2), (1, 3), (2, 4)]
for l, r in queries:
    if l == 0:
        s = prefix[r]
    else:
        s = prefix[r] - prefix[l - 1]
    print(s)


# Завдання 4.
# Дано масив чисел a та число k.
# Знайдіть максимальну суму підмасиву довжини k (використовуйте префіксні суми або ковзне вікно).

k = 3
window_sum = sum(a[:k])
max_sum = window_sum
for i in range(k, len(a)):
    window_sum += a[i] - a[i - k]
    max_sum = max(max_sum, window_sum)

print(max_sum)


# Завдання 5.
# Дано масив a і число S.
# Визначте, чи існує такий підмасив [l, r], що його сума дорівнює S.
# Використайте префіксні суми.

S = 6
prefix_sum = 0
seen = {0}
found = False
for x in a:
    prefix_sum += x
    if prefix_sum - S in seen:
        found = True
        break
    seen.add(prefix_sum)

print(found)
