def check_input(inputString): # in classes as well
	"""
	Arguments: String of arguments from Terminal
	Purpose:
		Split string into a list for easier iteration
	Return: List of arguments as string
	"""
	if inputString == '':
		inputList = []
		
	elif inputString.find(',') != -1:
		inputList = inputString.split(',')
	else:
		inputList = inputString.split(' ')

	return inputList