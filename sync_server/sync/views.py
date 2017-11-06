from django.http import HttpResponse
#import os #For Linux
import subprocess #For windows
import time

def index(request, sec):
	time.sleep(float(sec))
	#os.system("python 'C:\Users\HP/ HOME\Desktop\Django-sync-server\python_sync\click.py'")  #For Linux
	subprocess.call(['python', 'C:\Users\HP HOME\Desktop\Django-sync-server\python_sync\click.py']) # For windows
	# if you are using a Linux based system, you need to install sox and libsox to use play
	#os.system("play C:\Users\HP HOME\Desktop\Django-sync-server\python_sync\aud.mp3")

	# if you are using Windows, use this
	#subprocess.call(['echo `a'])
	return HttpResponse("Hello, your request has been successfully executed.")