# ESSRG @ IIIT-D Sync Server
Server for syncing multiple softwares across multiple platforms

## Dependencies:
* Python 2.7
* Django (use [this link](https://www.codingforentrepreneurs.com/blog/install-python-django-on-windows/) for installing in windows)
* pyautogui
* sox/libsox

## How to get it running:
* Go to "python_sync" folder and execute "autogui.py" ($ python autogui.py)
⋅⋅⋅ Move your mouse pointer around and note the x and y coordinates of the place that you want the click to happen. 
* Open click.py and change the x and y coordinates to the values from previous step 
* Go to the "sync_server/sync" folder and open "views.py"
⋅⋅⋅ Update the path to click.py.
* Use ipconfig (windows) or ifconfig (Linux) to get your IP address
* Open "sync_server/sync_server/settings.py" and add your IP address to the list of allowed hosts in line 28.
* Go back to the "sync_server" folder and execute "python manage.py runserver <Your IP Address>:<Port>"