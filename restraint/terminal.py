import argparse
import datetime

from restraint.main import Restraint
from restraint import io

parser = argparse.ArgumentParser(
    description='Restrain yourself from doing something more than X times per Y days/weeks/months/years')
subparsers = parser.add_subparsers(dest='action')

test_parser = subparsers.add_parser(
    'test',
    description='Given the log of performing this activity, test to see if you can do it',
)
test_parser.add_argument(
    dest='file',
    metavar='FILE',
    type=argparse.FileType('r'),
    default="activity.log",
    help='a file containing each day you performed the something, where each line is in the date format: "YYYY/MM/DD". (default: "activity.log")')
test_parser.add_argument(
    dest='times',
    metavar='X',
    type=int,
    help='the maximum number of TIMES you want to be able to do this something per Y days/weeks/months/years')
test_parser.add_argument(
    dest='units',
    metavar='Y',
    default=1,
    type=int,
    nargs='?',
    help='the multiple of days/weeks/months/years you wish to use as the time period (default: 1)')
test_parser.add_argument(
    dest='unit',
    metavar='TIME_UNIT',
    choices=Restraint.UNIT_CONVERSION.keys(),
    help='the basic unit of time')

mark_parser = subparsers.add_parser(
    'mark',
    description='Add a date to the log file (default: today)')
mark_parser.add_argument(
    dest='file',
    metavar='FILE',
    type=argparse.FileType('a'),
    default="activity.log",
    help='a file containing each day you performed the something, where each line is in the date format: "YYYY/MM/DD". (default: "activity.log")')
def date(s):
    try:
        datetime.datetime.strptime(
            s,
            io.PlaintextPutter.DATE_FORMAT)
        return s
    except a:
        raise argparse.ArgumentTypeError("Date must be in format YYYY/MM/DD")
mark_parser.add_argument(
    'date',
    default=datetime.datetime.today().strftime(
        io.PlaintextPutter.DATE_FORMAT),
    type=date,
    nargs='?',
    help="a date to add to the log (default: today)")
 
args = parser.parse_args()

if args.action == 'mark':
    Restraint.mark(args.file, args.date)
elif args.action == 'test':
    if Restraint.test(args.file, args.times, args.units, args.unit):
        print("Do it")
    else:
        print("Don't do it")
else:
    parser.print_help()
