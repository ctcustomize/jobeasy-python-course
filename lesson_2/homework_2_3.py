# Write your first program. Enter the temperature right now in Fahrenheit in temperature_fahrenheit variable as
# a string (e.g. '75') and convert it to Celsius.
# !important you should save only number to result_temperature. Formula (32°F − 32) × 5/9 = 0°C

# temperature_fahrenheit = 75
# temperature_celsius = int((temperature_fahrenheit - 32 )*5/9)
# result_temperature = print(temperature_celsius)


temperature_fahrenheit = int(input('What is a temperature right now?;'))
result_temperature = int(temperature_fahrenheit - 32) * 5 / 9
print(f'In Celsius it will be: {result_temperature}')