import argparse

parser = argparse.ArgumentParser()

parser.add_argument('greeting', help = 'The greeting message display')

parser.add_argument('-n', '--numbers', type=float, nargs='*', help = 'The Numbers to be displayed')

args = parser.parse_args()

print(args)
print(args.greeting)
print(args.numbers)

if args.numbers is not None:
    print(sum(args.numbers))