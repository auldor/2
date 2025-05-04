def product(x, y):
    dob = 1
    for i in range(x, y + 1):
        if i % 2 == 1:
            dob *= i
    return dob
