from package1 import *
print(dir())
print(Tiger.sound())


# before defining __all__ variable
# ['__annotations__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__']


# after defining __all__ variable in __init__.py
# ['Lion', 'Tiger', '__annotations__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__']
