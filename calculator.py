from replit import clear
def add(n1,n2):
  return n1 + n2

def multiply(n1,n2):
  return n1 * n2

def devide(n1,n2):
  return n1 / n2

def subtract (n1,n2):
  return n1 - n2

operations = {
  "+":add,
  "-":subtract,
  "/":devide,
  "*":multiply
}
def calculator():
  num1 = float(input("Enter your first number: "))
  for key in operations:
    print(key)
  keep_calculating = True
  while keep_calculating:
    symbol = input("Pick an operational Symbol: ")

    num2 = float(input("Enter your number for calculation: "))

    cal_function = operations[symbol]
    answer = cal_function(num1,num2)
    print(f"{num1} {symbol} {num2} = {answer} ")

    ask_user = input(f"type 'y'if you want to keep  calculating number {answer} type 'e' to exit & type 'r' to restart the program ").lower()
    if ask_user == "y":
        keep_calculating = True
        num1 = answer
    elif ask_user == "r":
      keep_calculating = False
      clear()
      calculator()
    else:
      keep_calculating = False
      print("Good Bye!!!")

calculator()

      
