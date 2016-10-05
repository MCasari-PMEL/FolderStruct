from tkinter import *
import os

def GenerateSpaces(level):

    while(level > 0):
        sys.stdout.write('  ')
        level -= 1

def PHOT_Generate_Top_Folder(pathVal):
    print("+Photo folder")
    tempPath = os.path.join(pathVal,'Photo')
    os.makedirs(tempPath)
    return


def PHOT_Generate(photo,pathVal,level):
    #print("\n********************************************")
    #print("Generating Mooring System Files & Folders\n")
    #Gen Drawings
    if(photo.top.get() != 1):
        return
   

    GenerateSpaces(level)
    PHOT_Generate_Top_Folder(pathVal)
    pPath = os.path.join(pathVal,'Photo')

        
