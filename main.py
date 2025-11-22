from input_handler import get_number, get_operator
from operations import add, subtract, multiply, divide
from output_handler import display_result

def main():
    print("----- Simple Calculator -----")

    num1 = get_number("Enter first number: ")
    num2 = get_number("Enter second number: ")
    operator = get_operator()

    if operator == '+':
        result = add(num1, num2)
    elif operator == '-':
        result = subtract(num1, num2)
    elif operator == '*':
        result = multiply(num1, num2)
    elif operator == '/':
        result = divide(num1, num2)

    display_result(result)

if __name__ == "__main__":
    main()
