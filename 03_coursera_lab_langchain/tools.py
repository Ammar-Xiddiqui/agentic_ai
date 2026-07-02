from langchain.tools import tool


@tool
def calculate_power(base: int, exponent: int) -> int:
    """
    Calculate base raised to exponent.
    """
    return base ** exponent


@tool
def multiply(num1: int, num2: int) -> int:
    """
    multiply two integer and give result 
    """
    return num1 * num2



@tool
def add(num1: int, num2: int) -> int:
    """
    add two integer and give result 
    """
    return num1 + num2



@tool
def subtract(num1: int, num2: int) -> int:
    """
    subtarct two integer and give result 
    """
    return num1 - num2


@tool
def divide(num1: int, num2: int) -> float:
    """
    divide two integer and give result 
    """
    return num1/num2



@tool
def modulus(num1: int, num2: int) -> int:
    """
    divide two integer and give result 
    """
    return num1%num2