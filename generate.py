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

def create_functions(fileName, function, delimiter='', classMethod=False):

	argumentString = raw_input("Enter argument(s) for "+function+': ')

	argumentList = check_input(argumentString)

	argumentString = ','.join(argumentList)
	
	if classMethod == True:
		if argumentList == []:
			argumentString = 'self'
		else:
			argumentString = 'self,'+argumentString

	fileName.write('def '+function+'('+argumentString+')'+':')

	returnString = raw_input("Enter return value(s) for "+function+': ')
	
	returnValueList = check_input(returnString)

	if returnValueList == []:
		fileName.write('\n\t'+delimiter+'pass # remove this and replace with the function body')
	else:
		returnString = ','.join(returnValueList)
		fileName.write('\n\t'+delimiter+'return '+returnString)

	fileName.write('\n\n')

def check_package(package):
	try:
		import package
		return True
	except ImportError:
		return False

def install_package(package):
	from subprocess import Popen, PIPE, STDOUT
	command = 'pip install '+package
	event = Popen(command, shell=True, stdin=PIPE, stdout=PIPE, stderr=STDOUT)
	output = event.communicate()
	print output[0]



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
			
			# check for modules and install dependencies if necessary

			for module in args.imports:

				moduleExists = check_package(module)

				if moduleExists:
					fileName.write('import '+module+'\n')

				else:
					pipExists = check_package('pip')
					
					if pipExists:
						install_package(module)
						fileName.write('import '+module+'\n')

					else:
						# install pip first
						from subprocess import Popen, PIPE, STDOUT
						command = 'easy_install pip'
						event = Popen(command, shell=True, stdin=PIPE, stdout=PIPE, stderr=STDOUT)
						output = event.communicate()
						print output[0]

						install_package(module)

						fileName.write('import '+module+'\n')


			fileName.write('\n')

		if args.classes:

			for className in args.classes:
				fileName.write('class '+className+':')

				dataString = raw_input('Enter data to be stored in the class, '+className+': ')

				dataList = check_input(dataString)

				argumentDataList = ['self']

				for arg in dataList:
					newArg = arg+'=None'
					argumentDataList.append(newArg)
					

				dataString = ','.join(argumentDataList)
				fileName.write('\n\tdef __init__('+dataString+'):')

				for arg in argumentDataList[1:]:
					
					fileName.write('\n\t\tself.'+arg.replace(' ', '').replace('=None', '')+' = '+arg.replace('=None', '').replace(' ', ''))

				fileName.write('\n\n')

				methodString = raw_input('Enter the methods of class, '+className+': ')

				# write methods to the class body

				methodList = check_input(methodString)

				for method in methodList:
					fileName.write('\t')
					create_functions(fileName, method, '\t', True)


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
	