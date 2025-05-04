import math
import random


def calc(m, n):
    top = math.sqrt(2) - math.sqrt(3 * n)
    bottom = 2 * m
    return top / bottom


def game():
    secret = random.randint(1, 100)
    print("Я загадав число від 1 до 100. Спробуй вгадати!")

    while True:
        try:
            guess = int(input("Твоя спроба: "))
            if guess < secret:
                print("Більше")
            elif guess > secret:
                print("Менше")
            else:
                print("Ти вгадав!")
                break
        except:
            print("Введи ціле число")


try:
    m = float(input("Введи m: "))
    n = float(input("Введи n: "))
    result = calc(m, n)
    print("Результат:", result)
except:
    print("Помилка вводу")

game()
