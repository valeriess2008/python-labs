import math

v0 = 15
f = 0.1
g = 9.8

for a in range(0, 61, 10):
    alpha = math.radians(a)
    s = v0 ** 2 / (2 * g * (f * math.cos(alpha) + math.sin(alpha)))
    print("Угол:", a, "Путь:", round(s, 2))





n = input("Введите целое число N: ")

while not n.isdigit() or int(n) <= 1:
    print("Ошибка! Введите целое число больше 1")
    n = input("Введите целое число N: ")

n = int(n)

k = 0

while 3 ** k <= n:
    k += 1

print("Наименьшее k =", k)

