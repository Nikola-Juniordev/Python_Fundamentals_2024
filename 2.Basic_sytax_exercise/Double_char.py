while True:
    input_string = input()
    if input_string == 'End':
        break
    elif input_string == 'SoftUni':
        continue
    else:
        for letter in input_string:
            print(letter * 2, end="")
    print()

