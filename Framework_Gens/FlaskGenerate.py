# Generate basic Flask app
import sys
import os
import subprocess

def write_flask(path, fileName):
	"""
	Arguments: path -> location to save app directory
			   fileName -> name of app index
	Purpose:
		Write the most basic Flask applicatiion w/
		directions on how to run
	Return:
	"""
	os.chdir(path)
	os.mkdir('Flask App')
	os.chdir('Flask App')

	flaskFile = open(fileName, 'w')

	flaskFile.write('# File created using pygen\n')
	flaskFile.write('# For more info on Flask go to http://flask.pocoo.org/\n')

	flaskFile.write('from flask import Flask\n')
	flaskFile.write('app = Flask(__name__)\n\n')

	flaskFile.write('@app.route("/")\n')
	flaskFile.write('def hello():\n')
	flaskFile.write('\treturn "Hello, World!"\n\n')

	flaskFile.write('if __name__ == "__main__:"\n')
	flaskFile.write('\t# in order to run, open your Terminal\n')
	flaskFile.write('\t# cd into the "Flask App" directory and\n')
	flaskFile.write('\t# type "python ' + fileName + '" and go to the outputted URL\n')
	flaskFile.write('\tapp.run()\n')

	flaskFile.close()

def main():
	path = sys.argv[1]
	fileName = sys.argv[2]
	write_flask(path, fileName)

	# open directory in Finder window
	subprocess.call('open .', shell=True)

if __name__ == '__main__':
	main()