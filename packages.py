def check_package(package):
	"""
	Argument: Package to import
	Purpose:
		check if package can be Imported
	Return: True or False depending on if module could be imported or not
	"""
	try:
		__import__(package)
		return True
	except ImportError:
		return False

def install_package(package):
	"""
	Argument: Package to install
	Purpose:
		Installs packages/modules if User doesn't have it installed already
	Return: True or False depending on if package installed or not
	"""

	if os.getuid() == 0:
		command = 'sudo pip install '+package
	else:
		command = 'pip install '+package
	
	command = command.split(' ')
	event = Popen(command, shell=True, stdin=PIPE, stdout=PIPE)
	output = event.communicate()

	messageString = output[0]
	beginMessage = messageString.find('Could')
	endMessage = messageString[beginMessage:].find(package)+len(package)+beginMessage

	if output[0].find("Could not find") != -1:
		print WARNING+'Download/Install Error: '+ENDC+messageString[beginMessage:endMessage]
		return False
	else:
		return True