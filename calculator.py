def add(num1,num2):
    print(num1 + num2)

def subtract(num1,num2):
    print(num1 - num2)

def multiply(num1,num2):
    print(num1 * num2)

def divide(num1,num2):
    print(num1 / num2)


first_number = int(input("Give me a number: "))
operator = input("Give me a math operator: ")
second_number = int(input("Give me another number: "))

if operator == "+":
    add(first_number,second_number)

if operator == "-":
    subtract(first_number,second_number)

if operator == "*":
    multiply(first_number,second_number)

if operator == "/":
    divide(first_number,second_number)

