from art import logo


## Calculator
# Add
def add(n1, n2):
  return n1 + n2


# Subtract
def substract(n1, n2):
  return n1 - n2


# Multiply
def multiply(n1, n2):
  return n1 * n2


# Divide
def divide(n1, n2):
  return n1 / n2


## create a dictionary named operations
operations = {"+": add, "-": substract, "*": multiply, "/": divide}


def calculator():
  print(logo)

  num1 = float(input("What's the first number?: "))
  for symbol in operations:
    print(symbol)

  is_end = False
  while not is_end:
    operation_symbol = input("Pick an operation: ")
    num2 = float(input("What's the next numer?: "))
    calculation_function = operations[operation_symbol]
    answer = calculation_function(num1, num2)

    print(f"{num1} {operation_symbol} {num2} = {answer}")

    # is_going = input(f"Type 'y' to continue caculating with {answer}, or type 'n' to exit.: ")
    is_going = input(
        f"Type 'y' to continue caculating with {answer}, or type 'n' to start a new calculation.: "
    )
    if is_going == "n":
      is_end = True
      calculator()  # recursion function to start a new calcuation
    else:
      num1 = answer


calculator()
