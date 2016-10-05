from tkinter import *
import os

def GenerateSpaces(level):

    while(level > 0):
        sys.stdout.write('  ')
        level -= 1

def MOOR_Generate_Top_Folder(pathVal):
    print("+Mooring folder")
    tempPath = os.path.join(pathVal,'Mooring')
    os.makedirs(tempPath)
    return

def MOOR_Generate_Bathymetry_Folder(pathVal):
    print("+Bathymetry Folder")
    tempPath = os.path.join(pathVal,'Bathymetry')
    os.makedirs(tempPath)
    return

def MOOR_Generate_Diagrams_Folder(pathVal):
    print("+Diagrams Folder")
    tempPath = os.path.join(pathVal,'Diagrams')
    os.makedirs(tempPath)
    return

def MOOR_Generate(moor,path,level):
    #print("\n********************************************")
    #print("Generating Mooring System Files & Folders\n")
    #Gen Drawings
    if(moor.top.get()!= 1):
        return
    
    GenerateSpaces(level)
    MOOR_Generate_Top_Folder(path)
    mPath = os.path.join(path,'Mooring')
    if(moor.bath.get()):
        GenerateSpaces(level+1)
        MOOR_Generate_Bathymetry_Folder(mPath)
        
    if(moor.diag.get()):
        GenerateSpaces(level+1)
        MOOR_Generate_Diagrams_Folder(mPath)
        
