import ctypes

# Loading the shared library
lib = ctypes.CDLL('./libexample.so')  

# Defining argument types and return types for the functions
lib.add.argtypes = [ctypes.c_int, ctypes.c_int]
lib.add.restype = ctypes.c_int

lib.multiply.argtypes = [ctypes.c_int, ctypes.c_int]
lib.multiply.restype = ctypes.c_int

lib.print_message.argtypes = []
lib.print_message.restype = None

# Calling the functions
result_add = lib.add(5, 3)
result_multiply = lib.multiply(5, 3)

print("Result of add(5, 3):", result_add)
print("Result of multiply(5, 3):", result_multiply)

lib.print_message()

