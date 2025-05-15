def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

# Executing code with taking i/p from user:
celsius_temp = float(input("Enter temperature in Celsius scale: "))
fahrenheit_temp = celsius_to_fahrenheit(celsius_temp)
print(f"{celsius_temp}°C is equal to {fahrenheit_temp}°F")
