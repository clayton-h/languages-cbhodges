import inspect


class ReflectionExample:
    # A sample method to be inspected
    def example_method(self):
        print("\nMethod is called.")


# Create an instance of ReflectionExample
obj = ReflectionExample()

# Get the list of all attributes and methods of the class
attributes = dir(obj)
print("\nAll attributes and methods of ReflectionExample: ", attributes)

# Inspect and print only the methods of the class
methods = inspect.getmembers(ReflectionExample, predicate=inspect.isfunction)
print("\nMethods of the class are: ")
for method in methods:
    print(method[0])

# Invoke a method by its name
method_name = 'example_method'
getattr(obj, method_name)()
