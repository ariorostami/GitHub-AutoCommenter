import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from pyautogui import press, typewrite, hotkey
from datetime import datetime
from datetime import timedelta
import time
#INSERT YOUR GITHUB USERNAME AND PASSWORD ON LINES 27 AND 30, AND IMPORT SELENIUM AND PYAUTOGUI BEFORE RUNNING
print("WARNING: change your computers power and sleep settings to not turn off or else this script may fail.\nYou can let the screen go to sleep though.\n")
print("==================================================\n")
print("What github commit would you like to comment on?\n")
#link to commit
value = input("Paste link to github commit link here: ")
#comment of form @autobot #cx
msg = input("\nWhat would you like your comment to be?")
howmany = input("\nAfter many hours would you like to wait before making your comment? (e.g 90 minutes = 1.5): ")
secs = 60*60*float(howmany)
target = datetime.now() + timedelta(hours=float(howmany)) 
#year month day format, based
bruh_time = target.strftime("%Y/%m/%d, %H:%M:%S")
print("======================================================================================")
print(f"Engaging forward thrusters and activating cryosleep.\nWe'll see you at {bruh_time}.\n")
time.sleep(5)
driver = webdriver.Chrome()
driver.get(value)
#TYPE YOUR USERNAME HERE
typewrite('YOUR-GITHUB-USERNAME-HERE')
press('tab')
#TYPE YOUR PASSWORD HERE
typewrite('YOUR-GITHUB-PASSWORD-HERE')
press('enter')
comment_box= driver.find_element_by_id('new_commit_comment_field')
comment_box.send_keys(msg)
time.sleep(secs)
button = driver.find_element_by_xpath("//*[@id='all_commit_comments']/div[3]/form/div/div/button")
print(f"task successfully accomplished at{datetime.now()}")
driver = None
print("I liek mudkipz")

button.click()
