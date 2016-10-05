"""
@author Matt Casari, matthew.casari@noaa.gov
@date October 4, 2016
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
import datetime
import CreateFolders
import FileTemplates
from tkinter import *
from FS import *
from SubSys import *
from GenerateStructure import *

from TemplatePath import *
#from FS_class import *

try:
    root = Tk()
    root.withdraw()
    pathname = simpledialog.askstring("Project Name","Enter Project Name")
    root.destroy()
except:
    pathname = "Project"

    
#Setup the working directories
root = Tk()
root.withdraw()
#starting_path = filedialog.askdirectory()

starting_path = "C:/Users/Casari/Desktop/Sandbox/TESTING"
root.destroy()
#template_path = os.path.join(starting_path,'Templates')
project_path = os.path.join(starting_path,pathname)



#Determine which files/folders to include
fs = FileStructure()
mainloop()

#if there are subsystems requested, query files/folders to include
if(fs.numsubs > 0):
    ss = SubSystem(fs.numsubs)
    mainloop()

print('+'+pathname)
#Create the Project Directory
os.makedirs(project_path)

#Generate all Electrical Folders & Files
ELEC_Generate(fs.elec,project_path,1,template_path)

#Generate all Mechanical Folders & Files
MECH_Generate(fs.mech,project_path,1,template_path)

#Generate all Firmware Folders & Files
MOOR_Generate(fs.moor,project_path,1)

#Generate all Mooring Folders & Files
#FIRM_Generate(fs.firm,project_path,0)

#Generate all Test Folders & Files
TEST_Generate(fs.test,project_path,1,template_path)

#Generate all Photo Folders
PHOT_Generate(fs.photos,project_path,1)

#Generate all Cruise Folders & Files
CRUI_Generate(fs.cruise,project_path,1)

#Generate all Documentation Folders & Files
DOCU_Generate(fs.docu,project_path,1,template_path)

#Generate all Purchases Folders & Files
PURC_Generate(fs.purc,project_path,1)

#Generate all Subsystems
if(fs.numsubs > 0):
    SUBS_Generate(ss,project_path,1,template_path)


#print(templatePath)
