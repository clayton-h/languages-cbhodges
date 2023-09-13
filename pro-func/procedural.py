#c for calculator
#Author: Clayton H.
#procedural code (mutable - steps)

result = 0

def add(x, y):
	return (x + y)

def sub(x, y):
	return (x - y)

def div(x, y):
	return (x / y)

def mult(x, y):
	return (x * y)

def main():
	print("\ncalculator:")
	print("1 for addition")
	print("2 for subtraction")
	print("3 for division")
	print("4 for multiplication\n")

	choice = input("enter (1/2/3/4): ")
	num1 = float(input("enter first number: "))
	num2 = float(input("enter second number: "))

	if(choice == "1"):
		result = add(num1, num2)
		print(f"{num1} + {num2} = {result}")
	elif(choice == '2'):
		result = sub(num1, num2)
		print(f"{num1} - {num2} = {result}")
	elif(choice == '3'):
		result = div(num1, num2)
		print(f"{num1} / {num2} = {result}")
	elif(choice == '4'):
		result = mult(num1, num2)
		print(f"{num1} * {num2} = {result}")

if __name__ == "__main__":
    main()