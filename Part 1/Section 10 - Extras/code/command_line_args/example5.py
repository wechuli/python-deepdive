import sys

#  --last-name Value --first-name Jon

print(sys.argv[1:])

keys = sys.argv[1::2]
values = sys.argv[2::2]

print(keys)
print(values)


args = {k: v for k, v in zip(keys, values)}

print(args)


first_name: str = args.get('--first-name', None)
last_name: str = args.get('--last-name', None)
yob: int = int(args.get('--yob', None))

print(first_name, last_name, yob)
