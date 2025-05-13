#!/usr/bin/python3
""" FizzBuzz
"""
import sys


def fizzbuzz(n):
    """
    FizzBuzz function prints numbers from 1 to n separated by a space.

    - For multiples of three print "Fizz" instead of the number.
    - For multiples of five print "Buzz".
    - For numbers which are multiples of both three and five, print "FizzBuzz".
    """
    if n < 1:
        return

    tmp_result = []
    for i in range(1, n + 1):
        # Changes made:  must check for multiples of 3 and 5 first,
        # Before, the condition i % 3 == 0 came before
        # i % 3 == 0 and i % 5 == 0, so we never met the final case
        # This caused numbers like 15 or 30 to be incorrectly labeled "Fizz"
        # instead of "FizzBuzz"
        if (i % 3 == 0 and i % 5 == 0):
            tmp_result.append("FizzBuzz")
        elif (i % 3) == 0:
            tmp_result.append("Fizz")
        elif (i % 5) == 0:
            tmp_result.append("Buzz")
        else:
            tmp_result.append(str(i))
    print(" ".join(tmp_result))


if __name__ == '__main__':
    if len(sys.argv) <= 1:
        print("Missing number")
        print("Usage: ./0-fizzbuzz.py <number>")
        print("Example: ./0-fizzbuzz.py 89")
        sys.exit(1)

    # Convert argument to integer
    number = int(sys.argv[1])
    fizzbuzz(number)
