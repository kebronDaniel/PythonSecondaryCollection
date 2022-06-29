
logo = '''
 _____________________
|  _________________  |
| | JO           0. | |
| |_________________| |
|  ___ ___ ___   ___  |
| | 7 | 8 | 9 | | + | |
| |___|___|___| |___| |
| | 4 | 5 | 6 | | - | |
| |___|___|___| |___| |
| | 1 | 2 | 3 | | x | |
| |___|___|___| |___| |
| | . | 0 | = | | / | |
| |___|___|___| |___| |
|_____________________|
'''


def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    if n2 == 0:
        return None
    return n1 / n2


def calculator():
    print(logo)
    oprerations = {
        "+": add,
        "-": subtract,
        "*": multiply,
        "/": divide
    }

    num1 = float(input("What is the first number? "))

    should_continue = True

    while should_continue:

        for opreator in oprerations:
            print(opreator)

        symbol = input("Select an operator from the above ones  ")

        num2 = float(input("What is the next number? "))

        function = oprerations[symbol]
        result = function(num1, num2)

        print(f"{num1} {symbol} {num2} = {result}")

        choice = input(
            "Type 'yes' to continue calculating or 'new' to start fresh or 'quit' to quit : ").lower()

        if choice == 'yes':
            num1 = result
        elif choice == 'new':
            calculator()
        else:
            should_continue = False


calculator()
