
from argparse import ArgumentParser

parser = ArgumentParser()
parser.print_help()
# usage: example.py [-h]
# 
# optional arguments:
#   -h, --help  show this help message and exit

print("\n ===================== \n")
parser.add_argument("pos1", help="positional argument 1")
parser.add_argument("-o", "--optional-arg", help="optional argument", dest="opt", default="default")

args = parser.parse_args()
print("positional arg:", args.pos1)
print("optional arg:", args.opt)


# execute "python argparse_example.py -h"

# usage: argparse_example.py [-h] [-o OPT] pos1

# positional arguments:
#   pos1                  positional argument 1

# optional arguments:
#   -h, --help            show this help message and exit
#   -o OPT, --optional-arg OPT
#                         optional argument
