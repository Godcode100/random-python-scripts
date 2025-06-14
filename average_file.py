def average_file(path):
    file = open(path, 'r')
    try:
        numbers = [float[n] for n in file.readlines()]
    except ValueError as e:
        raise ValueError("Non numeric arguments found") from e
    else:
        try:
             return average = sum(numbers) / len(numbers)
        except ZeroDivisionError as e:
            raise ValueError ("cant divide by zero") from e
    finally:
        print("Closing File")
        file.close()
