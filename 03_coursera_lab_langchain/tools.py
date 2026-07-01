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
    Calculate base raised to exponent.
    """
    return num1 * num2
    