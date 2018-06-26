# We are making a clculator

def eval_two_nums(num1, num2, operator):

    while True:
        if operator == "+":
            answer = num1 + num2
            print("{} {} {} = {}".format(num1, operator, num2, answer))
            return answer
        elif operator == "-":
            answer = num1 - num2
            print("{} {} {} = {}".format(num1, operator, num2, answer))
            return answer
        elif operator == "/":
            answer = num1 / num2
            print("{} {} {} = {}".format(num1, operator, num2, answer))
            return answer
        elif operator == "*":
            answer = num1 * num2
            print("{} {} {} = {}".format(num1, operator, num2, answer))
            return answer



while True:
    try:
        num1 = int(input("What is the first number? "))
        num2 = int(input("What is the second number? "))
        operator = input("What operator shall we use? ")
        eval_two_nums(num1, num2, operator)
    except ValueError:
        print("Invalid input.")
        continue
    go_again = input("Would you like to enter another set of numbers? ")
    if go_again.lower in ["n", "no"]:
        print("Goodbye!")
        break
