import argparse
import time

parser = argparse.ArgumentParser()

parser.add_argument('greeting', help = 'The greeting message display')
parser.add_argument('-n', '--numbers', type=float, nargs='*', help = 'The Numbers to be displayed')
parser.add_argument('-v', '--verbosity', type=int, choices=[0,1,2], help = 'Determines how much information is displayed')
# parser.add_argument('-f', '--file', type=str)
parser.add_argument('--debug', action='store_true', help='Enables debug mode')

args = parser.parse_args()

if args.debug:
    start = time.perf_counter()

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

if args.debug:
    end = time.perf_counter()
    print(end -start)