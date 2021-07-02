#AmrMuallaD10Calculator
def Add(n1, n2):
    answer = n1 + n2
    return answer

def Subtract(n1, n2):
    answer = n1 - n2
    return answer

def Multiply(n1,n2):
    answer = n1 * n2
    return answer

def Divide(n1, n2):
    answer = (n1/n2)
    return answer

operations = {}
operations["+"] = Add
operations["-"] = Subtract
operations["*"] = Multiply
operations["/"] = Divide

def Calculating():
  num1 = float(input("What is the first number?: "))
  num2 = float(input("What is the second number?: "))

  for symbol in operations:
    print(symbol)

  what_operation = input("What operation do you wish to perform? Choose from the symbols above: ")
  calculation = operations[what_operation]
  answer = calculation(num1, num2)

  print(f"The calculation of {num1} {what_operation} {num2} = {answer}")

  more = input("Would you like to continue operating? Press Y for Yes and N for No. Type O for a new calculation. ")

  while(more == "Y"):
    next_number = float(input("What is the next number?: "))
    what_operation = input("What operation do you wish to perform? Choose again out of the symbols: ")
    calculation = operations[what_operation]
    answer1 = calculation(answer,next_number)
    print(f"The calculation of {answer} {what_operation} {next_number} = {answer1}")
    answer = answer1
    more = input("Would you like to continue operating? Press Y for Yes and N for No. Type O for a new calculation. ")

  if(more == "O"):
    Calculating()

Calculating()
