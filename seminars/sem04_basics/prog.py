import sys
import argparse

parser = argparse.ArgumentParser()

parser.add_argument("--verbose", action="store_true")   # sets verbose True if present
parser.add_argument("--quiet", action="store_false", dest="verbose")  # flip

# append (collect repeated values)
parser.add_argument("-t", "--tag", action="append")
# usage: --tag a --tag b -> args.tag == ['a','b']

# count (counts occurrences)
parser.add_argument("-v", action="count", default=0)
# -vv -> verbose == 2

# store_const
parser.add_argument("--opt1", action="store_const", const=42, dest="value")
print(sys.argv)
args = parser.parse_args()
print(args)