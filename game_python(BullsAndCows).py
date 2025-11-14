import random

print("Введите диапазон!")
a1 = int(input("Введите первое число: "))
b2 = int(input("Введите второе число: "))

min_chislo = min(a1, b2)
max_chislo = max(a1, b2)

print(f"Угадай число от " + str(min_chislo) + " до " + str(max_chislo))
chislo = random.randint(min_chislo, max_chislo)
schet = 0

while True:
    schet = schet + 1
    print("Попытка", schet)
    otvet = input("Введи число: ")

    if not otvet.isdigit():
        print("Это не число! Попробуй ещё раз")
        continue

    otvet = int(otvet)

    if otvet < chislo:
        print("Загаданное число больше")
    elif otvet > chislo:
        print("Загаданное число меньше")
    else:
        print("Ты угадал! Поздравляю!")
        print("Тебе понадобилось", schet, "попыток")
        break