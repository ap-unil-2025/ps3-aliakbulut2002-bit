"""
Problem 2: Temperature Converter
Convert between Celsius and Fahrenheit temperatures.
"""

def celsius_to_fahrenheit(celsius):
    Fahrenheit=(celsius* 9/5) +32
    return Fahrenheit
    


def fahrenheit_to_celsius(fahrenheit):
    celsius= (fahrenheit -32) * 5/9
    return celsius


def temperature_converter():
    x = int(input("température ? "))
    current_unit = input("Current unit (C/F): ")
    if current_unit == "C":
        return round(celsius_to_fahrenheit(x), 2)
    else:
        return round(fahrenheit_to_celsius(x), 2)

   
    print("Temperature Converter")
    print("-" * 30)

   


# Test cases (DO NOT MODIFY)
if __name__ == "__main__":
    # Test conversions
    print("Running tests...")

    # Test Celsius to Fahrenheit
    assert celsius_to_fahrenheit(0) == 32, "0°C should be 32°F"
    assert celsius_to_fahrenheit(100) == 212, "100°C should be 212°F"

    # Test Fahrenheit to Celsius
    assert fahrenheit_to_celsius(32) == 0, "32°F should be 0°C"
    assert fahrenheit_to_celsius(212) == 100, "212°F should be 100°C"

    print("All tests passed!")
    print()

    # Run interactive converter
    print(temperature_converter())