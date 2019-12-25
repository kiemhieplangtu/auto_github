# 1. run: source ~/.my_commands.sh
# 2. then type create (the function below) on Terminal

# 3. Install github for Python:
#    pip install PyGithub

# 3. Install selenium for Python:
#    pip install selenium


import sys, os
# sys.path.insert(0, os.getenv("HOME")+'/Phd@MQ/projects/Dark') # add folder of Class

from github import Github



def create():
	'''
	Doc-block
	'''
	path     = os.getenv('HOME')+'/projects/'

	username = 'kiemhieplangtu'
	password = 'Hoanglaota08101988'

	folder   = str( sys.argv[1] )

	print('>> Creating directory: ' + folder)
	os.makedirs( path + folder )

	user = Github( username, password ).get_user()
	repo = user.create_repo( folder )

	print( 'Succesfully created repository %s' %(folder))


## --- MAIN --- ##
if __name__ == '__main__':
	create()