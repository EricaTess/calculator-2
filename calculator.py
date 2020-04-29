"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )


# Replace this with your code
while True:
    input_string = input("Enter your equation > ")
    tokens = input_string.split(' ')
    if tokens == 'q':
        break
    elif tokens[0] == 'pow':
        print(power(int(tokens[1]), int(tokens[2])))
