from mod import product

def expression(m):
    z = -(m ** 0.5)
    return z


try:
    m = int(input("Введіть значення m: "))
    print("Значення виразу z =", expression(m))
except:
    print("Помилка! Введіть ціле число.")


try:
    x = int(input("Введіть від якого числа (x) знаходити добуток непарних чисел: "))
    y = int(input("Введіть до якого числа (y) знаходити добуток непарних чисел: "))

    while x > y:
        print("x не може бути більшим за y. Спробуйте ще раз.")
        x = int(input("Введіть x: "))
        y = intD(input("Введіть y: "))

    result = product(x, y)
    print("Добуток непарних чисел від x до y =", result)
except:
    print("Помилка! Введіть цілі числа.")
