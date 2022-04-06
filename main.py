#1
duration = int(input("Секунды: "))

day = duration // (24 * 3600)
duration %= (24 * 3600)
hour = duration // 3600
duration %= 3600
minutes = duration // 60
duration %= 60

if day >= 1:
    print(day, "дн", hour, "час", minutes, "мин", duration, "сек")
elif hour >= 1:
    print(hour, "час", minutes, "мин", duration, "сек")
elif minutes >= 1:
    print(minutes, "мин", duration, "сек")
elif duration < 60:
    print(duration, "сек")

#2
cube = []
for i in range(1, 1000, 2):
    cube.append(i ** 3)
sum_1 = 0
for i in cube:
    summa = 0
    m = i
    while i > 0:
        summa += i % 10
        i //= 10
    if summa % 7 == 0:
        sum_1 += m
print(sum_1)

#3
word = 'процент'

for i in range(1, 101):

    if i == 11 or i == 12 or i == 13 or i == 14:
        print(i, word + "ов")
    elif i % 10 == 1:
        print(i, word)
    elif 2 <= i % 10 < 5:
        print(i, word + "а")
    else:
        print(i, word + "ов")


