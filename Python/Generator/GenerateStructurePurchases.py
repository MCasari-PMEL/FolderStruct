from tkinter import *
import os

def GenerateSpaces(level):

    while(level > 0):
        sys.stdout.write('  ')
        level -= 1

def PURC_Generate_Top_Folder(pathVal):
    print("+Purchases folder")
    tempPath = os.path.join(pathVal,'Purchases')
    os.makedirs(tempPath)
    return


def PURC_Generate(purc,path,level):
    #print("\n********************************************")
    #print("Generating Mooring System Files & Folders\n")
    #Gen Drawings
    if(purc.top.get() != 1):
        return
    
    GenerateSpaces(level)
    PURC_Generate_Top_Folder(path)


        
