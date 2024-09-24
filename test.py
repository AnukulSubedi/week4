import example  # type: ignore # Import the module, which should match the module name in PYBIND11_MODULE

# Call the 'add' function from the module
result = example.add(5, 3)
print(f"Result of add(5, 3): {result}")
