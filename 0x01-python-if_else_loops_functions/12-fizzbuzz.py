#!/usr/bin/python3

def fizzbuzz():
    for i in range(1, 101):
        response = ''
        if i % 5 == 0 and i % 3 == 0:
            response = 'FizzBuzz'
        elif i % 3 == 0:
            response = 'Fizz'
        elif i % 5 == 0:
            response = 'Buzz'
        else:
            response = str(i)
        print("{} ".format(response), end='')
