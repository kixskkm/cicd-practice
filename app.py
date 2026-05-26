from calc import add, subtract
from converter import km_to_mile, celsius_to_fahrenheit

def calc_and_convert(a, b):
    result = add(a, b)
    distance = km_to_mile(result)
    return distance

def temp_pipeline(celsius):
    result = subtract(celsius, 0)
    return celsius_to_fahrenheit(result)