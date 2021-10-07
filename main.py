import webbrowser
import schedule
import time
from datetime import date
from datetime import datetime

# Zoom Auto Join 
# Version 2.0
# Uses webbroser.open instead of pyautogui clicks (faster and more reliable!)
# Get your Zoom link while in the Zoom meeting


# Auto-Join function:

def zoomClass(link):

	webbrowser.open(link)

# Information:

class Cours:

	def __init__(self, name, id, password, link):
		self.name = name
		self.id = id
		self.password = password
		self.link = link

	def info(self):
		print(" ")
		print(" ")
		print(self.name, "at", zoom_time)
		print(self.id)
		print(self.password)

maths = Cours("Mathematics:", "99101666123", "202995", "https://zoom.us/j/99101666123?pwd=a23oi7cn585c2982395") # EXAMPLE COURSE ZOOM (insert course name, zoom id, zoom password, zoom link)

# Schedule:

if date.today().weekday() == 0:	# Monday

	zoom_time = "13:00" # TIME OF MEETING
	maths.info() # DISPLAYS INFO
	schedule.every().monday.at("%s"%zoom_time).do(zoomClass, maths.link) #every().tuesday


if date.today().weekday() == 1:	# Tuesday

	zoom_time = "08:00"
	maths.info()
	schedule.every().tuesday.at("%s"%zoom_time).do(zoomClass, maths.link) #every().tuesday 


if date.today().weekday() == 2:	# Wednesday



if date.today().weekday() == 3:	# Thursday



if date.today().weekday() == 4:	# Friday



if date.today().weekday() == 5 or date.today().weekday() == 6: # Weekend
	exit()

now = datetime.now()
finalHour = now.replace(hour=17, minute=0, second=0, microsecond=0) # MARKS END OF THE DAY (closes the program)

if now > finalHour:
	exit()

while True:
	schedule.run_pending()
	time.sleep(1)
