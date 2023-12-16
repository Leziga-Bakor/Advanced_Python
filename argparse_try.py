import argparse

parser = argparse.ArgumentParser()

parser.add_argument('greeting', help = 'The greeting message display')

parser.add_argument('-n', '--numbers', type=float, nargs='*', help = 'The Numbers to be displayed')

parser.add_argument('-v', '--verbosity', type=int, choices=[0,1,2], help = 'Determines how much information is displayed')

args = parser.parse_args()

print(args)
print(args.greeting)
print(args.numbers)

if args.verbosity is None:
    print(args.greeting)
    if args.numbers is not None:
        print(sum(args.numbers))
else:
    if args.verbosity >= 0:
        print(args.greeting)
        if args.numbers is not None:
            print(sum(args.numbers))
    if args.verbosity >= 1:
        print(args.numbers)
    if args.verbosity == 2:
        print('Extra information')