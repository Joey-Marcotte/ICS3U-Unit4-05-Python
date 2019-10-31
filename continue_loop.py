#!/usr/bin/env python3

# Created by: Joey Marcotte
# Created on: October 2019
# This program shows continue


def main():

    counter = 0
    total_number = 0
    # input
    amount_of_numbers = input("Enter the amount of numbers to add: ")
    try:
        amount_of_numbers_in_numbers = int(amount_of_numbers)
    except(ValueError):
        print("Not a valid Number")

    while counter < amount_of_numbers_in_numbers:
        number = input("Enter a number you would like to add: ")
        try:
            number_as_number = int(number)
            counter = counter + 1
            if number_as_number < 0:
                continue
            elif number_as_number >= 0:
                total_number = number_as_number + total_number
                continue

        except(ValueError):
            print("Not a valid number inputted")

    print("Sum of all posiive numbers = {0}".format(total_number))


if __name__ == "__main__":
    main()
