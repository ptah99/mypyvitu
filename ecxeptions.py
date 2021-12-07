# Errors and Exceptions
try:
    a = 5/0
    b = a + 4
except ZeroDivisionError as e:
    print(e)
except TypeError as e:
    print(e)
else:
    print("Everything is fine")
finally:
    print("cleaning up...")

# define our own error classes

class ValueTooHighError(Exception):
    pass
class ValueTooLowError(Exception):
    def __init__(self, message, value):
        self.message = message
        self.value = value

def test_value(x):
    if x > 100:
        raise ValueTooHighError('value is too high')
    if x < 5:
        raise ValueTooLowError("value is too small", x)

try:
    test_value(2)
except ValueTooHighError as e:
    print(e)
except ValueTooLowError as e:
    print(e.message, e.value)
    
