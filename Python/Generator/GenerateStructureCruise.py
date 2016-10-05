from tkinter import *
import os

def GenerateSpaces(level):

    while(level > 0):
        sys.stdout.write('  ')
        level -= 1

def CRUI_Generate_Top_Folder(pathVal):
    print("+Cruise folder")
    tempPath = os.path.join(pathVal,'Cruise')
    os.makedirs(tempPath)
    return

def CRUI_Generate_Report_Template(pathVal):
    print("-Report Template")
    return

def CRUI_Generate_Data_Folder(pathVal):
    print("+Data Folder")
    tempPath = os.path.join(pathVal,'Data')
    os.makedirs(tempPath)
    return

def CRUI_Generate(cruise,pathVal,level):
    #print("\n********************************************")
    #print("Generating Mooring System Files & Folders\n")
    #Gen Drawings
    if(cruise.top.get() != 1):
        return
    
    GenerateSpaces(level)
    CRUI_Generate_Top_Folder(pathVal)
    cPath = os.path.join(pathVal,'Cruise')
    if(cruise.report.get()):
        GenerateSpaces(level+1)
        CRUI_Generate_Report_Template(cPath)

    if(cruise.data.get()):
        GenerateSpaces(level+1)
        CRUI_Generate_Data_Folder(cPath)
            
        
        
