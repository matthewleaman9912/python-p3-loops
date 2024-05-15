#!/usr/bin/env python3

def happy_new_year():
    i = 10
    while i > 0:
        print(i)
        i -= 1
    print("Happy New Year!")

def square_integers(int_list):
    square_list = [num * num for num in int_list]
    return square_list

def fizzbuzz():
    for i in range(101):
        if i > 0:
            if i % 5 == 0 and i % 3 == 0:
                print("FizzBuzz")
            elif i % 5 == 0:
                print("Buzz")
            elif i % 3 == 0:
                print("Fizz")
            else:
                print(i)
