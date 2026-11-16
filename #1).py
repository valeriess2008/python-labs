#1)
text = input("Введите текст: ")
s = "бвгджзйклмнпрстфхцчшщ"

mx = -1
res = ""

for word in text.split():
    k = 0
    for i in word.lower():
        if i in s:
            k += 1

    if k / len(word) > mx:
        mx = k / len(word)
        res = word

print("Исходный текст:", text)
print("Результат:", res)

#2)

text = input("Введите текст: ")
s = "бвгджзйклмнпрстфхцчшщ"
k = 0

for word in text.split():
    word = word.lower()

    for i in range(len(word) - 1):
        if word[i] == word[i + 1] and word[i] in s:
            k += 1
            break

print("Исходный текст:", text)
print("Количество слов:", k)

#3)

import random

while True:
    n = input("Введите размер списка: ")
    if n.isdigit() and int(n) > 0:
        n = int(n)
        break
    print("Ошибка ввода")

a = []

for i in range(n):
    a.append(random.randint(-10, 10))

print("Исходный список:", a)

k = 0

for i in range(n):
    if a[i] > a[k]:
        k = i

print("Номер максимального элемента:", k + 1)

for i in range(n):
    for j in range(n - 1 - i):
        if abs(a[j]) > abs(a[j + 1]):
            a[j], a[j + 1] = a[j + 1], a[j]

print("Изменённый список:", a)
