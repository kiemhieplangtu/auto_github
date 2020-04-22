# 1. run: source ~/.my_commands.sh
# 2. then type create (the function below) on Terminal

# 3. Install github for Python:
#    pip install PyGithub

# 3. Install selenium for Python:
#    pip install selenium


import sys, os
from   selenium                          import webdriver
from   selenium.webdriver.chrome.options import Options

from   webdriver_manager.chrome          import ChromeDriverManager



def remove():
	'''
	Doc-block
	'''


	path     = os.getenv('HOME')+'/projects/'

	username = 'nv-hiep'
	password = 'Hoanglaota08101988'

	repo     = str( sys.argv[1] )

	yn = input('Are you sure to remove repository "%s"? (yes/no):\n' %repo)
	yn = yn.lower().strip()
 
	if( yn not in ['yes', 'no'] ):
		print(f'You entered %s' %yn)
		print(f'Please enter "yes" or "no" !')
		sys.exit()

	if( yn == 'no' ):
		print(f'You entered "%s" -> nothing to do!' %yn)
		sys.exit()


	try:
		# Connect
		chrome_options = webdriver.ChromeOptions()
		chrome_options.add_argument("--incognito")
		global browser # this will prevent the browser variable from being garbage collected
		# browser = webdriver.Chrome(os.getenv('HOME')+'/program/chromedriver_linux64/chromedriver')
		browser = webdriver.Chrome(ChromeDriverManager().install())
		# browser.set_window_size(1800, 900)
		browser.get('https://github.com/login')
		# browser.find_element(By.NAME, 'username').send_keys('MYEMAIL', Keys.TAB, 'MYPW', Keys.ENTER)


		browser.find_elements_by_xpath("//input[@name='login']")[0].send_keys(username)
		browser.find_elements_by_xpath("//input[@name='password']")[0].send_keys(password)
		browser.find_elements_by_xpath("//input[@name='commit']")[0].click()
		browser.get('https://github.com/' + username + '/' + repo + '/settings')
		browser.find_elements_by_xpath(
			'//*[@id="options_bucket"]/div[@class="Box Box--danger"]/ul/li[4]/details/summary'
			)[0].click()
		browser.find_elements_by_xpath(
			'//*[@id="options_bucket"]/div[@class="Box Box--danger"]/ul/li[4]/details/details-dialog/div[@class="Box-body overflow-auto"]/form/p/input'
			)[0].send_keys( username + '/' + repo )
		browser.find_elements_by_xpath(
			'//*[@id="options_bucket"]/div[@class="Box Box--danger"]/ul/li[4]/details/details-dialog/div[@class="Box-body overflow-auto"]/form/button'
			)[0].click()
		#options_bucket > div.Box.Box--danger > ul > li:nth-child(4) > details > details-dialog > div.Box-body.overflow-auto > form > button
		browser.get("https://github.com/" + username)

		yn = input('Do you want to remove local folder "%s"? (yes/no):\n' %repo)
		yn = yn.lower().strip()

		while (yn not in ['yes', 'no']):
			print(f'You entered %s' %yn)
			print(f'Please enter "yes" or "no" !')
			yn = input()
			yn = yn.lower().strip()

		if( yn == 'no' ):
			print(f'You entered "%s" -> You keep the local folder!' %repo)
			sys.exit()

		os.system('rm -rf ' + path + repo)
		browser.close()

	except Exception as e:
		print (e, 'github')

	


## --- MAIN --- ##
if __name__ == '__main__':
	remove()