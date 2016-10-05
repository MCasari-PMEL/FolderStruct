#!/usr/bin/python

"""
@author Matt Casari, matthew.casari@noaa.org
@date July 19th, 2016
@version 0.0.1
@copyright National Ocean and Atmospheric Administration
@copyright Pacific Marine Environmental Lab
@copyright Engineering Development Division
"""

import sys
import os
import shutil
import glob
import time
from os import path
from tkinter import *
import datetime
import CreateFolders
import FileTemplates

NUM_SUBSYSTEMS = 5
PROJECT_NAME = 'Proj1'

try:
        root = Tk()
        root.withdraw()
        pathname = simpledialog.askstring("Project Name", "Enter Project name")
#pathname = simpledialog.askstring('Project Name','Enter the Project Name')
except:
        print('Failed to create foldername')
                
#Find the current working directory
starting_path = os.getcwd()
template_path = os.path.join(starting_path,'Templates')
project_path = os.path.join(starting_path,pathname)
# template_path = starting_path + '/Templates/'
# project_path = starting_path + '/New Project'

#create a project directory if it doesn't exist
if not os.path.isdir(project_path):
	os.makedirs(project_path)
	
#change directory to project path
os.chdir(project_path)

#Generate All the Folders for the project
CreateFolders.GenerateAll(project_path,NUM_SUBSYSTEMS)

#Copy the file templates and adjust them to be project specific
FileTemplates.GenerateAll(template_path,project_path, NUM_SUBSYSTEMS)


print(os.getcwd())



os.chdir(starting_path)


