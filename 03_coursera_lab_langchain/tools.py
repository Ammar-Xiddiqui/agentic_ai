import re

def calculate_power(input_text):
    numbers = re.findall(r"-?\d+\.?\d*", input_text)

    if len(numbers) < 2:
        return {"error": "Need base and exponent"}

    base = float(numbers[0])
    exponent = float(numbers[1])

    return {
        "base": base,
        "exponent": exponent,
        "result": base ** exponent
    }