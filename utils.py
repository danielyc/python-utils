def error(msg='', ext=False):
	if len(str(msg)) == 0:
		print('[*] ERROR no error message specified')
		return None
	if exit:
		print('[*] ERROR ' + str(msg))
		exit()
	else:
		print('[*] ERROR ' + str(msg))
		

def secInput(msg=''):
	badchars = ['|','&',';','"',"'"]
	inp = input(msg)
	for i in badchars:
		if i in inp:
			error('Bad character detected', True)
			return None
	return inp
	

def isTool(tool):
	try:
		subprocess.call(tool, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	except OSError as a:
		if e.errno == os.errno.ENOENT:
			return False
	return True
	
	
def isService(service):
	if os.system('service ' + service + ' status > /dev/null 2>&1') == 1024:
		return False
	return True
	
					
if __name__ == '__main__':
	print('Checking library compatibility')
	imports =['sys','subprocess','os']
	for i in imports:
		try:
			exec('import ' + i)
		except ImportError:
			error('Could not import \'%s\'' %i, True)
	if sys.version_info[0] < 3:
		error('Must be running Python 3.x', True)
	
	print('Library is compatible')
	
