def add(n1, n2):
    return n1 + n2


def sub(n1, n2):
    return n1 - n2


def mult(n1, n2):
    return n1 * n2


def div(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": sub,
    "*": mult,
    "/": div
}


def calc():
    num1 = float(input("type the first number"))
    repo = True
    while repo:
        operation = str(input('"type a mathematical operator (a choice of "+", "-", "*" or "/")'))
        num2 = float(input("2nd number"))
        answer = operations[operation](num1, num2)
        print(answer)

        repeat = str(input("if the user wants to continue working with the previous result.")).lower()

        if repeat == "y":
            num1 = answer
            print(num1)

        else:
            repo = False
            calc()


calc()

