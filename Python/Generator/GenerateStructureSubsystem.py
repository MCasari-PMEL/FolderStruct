from tkinter import *
from GenerateStructureElectrical import *
from GenerateStructureMechanical import *
from GenerateStructurePhotos import *
from GenerateStructureDocumentation import *
import os

def GenerateSpaces(level):

    while(level > 0):
        sys.stdout.write('  ')
        level -= 1

def SUBS_Generate_Top_Folder(pathVal):
    print("Subsystems")
    tempPath = os.path.join(pathVal,'Subsystems')
    os.makedirs(tempPath)
    return

def SUBS_Generate_Name_Folder(pathVal,name):
    print("+" + name + " Folder")
    tempPath = os.path.join(pathVal,name)
    os.makedirs(tempPath)
    return

def SUBS_Generate_BOM_Template(pathVal):
    print("-BOM Template")
    return

def SUBS_Generate_UserManual_Template(pathVal):
    print("-User Manual Template")
    return

def SUBS_Generate(subs,pathVal,level):
    if(subs.numsubs == 0):
        return
    GenerateSpaces(level)
    
    #Generate the top level folder
    SUBS_Generate_Top_Folder(pathVal)
    spath = os.path.join(pathVal,'Subsystems')
    for i in range(subs.numsubs):
        #Generate the subsystem name folder
        GenerateSpaces(level+1)
        SUBS_Generate_Name_Folder(spath,subs.name[i])
        #path = pathVal + '/Subsystems/' + subs.name[i]
        #tpath = os.path.join(pathVal,'Subsystems')
        path = os.path.join(spath,subs.name[i])

        #Generate the User Manual Template
        if(subs.userman.get()):
            GenerateSpaces(level+2)
            SUBS_Generate_UserManual_Template(path)

        #Generate the BOM Template
        if(subs.bom.get()):
            GenerateSpaces(level+2)
            SUBS_Generate_BOM_Template(path)
        
        #Generate the electrical folder
        #GenerateSpaces(level+1)
        ELEC_Generate(subs.elec,path,level+3)
        
        #Generate the mechanical folder
        #GenerateSpaces(level+1)
        MECH_Generate(subs.mech,path,level+3)
        
        #Generate the photo folder
        #GenerateSpaces(level+1)
        PHOT_Generate(subs.photos,path,level+3)
        
        #Generate the documentation folder
        #GenerateSpaces(level+1)
        DOCU_Generate(subs.docu,path,level+3)
    
        
    
