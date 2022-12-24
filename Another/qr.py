# Python calculator program

# function to add two numbers 
def add(num1, num2):
  return num1 + num2

# function to subtract two numbers 
def subtract(num1, num2):
  return num1 - num2

# function to multiply two numbers
def multiply(num1, num2):
  return num1 * num2

# function to divide two numbers
def divide(num1, num2):
  return num1 / num2

print("Welcome to the Python calculator!")

# ask the user to enter the first number
num1 = float(input("Enter the first number: "))

# ask the user to enter the second number
num2 = float(input("Enter the second number: "))

# ask the user to enter the operation they would like to perform
print("Enter the operation you would like to perform:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

# store the user's choice in a variable
choice = int(input("Enter your choice (1/2/3/4): "))

if choice == 1:
  result = add(num1, num2)
elif choice == 2:
  result = subtract(num1, num2)
elif choice == 3:
  result = multiply(num1, num2)
elif choice == 4:
  result = divide(num1, num2)
else:
  print("Invalid input. Please try again.")

# print the result of the operation
print(f"The result is: {result}")
