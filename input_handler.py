def get_number(prompt):
    try:
        return float(input(prompt))
    except ValueError:
        print("Invalid input! Please enter a number.")
        return get_number(prompt)

def get_operator():
    op = input("Enter operator (+, -, *, /): ")
    if op in ['+', '-', '*', '/']:
        return op
    else:
        print("Invalid operator!")
        return get_operator()
