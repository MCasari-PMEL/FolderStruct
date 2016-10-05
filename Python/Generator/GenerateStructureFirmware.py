from tkinter import *
import os

def GenerateSpaces(level):

    while(level > 0):
        sys.stdout.write('  ')
        level -= 1

def FIRM_Generate_Top_Folder(pathVal):
    print("+Firmware Folder")
    tempPath = os.path.join(pathVal,'Firmware')
    os.makedirs(tempPath)
    return

def FIRM_Generate_Firmware_Folder(pathVal):
    print("+Generating Firmware Folder")
    tempPath = os.path.join(pathVal,'Firmware')
    os.makedirs(tempPath)
    return

def FIRM_Generate_Firmware_API_Template(pathVal):
    print("-Generating Firmware API Template")
    
    return

def FIRM_Generate_Firmware_Binaries_Folder(pathVal):
    print("+Generating Binaries Folder")
    tempPath = os.path.join(pathVal,'Binaries')
    os.makedirs(tempPath)
    return

def FIRM_Generate_Firmware_Source_Folder(pathVal):
    print("+Generating Firmware Source Folder")
    tempPath = os.path.join(pathVal,'src')
    os.makedirs(tempPath)
    return

def FIRM_Generate_Firmware_Source_C_Template(pathVal):
    print("-Generating Firmware Source C Code Template")
    return

def FIRM_Generate_Firmware_Source_H_Template(pathVal):
    print("-Generating Firmware Source H Code Template")
    return

def FIRM_Generate(firm,pathVal,level):
    #print("\n********************************************")
    #print("Generating Mechanical System Files & Folders\n")

    if(firm.top.get() != 1):
        return
    GenerateSpaces(level)
    FIRM_Generate_Top_Folder(pathVal)
    fPath = os.path.join(pathVal,'Firmware')

    if(firm.api.get()):
        GenerateSpaces(level+2)
        FIRM_Generate_Firmware_API_Template(fPath)
    if(firm.binaries.get()):
        GenerateSpaces(level+2)
        FIRM_Generate_Firmware_Binaries_Folder(fPath)

    if(firm.source.get()):
        GenerateSpaces(level+2)
        FIRM_Generate_Firmware_Source_Folder(fPath)
        fsPath = os.path.join(fPath,'src')
        if(firm.source_c.get()):
            GenerateSpaces(level+3)
            FIRM_Generate_Firmware_Source_C_Template(fsPath)
        if(firm.source_h.get()):
            GenerateSpaces(level+3)
            FIRM_Generate_Firmware_Source_H_Template(fsPath)
        
