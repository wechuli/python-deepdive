import sys
import argparse


parser = argparse.ArgumentParser(
    description='Calculates the div a//b and mode a%b of two integers')

parser.add_argument("a", help="first integer", type=int)
parser.add_argument("b", help="second integer", type=int)


args = parser.parse_args()

a = args.a
b = args.b

print(f'{a} // {b} = {a//b}, {a} % {b} = {a%b}')
