for num in range(0, 101):
    if num % 3 == 0 and num % 5 == 0:
        print(str(num) + ' ' + 'FizzBuzz')
    elif num % 3 == 0:
        print(str(num) + ' ' + 'Fizz')
    elif num % 5 == 0:
        print(str(num) + ' ' + 'Buzz')
