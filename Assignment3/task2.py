import math

n = int(input("Enter a number: "))


def square():
    global n
    return math.sqrt(n)


def logarithm():
    global n
    return math.log(n)


def sine():
    global n
    return math.sin(n)


print("Square Root: ", square())
print("Logarithm: ", logarithm())
print("Sine: ", sine())
