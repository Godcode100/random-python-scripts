number = None
while number is None:
    try:
        raw = input(" Enter a number or 't' to quit:\n")
        if raw == 't':
            print("Quitting Program")
            break
        number == int(raw)
    except ValueError:
        print("You didnot enter a number")
else:
    print(f"You entered {number}")

