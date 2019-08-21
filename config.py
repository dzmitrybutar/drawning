import argparse
import os

BASEDIR = os.path.abspath(os.path.dirname(__file__))

parser = argparse.ArgumentParser(description='Drawing')
parser.add_argument('infile', type=str, help='Input filename and dir for initial conditions')
parser.add_argument('outfile', type=str, help='Output filename and dir for the result')
args = parser.parse_args()

infile_path = BASEDIR + '/' + args.infile
outfile_path = BASEDIR + '/' + args.outfile
