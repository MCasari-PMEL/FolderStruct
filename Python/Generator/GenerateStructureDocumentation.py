from tkinter import *
import os
from CopyTemplate import *

def GenerateSpaces(level):

    while(level > 0):
        sys.stdout.write('  ')
        level -= 1

def DOCU_Generate_Top_Folder(pathVal):
    print("+Documentation folder")
    tempPath = os.path.join(pathVal,'Documentation')
    os.makedirs(tempPath)
    return
def DOCU_Generate_ProjectReqs_Template(pathVal,tPath):
    print("-Project Requirements")
    COPY_ProjectRequirements(tPath,pathVal)

def DOCU_Generate_UserManual_Template(pathVal,tPath):
    print("-Project Requirements")
    COPY_UserManual(tPath,pathVal)

def DOCU_Generate_Deploymentnotes_Folder(pathVal):
    print("+Deployment Notes")
    tempPath = os.path.join(pathVal,'Deployment')
    os.makedirs(tempPath)
    return

def DOCU_Generate(docu,path,level,templatePath):
    #print("\n********************************************")
    #print("Generating Mooring System Files & Folders\n")
    #Gen Drawings
    if(docu.top.get() != 1):
        return
    if(docu.top.get()):
        GenerateSpaces(level)
        DOCU_Generate_Top_Folder(path)

    dPath = os.path.join(path,'Documentation')

    if(docu.projreqs.get()):
        GenerateSpaces(level+1)
        DOCU_Generate_ProjectReqs_Template(dPath,templatePath)
            
    if(docu.userman.get()):
        GenerateSpaces(level+1)
        DOCU_Generate_UserManual_Template(dPath,templatePath)

    if(docu.deploy.get()):
        GenerateSpaces(level+1)
        DOCU_Generate_Deploymentnotes_Folder(dPath)
