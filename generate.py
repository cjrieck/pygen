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

			argumentString = raw_input("Enter argument(s) for "+function+': ')

			if argumentString == '':
				argumentList = []
			elif argumentString.find(',') != -1:
				argumentList = argumentString.split(',')
				print argumentList
			else:
				argumentList = argumentString.split(' ')
			# argumentList = str(tuple(argumentList))
			argumentString = ','.join(argumentList)

			fileName.write('def '+function+'('+argumentString+')'+':')

			returnString = raw_input("Enter return value(s) for "+function+': ')
			
			if returnString == '':
				returnValueList = []
			elif returnString.find(',') != -1:
				returnValueList = returnString.split(',')
			else:
				returnValueList = returnString.split(' ')
			
			if returnValueList == []:
				fileName.write('\n\tpass # remove this and replace with the function body')
			else:
				returnString = ','.join(returnValueList)
				fileName.write('\n\treturn '+returnString)

			fileName.write('\n\n')

		fileName.write("def main():\n\tpass")
		fileName.write("\n\nif __name__ == '__main__':\n\tmain()")

		fileName.close()

if __name__ == '__main__':
	main()
	