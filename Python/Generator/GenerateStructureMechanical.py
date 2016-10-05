from tkinter import *
import os

def GenerateSpaces(level):

    while(level > 0):
        sys.stdout.write('  ')
        level -= 1

def MECH_Generate_Top_Folder(pathVal):
    print("+Mechanical Folder")
    tempPath = os.path.join(pathVal,'Mechanical')
    os.makedirs(tempPath)
    return

def MECH_Generate_Assemblies_Folder(pathVal):
    print("+Assemblies Folder")
    tempPath = os.path.join(pathVal,'Assemblies')
    os.makedirs(tempPath)
    return

def MECH_Generate_Drawings_Folder(pathVal):
    print("+Drawings Folder")
    tempPath = os.path.join(pathVal,'Drawings')
    os.makedirs(tempPath)

def MECH_Generate(mech,pathVal,level,template):
    #print("\n********************************************")
    #print("Generating Mechanical System Files & Folders\n")

    if(mech.top.get() != 1):
        return
    GenerateSpaces(level)
    MECH_Generate_Top_Folder(pathVal)
    mPath = os.path.join(pathVal,'Mechanical')
    #Gen Drawings
    if(mech.assemblies.get()):
        GenerateSpaces(level+1)
        MECH_Generate_Assemblies_Folder(mPath)
        
    if(mech.drawings.get()):
        GenerateSpaces(level+1)
        MECH_Generate_Drawings_Folder(mPath)
