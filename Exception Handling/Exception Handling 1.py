#Handle ZeroDivisionError Exception
try:
    result = 10 / 0
except ZeroDivisionError as e:
    print(f"Error: {e}. We cannot divide by zero.")