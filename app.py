# app.py - Simple calculator app

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

def power(base, exponent):
    return base ** exponent

if __name__ == "__main__":
    print("Simple Calculator")
    print(f"2 + 3 = {add(2, 3)}")
    print(f"10 - 4 = {subtract(10, 4)}")
    print(f"5 * 6 = {multiply(5, 6)}")
    print(f"20 / 4 = {divide(20, 4)}")
    print(f"2 ^ 3 = {power(2, 3)}")
