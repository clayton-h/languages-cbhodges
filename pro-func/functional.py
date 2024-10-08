#c for calculator
#Author: Clayton H.
#functional code (immutable - functions)

def add(x, y):
	return (x + y)

def sub(x, y):
	return (x - y)

def div(x, y):
	return (x / y)

def mult(x, y):
	return (x * y)

#higher-order function
def operation(op, x, y):
	return op(x, y)

operations = {
    'add': add,
    'subtract': sub,
    'multiply': mult,
    'divide': div
}

def main():
	while True:
		print("\ncalculator:")
		print("add for addition")
		print("sub for subtraction")
		print("div for division")
		print("mult for multiplication\n")

		choice = input(": ")

		if choice in operations:
			x = float(input("enter first number: "))
			y = float(input("enter second number: "))

			result = operation(operations[choice], x, y)
			print(result)

if __name__ == "__main__":
    main()