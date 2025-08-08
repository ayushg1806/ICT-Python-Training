#Convert temperature from Fahrenheit to Celsius and vice versa
temp = float(input('Enter temperature in Celsius: '))
tempFahrenheit = ((temp * 9)/5) + 32
print('Temperature in Fahrenheit:', tempFahrenheit)

tempFahrenheit = float(input('Enter temperature in Fahrenheit: '))
tempCelsius = ((tempFahrenheit - 32)*5)/9
print('Temperature in Celsius:', tempCelsius)