# def celsius_to_fahrenheit(temperature: float) -> float:
#     """Converts a temperature in Celsius degrees to Fahrenheit degrees"""
#     pass

# def fahrenheit_to_celsius(temperature: float) -> float:
#     """Converts a temperature in Fahrenheit degrees to Celsius degrees"""
#     pass

# def meters_to_imperial(value: float) -> str:
#     """Converts a value in meters to a string value using imperial units"""
#     pass

# def inches_to_imperial(value: int) -> str:
#     """Converts a value in inches to a string value using imperial units"""
#     pass

# if __name__ == "__main__":
#     meters = float(input("Please enter a value in meters: "))
#     converted = meters_to_imperial(meters)
#     print("In imperial units:", converted)

#     inches = int(input("Please enter a value in inches: "))
#     converted = inches_to_imperial(meters)
#     print("In imperial units:", converted)

def celsius_to_fahrenheit(temperature: float) -> float:
    """Converts a temperature in Celsius degrees to Fahrenheit degrees"""
    return temperature * 9 / 5 + 32

def fahrenheit_to_celsius(temperature: float) -> float:
    """Converts a temperature in Fahrenheit degrees to Celsius degrees"""
    return (temperature - 32) * 5 / 9

def meters_to_imperial(value: float) -> str:
    """Converts a value in meters to a string value using imperial units"""
    inches = value / 0.0254
    feet = int(inches // 12)
    inches = int(inches % 12)
    yards = int(feet // 3)
    feet = int(feet % 3)
    miles = int(yards // 1760)
    yards = int(yards % 1760)

    result = ""
    if miles > 0:
        result += f"{miles} miles "
    if yards > 0:
        result += f"{yards} yards "
    if feet > 0:
        result += f"{feet} feet "
    if inches > 0:
        result += f"{inches} inches "
    return result.strip()

def inches_to_imperial(value: int) -> str:
    """Converts a value in inches to a string value using imperial units"""
    feet = value // 12
    inches = value % 12
    yards = feet // 3
    feet = feet % 3
    miles = yards // 1760
    yards = yards % 1760

    result = ""
    if miles > 0:
        result += f"{miles} miles "
    if yards > 0:
        result += f"{yards} yards "
    if feet > 0:
        result += f"{feet} feet "
    if inches > 0:
        result += f"{inches} inches "
    return result.strip()