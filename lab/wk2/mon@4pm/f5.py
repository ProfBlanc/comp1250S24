# triple quotes or multi-line comment
"""
Ask the user for a temperature in Celsius
convert this temperature into Fahrenheit
"""

temp_in_celsius = float(input("Enter a temperature in Celsius: "))

temp_in_fahrenheit = (9/5 * temp_in_celsius) + 32
print(f"{temp_in_celsius} degrees C is {temp_in_fahrenheit} degrees F")
