#!/usr/bin/env python

import argparse

def main():
	parser = argparse.ArgumentParser()
	parser.add_argument('file', help='name of the file you want to create')
	parser.add_argument('-f', '--functions', nargs='+', help='names of functions you want to create')


	args = parser.parse_args()

	fileName = ""
	if args.file:
		fileName = open(args.file+'.py', 'w')
		# fileName.close()

	if args.functions:
		for function in args.functions:
			argumentString = raw_input("Enter argument(s) for "+function)
			if argumentString.find(',') != -1:
				argumentList = argumentString.split(',')
			else:
				argumentList = argumentString.split(' ')

			argumentList = str(tuple(argumentList))

			


if __name__ == '__main__':
	main()
	