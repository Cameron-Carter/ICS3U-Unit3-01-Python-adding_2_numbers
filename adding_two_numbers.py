#!/usr/bin/env python3

# Created by: Cameron Carter
# Created on April 2021
# This program adds two inputted numbers


def main():
    # This function adds two numbers
    print("This program adds two numbers.")

    # Input
    number_one = float(input("Enter the first number: "))
    number_two = float(input("Enter the second number: "))

    # Process
    total = number_one + number_two

    # Output
    print("\n{0} + {1} = {2}.".format(number_one, number_two, total))
    print("\nDone.")


if __name__ == "__main__":
    main()
