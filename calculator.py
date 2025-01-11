def calculator():
 
  while True:
    try:
      num1 = float(input("Enter the first number: "))
      num2 = float(input("Enter the second number: "))
      operator = input("Enter the operator (+, -, *, /): ")

      if operator == '+':
        result = num1 + num2
      elif operator == '-':
        result = num1 - num2
      elif operator == '*':
        result = num1 * num2
      elif operator == '/':
        if num2 == 0:
          print("Error: Division by zero is not allowed.")
        else:
          result = num1 / num2
      else:
        print("Invalid operator. Please enter +, -, *, or /.")
        continue

      print("Result:", result)
      break

    except ValueError:
      print("Invalid input. Please enter valid numbers.")

if __name__ == "__main__":
  calculator()
  
  
  