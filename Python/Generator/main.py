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

starting_path = "C:"
root.destroy()
template_path = os.path.join(starting_path,'Templates')
project_path = os.path.join(starting_path,pathname)



#Determine which files/folders to include
fs = FileStructure()
mainloop()

#if there are subsystems requested, query files/folders to include
if(fs.numsubs > 0):
    ss = SubSystem(fs.numsubs)
    mainloop()

#Generate all Electrical Folders & Files
ELEC_Generate(fs.elec,project_path)

#Generate all Mechanical Folders & Files


#Generate all Firmware Folders & Files

#Generate all Mooring Folders & Files

#Generate all Test Folders & Files

#Generate all Documentation Folders & Files

#Generate all Photo Folders

#Generate all Cruise Folders & Files

#Generate all Purchases Folders & Files
