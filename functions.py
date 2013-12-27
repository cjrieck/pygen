from inputs import check_input

GREY = '\033[90m'
BOLD = '\033[1m'
FUNCTION = GREY+BOLD
ENDC = '\033[0m'

def create_functions(fileName, function, delimiter='', classMethod=False):
	"""
	Arguments: file to write to, function to write, add extra delimeter if class method, boolean for class method or not
	Purpose:
		writes the functions/method to the file
		will add arguments and return values to functions/methods
	Return: N/A
	"""

	argumentString = raw_input("Enter argument(s) for "+FUNCTION+function+ENDC+': ')

	argumentList = check_input(argumentString)

	argumentString = ','.join(argumentList)
	
	if classMethod == True:
		if argumentList == []:
			argumentString = 'self'
		else:
			argumentString = 'self,'+argumentString

	fileName.write('def '+function+'('+argumentString+')'+':')

	returnString = raw_input("Enter return value(s) for "+FUNCTION+function+ENDC+': ')
	
	returnValueList = check_input(returnString)

	if returnValueList == []:
		fileName.write('\n\t'+delimiter+'pass # remove this and replace with the function body')
	else:
		
		if not classMethod:
			returnString = ','.join(returnValueList)
			fileName.write('\n\t'+delimiter+'return '+returnString)
		else:
			classReturnValueList = []
			
			for value in returnValueList:
				# value = 'self.'+value.replace(' ','')
				value = value.replace(' ','')
				classReturnValueList.append(value)
			
			returnString = ','.join(classReturnValueList)
			fileName.write('\n\t'+delimiter+'return '+returnString)

	fileName.write('\n\n')