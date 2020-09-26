import schedule 
import ctypes
import random
import time
import os

# path to the folder containing the images to be used as wallpapers
path = os.path.join(os.getcwd(), 'week-3/Subham_Patel/wallpapers')
# initializing the list of images
images=[]
# creating a list of all the images in the folder
files = os.listdir(path)
for file in files:
  # making sure that the file is an image
  if file.endswith(('.jpg', '.png', '.jpeg')):
    images.append(os.path.join(path, file))

# the relevant flag to be used in the SPIW function being initialized in it's integer form
SPI_SETDESKWALLPAPER = 20

def changeWallpaper():
  # using the random function to ensure that a random image is chosen each time this function gets executed.
  randomindex=random.randint(0,(len(images)-1))
  # now setting the randomly selected image as the desktop wallpaper using the ctypes module's windll api
  ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, images[randomindex], 0)

# every day at 22:00 time changeWallpaper() is called
schedule.every().day.at("22:00").do(changeWallpaper)

# this loop causes the script to run indefinitely
while True:
  # run all the jobs that are scheduled after every minute
  schedule.run_pending() 
  time.sleep(60) 
