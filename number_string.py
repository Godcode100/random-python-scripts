import math
def average(number_string):
    try:
        numbers = [float(n) for n in number_string.split()]
    except ValueError:
        total = math.nan
        values = 1
    else:
        total = sum(numbers)
        values = len(numbers)
    try:
        mean = total / values
    except ZeroDivisionError:
        mean = math.inf
    return mean
while True:
    number_string = input("Enter space delimited list of numbers \n")
    print (average(number_string))
    
