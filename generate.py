#!/usr/bin/env python

import argparse
import os
import sys
import glob
import subprocess 

from functions import create_functions
from inputs import check_input
from packages import check_root, check_pip, install_pip, check_package, install_package

"""
Color codes:
"""
RED = '\033[91m'
BLUE = '\033[94m'
CYAN = '\033[96m'
GREY = '\033[90m'

BOLD = '\033[1m'

WARNING = RED
MODULE = BLUE+BOLD
FUNCTION = GREY+BOLD
ENDC = '\033[0m'

def main():
	parser = argparse.ArgumentParser()
	parser.add_argument('file', default='pygenFile',help='name of the file you want to create')
	parser.add_argument('-p', '--path', nargs='?', default='./', help='destination path of the file')
	parser.add_argument('-i', '--imports', nargs='+', help='modules you want to import')
	parser.add_argument('-c', '--classes', nargs='+', help='names of classes you want to create')
	parser.add_argument('-f', '--functions', nargs='+', help='names of functions you want to create')
	
	parser.add_argument('-fw', '--framework', nargs='?', help='name of python framework')

	args = parser.parse_args()

	fileName = ""
	os.chdir(args.path)

	# begin implementing Framework app files generation
	if args.framework:

		check_root()

		if not check_pip():
			
			install_pip()

		print 'About to install modules'
		if install_package(args.framework):

			currDir = os.path.abspath(os.getcwd())
			os.chdir(os.path.dirname(os.path.abspath(__file__)))
			
			supported = False
			for supportedFW in os.listdir():
				if supportedFW.find(args.framework) != -1:
					supported = True
					break

			os.chdir(currDir)

			if supported:	
				subprocess.call('python '+os.path.dirname(os.path.abspath(__file__))+supportedFW) # get directory of generate script
				# pipe the current directory to the FrameWork generate file

			else:
				print 'Framework not supported at this time'
		else:
			print 'Error installing '+args.framework


	else:
		if args.file:
			
			filelist = glob.glob('./*.py')
			newfile = args.file+'.py'
			if any(newfile in s for s in filelist): 	#checks to see if file exists in a list of files in current directory
				print WARNING+BOLD+'Warning!'+ENDC+' About to overwrite '+BLUE+args.file+ENDC
			 	response = raw_input(CYAN+'Would you like to continue?'+ENDC+'[y/n] ')
			 	if response.lower() == 'n':
			 		sys.exit()
				else:
					os.remove(newfile)
	
			else:
			 	print 'Creating new file, '+BLUE+BOLD+newfile

			fileName = open(newfile, 'w')
			fileName.write("#!/usr/bin/env python\n\n")

			if args.imports:
				
				check_root()

				for module in args.imports:
					module = module.replace(',', '')

					moduleExists = check_package(module)
					
					if moduleExists:
						print 'Imported '+MODULE+module+ENDC
						fileName.write('import '+module+'\n')

					else:
						
						if args.path:
							pipExists = check_pip(args.path)
						else:
							pipExists = check_pip()

						if pipExists:
							couldInstall = install_package(module)
							
							if couldInstall:
								print 'Imported '+MODULE+module+ENDC
								fileName.write('import '+module+'\n')
							else:
								print WARNING+'ERROR:'+ENDC+' Module, '+MODULE+module+ENDC+', does not exist or could not be downloaded/installed. Did not write to file'
						
						else:
							
							install_pip()

							install_package(module)

							fileName.write('import '+module+'\n')


				fileName.write('\n')

			if args.classes:

				for className in args.classes:
					className = className[0].upper()+className[1:] # uppercase class name
					fileName.write('class '+className+':')

					dataString = raw_input('Enter data to be stored in the class, '+BLUE+BOLD+className+ENDC+': ')

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

					methodString = raw_input('Enter the methods of class, '+BLUE+BOLD+className+ENDC+': ')

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
		print 'Successfully created the file, '+CYAN+args.file+'.py'+ENDC

	# open file generated in default editor
	stderr = ""
	try:
		subprocess.call('open '+args.file+'.py', shell=True)
		returnCode = subprocess.check_output('open '+args.file+'.py', 
											 stderr=subprocess.STDOUT, 
											 shell=True)
		if returnCode < 0:
			print >>sys.stderr, "Child was terminated by signal", -returnCode
		else:
			print >>sys.stderr, "Child returned", returnCode
	except OSError, e:
		print >>sys.stderr, "Execution failed", e

if __name__ == '__main__':
	main()
	