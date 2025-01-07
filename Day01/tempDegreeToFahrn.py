# 2. Python program to convert the temperature in degree centigrade to Fahrenheit
# Formula
# Temperature in degrees Fahrenheit (°F) = (Temperature in degrees Celsius (°C) * 9/5) + 32.
# Temperature in degrees Celsius (°C) = (Temperature in degrees Fahrenheit (°F) - 32) * 5/9.

def temfahrenheit():
    try:
        inputtemdegrees = int(input("Enter Temprature value in degrees Celsius "))
        print("Temperature in degrees Celsius (°C) is ", inputtemdegrees)
        outtemfahrenheit = (inputtemdegrees * 9 / 5) + 32
        print("Temperature in degrees Fahrenheit (°F)", outtemfahrenheit)
    except ValueError:
        print("Please enter a valid numerical value.")


temfahrenheit()