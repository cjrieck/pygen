#!/usr/bin/env python
import argparse

def check_input(inputString):

	if inputString == '':
		inputList = []
		
	elif inputString.find(',') != -1:
		inputList = inputString.split(',')
	else:
		inputList = inputString.split(' ')

	return inputList


def create_functions(fileName, function, delimiter=''):

	argumentString = raw_input("Enter argument(s) for "+function+': ')

	argumentList = check_input(argumentString)

	argumentString = ','.join(argumentList)
	
	fileName.write('def '+function+'('+argumentString+')'+':')

	returnString = raw_input("Enter return value(s) for "+function+': ')
	
	returnValueList = check_input(returnString)

	if returnValueList == []:
		fileName.write('\n\tpass # remove this and replace with the function body')
	else:
		returnString = ','.join(returnValueList)
		fileName.write('\n\t'+delimiter+'return '+returnString)

	fileName.write('\n\n')

def main():
	parser = argparse.ArgumentParser()
	parser.add_argument('file', help='name of the file you want to create')
	parser.add_argument('-i', '--imports', nargs='+', help='modules you want to import')
	parser.add_argument('-c', '--classes', nargs='+', help='names of classes you want to create')
	parser.add_argument('-f', '--functions', nargs='+', help='names of functions you want to create')


	args = parser.parse_args()

	fileName = ""
	if args.file:
		fileName = open(args.file+'.py', 'w')
		# fileName.close()

		if args.imports:
			pass

		if args.classes:

			for className in args.classes:
				fileName.write('class '+className+':')

				dataString = raw_input('Enter data to be stored in the class, '+className+': ')

				dataList = check_input(dataString)

				argumentDataList = []

				for arg in dataList:
					newArg = arg+'=None'
					argumentDataList.append(newArg)
					

				dataString = ','.join(argumentDataList)
				fileName.write('\n\tdef __init__('+dataString+'):')

				for arg in argumentDataList:
					fileName.write('\n\t\tself.'+arg.replace(' ', '').replace('=None', '')+' = '+arg.replace('=None', '').replace(' ', ''))

				fileName.write('\n\n')

				methodString = raw_input('Enter the methods of class, '+className+': ')

				# write methods to the class body

				methodList = check_input(methodString)

				for method in methodList:
					fileName.write('\t')
					create_functions(fileName, method, '\t')


		if args.functions:

			for function in args.functions:

				create_functions(fileName, function)

			fileName.write("def main():\n\tpass")
			fileName.write("\n\nif __name__ == '__main__':\n\tmain()")
		
		else:
			fileName.write("def main():\n\tpass")
			fileName.write("\n\nif __name__ == '__main__':\n\tmain()")
		
	fileName.close()

if __name__ == '__main__':
	main()
	