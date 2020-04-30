import argparse

parser = argparse.ArgumentParser(description="testing defaults and flags")

parser.add_argument('--monty', action='store_const',
                    const='Python')  # constant value
parser.add_argument('-n', '--name', default='John')  # default values


parser.add_argument('-v', '--verbose', action='store_const',
                    const=True, default=False)  # flags

parser.add_argument('-v2', action='store_const', const=True)


parser.add_argument('-q', '--quiet', action='store_false')
args = parser.parse_args()
print(args)
