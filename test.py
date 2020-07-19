def add(num1, num2):
    return num1 + num2


def sub(num1, num2):
    return num1 - num2


def mult(num1, num2):
    return num1 * num2


def div(num1, num2):
    if(num1 > num2):
        print("your first value should be greater")
        return 0
    return num2 / num1


sum = add(4, 7)
print(sum)

diff = sub(27, 13)
print(diff)

product = mult(5, 3)
print(product)

quotient = div(3, 15)
print(quotient)

quotient = div(15, 3)
print(quotient)
