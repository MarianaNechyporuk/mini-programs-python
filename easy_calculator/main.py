from art import logo
print(logo)

def add(n1, n2):
  return n1 + n2 

def subtrack(n1, n2):
  return n1 - n2 

def multiply(n1, n2):
  return n1 * n2 

def divide(n1, n2):
  return n1 / n2 

operations = {
  "+" : add, 
  "-" : subtrack, 
  "*" : multiply, 
  "/" : divide
}

def calculator():
  num1 = float(input("What's the first number? : "))
  for symbol in operations:
    print(symbol)
  should_continue = True
  
  while should_continue:
    operation_symbol = input("Pick an operation: ")
    num2 = float(input("What's the next number? : "))
    calc = operations[operation_symbol]
    result = calc(num1, num2)
  
    print(f"{num1} {operation_symbol} {num2} = {result}")
  
    if input(f"Type 'y' to continue calculating with {result}, or type 'n' to start again: ") == "y":
      num1 = result
    else:
      should_continue = False
      calculator()

calculator()
