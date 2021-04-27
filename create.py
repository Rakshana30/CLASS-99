import os
import shutil
source = input("Enter your source folder")
destination = input("Enter your destination folder")
source = source+'/'
destination = destination+'/'
files = os.listdir(source)
for f in files:
    shutil.copy((source+f),destination) 
    