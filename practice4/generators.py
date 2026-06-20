def square_numbers(n):
    for i in range(n + 1):
        yield i ** 2


def even_numbers(n):
    for i in range(n + 1):
        if i % 2 == 0:
            yield i


def divisible_by_3_and_4(n):
    for i in range(n + 1):
        if i % 3 == 0 and i % 4 == 0:
            yield i


def squares(a, b):
    for i in range(a, b + 1):
        yield i ** 2


def countdown(n):
    for i in range(n, -1, -1):
        yield i


n = int(input("Enter n: "))

print("Squares up to n:")
for x in square_numbers(n):
    print(x)

print("Even numbers:")
print(", ".join(str(x) for x in even_numbers(n)))

print("Divisible by 3 and 4:")
for x in divisible_by_3_and_4(n):
    print(x)

a = int(input("Enter a: "))
b = int(input("Enter b: "))

print("Squares from a to b:")
for x in squares(a, b):
    print(x)

print("Countdown:")
for x in countdown(n):
    print(x)