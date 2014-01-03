import os
from subprocess import call, check_output, STDOUT
from pkgutil import iter_modules
from sys import exit

RED = '\033[91m'
CYAN = '\033[96m'
BOLD = '\033[1m'
WARNING = RED
ENDC = '\033[0m'

def check_root():
	if os.getuid() != 0: # check for root user
		print WARNING+BOLD+'Warning: Not root user!'+ENDC+' Some dependencies may not install.'
		response = raw_input(CYAN+'Continue?'+ENDC+'[y/n]: ')
		
		if response.lower() == 'n':
			sys.exit()

def check_pip(path=None):
	if path != "./":
		currDir = path
	else:
		currDir = os.path.abspath(os.getcwd())
		
	os.chdir('/usr/local/bin/')
	packageList = os.listdir('./')

	if 'pip' in packageList:
		pipExists = True
	else:
		pipExists = False

	os.chdir(currDir)
	
	return pipExists

def install_pip():
	command = 'easy_install pip'
							
	call(command, shell=True)
	err = check_output(command, 
				 	   stderr=STDOUT, 
				 	   shell=True)

def check_package(package):
	"""
	Argument: Package to import
	Purpose:
		check if package can be Imported
	Return: True or False depending on if module is in list of preinstalled modules
	"""
	
	moduleList = [mod[1] for mod in iter_modules()]

	if package in moduleList:
		# del moduleList
		return True
	else:
		# del moduleList
		return False

def install_package(package):
	"""
	Argument: Package to install
	Purpose:
		Installs packages/modules if User doesn't have it installed already
	Return: True or False depending on if package installed or not
	"""

	command = 'pip install ' + package

	call(command, shell=True)
	err = check_output(command, 
					   stderr=STDOUT, 
					   shell=True)
	# print "ERROR FROM INSTALL PACKAGE: "+err
	
	if err.find('Requirement already satisfied') == -1:
		print WARNING+'Download/Install Error: '+ENDC #+messageString[beginMessage:endMessage]
		return False
	else:
		return True