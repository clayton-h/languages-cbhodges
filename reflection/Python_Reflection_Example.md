
# Python Reflection Example

Reflection in Python can be accomplished using built-in functions like `dir()` and the `inspect` module.

## Class Definition
A simple class `ReflectionExample` is defined with one method `example_method()`.

## Reflection Usage
- `dir(obj)`: List all attributes and methods of an instance `obj`.
- `inspect.getmembers(ReflectionExample, predicate=inspect.isfunction)`: Get all methods of the class.
- `getattr(obj, method_name)()`: Invoke a method by its name on an instance `obj`.

## Example Code
```python
import inspect

class ReflectionExample:
    def example_method(self):
        print("Method is called.")

obj = ReflectionExample()
attributes = dir(obj)
methods = inspect.getmembers(ReflectionExample, predicate=inspect.isfunction)

for method in methods:
    print(method[0])

method_name = 'example_method'
getattr(obj, method_name)()
```

This markdown file provides a concise overview of the reflection capabilities in Python using a simple class example.
