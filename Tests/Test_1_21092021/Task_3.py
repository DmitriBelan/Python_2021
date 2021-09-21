while True:
    a = float(input('Please enter side "a": '))
    b = float(input('Please enter side "b": '))
    c = float(input('Please enter side "c": '))
    if a ** 2 + b ** 2 == c ** 2:
        print('Ok')
    else:
        print('Not OK')