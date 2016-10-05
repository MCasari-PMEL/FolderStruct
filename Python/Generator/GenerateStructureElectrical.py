from tkinter import *
from GenerateStructureFirmware import *
import os
from CopyTemplate import *

def GenerateSpaces(level):

    while(level > 0):
        sys.stdout.write('  ')
        level -= 1

def ELEC_Generate_Top_Folder(pathVal):
    print("+Electrical Folder")
    tempPath = os.path.join(pathVal,'Electrical')
    os.makedirs(tempPath)
    return

def ELEC_Generate_BOM_Template(pathVal,tPath):
    print("-BOM Template")
    COPY_ElectricalBOM(tPath,pathVal)
    return

def ELEC_Generate_UserManual_Template(pathVal,tPath):
    COPY_UserManual(tPath,pathVal)
    print("-User Manual Template")
    return

def ELEC_Generate_Powerbudget_Template(pathVal,tPath):
    print("-Powerbudget Template")
    COPY_Electrical_PowerBudget(tPath,pathVal)

def ELEC_Generate_WD_Sub(pathVal):
    print("+Wiring Diagram Folder")
    tempPath = os.path.join(pathVal,'WiringDiagrams')
    os.makedirs(tempPath)
    return

def ELEC_Generate_WD_Template(pathVal,tPath):
    print("-Wiring Diagram Template")
    COPY_WiringDiagram(tPath,pathVal)
    return

def ELEC_Generate_Schem_Sub(pathVal):
    print("+Schematic Folder")
    tempPath = os.path.join(pathVal,'Schematics')
    os.makedirs(tempPath)
    return

def ELEC_Generate_Schem_Template(pathVal,tPath):
    print("-Schematic Template")
    COPY_Schematic(tPath,pathVal)
    return

def ELEC_Generate_Photo_Folder(pathVal):
    print("+Photo Folder")
    tempPath = os.path.join(pathVal,'Photos')
    os.makedirs(tempPath)
    return

def ELEC_Generate_Datasheet_Folder(pathVal):
    print("+Datasheet Folder")
    tempPath = os.path.join(pathVal,'Datasheets')
    os.makedirs(tempPath)
    return

def ELEC_Generate_InterfaceDocument_Template(pathVal,tPath):
    print("-Interface Document Template")
    return

def ELEC_Generate_Firmware_Folder(pathVal):
    print("+Firmware Folder")
    tempPath = os.path.join(pathVal,'Firmware')
    os.makedirs(tempPath)
    return

def ELEC_Generate_Firmware_API_Template(pathVal,tPath):
    print("-Firmware API Template")
    return

def ELEC_Generate_Firmware_Binaries_Folder(pathVal):
    print("+Binaries Folder")
    tempPath = os.path.join(pathVal,'Binaries')
    os.makedirs(tempPath)
    return

def ELEC_Generate_Firmware_Source_Folder(pathVal):
    print("+Firmware Source Folder")
    tempPath = os.path.join(pathVal,'src')
    os.makedirs(tempPath)
    return

def ELEC_Generate_Firmware_Source_C_Template(pathVal,tPath):
    print("-Firmware Source C Code Template")
    return

def ELEC_Generate_Firmware_Source_H_Template(pathVal,tPath):
    print("-Firmware Source H Code Template")
    return






def ELEC_Generate(elec,pathVal,level,template):
    #print("\n********************************************")
    #print("Generating Electrical System Files & Folders\n")
    if(elec.top.get() != 1):
        return
    GenerateSpaces(level)
    ELEC_Generate_Top_Folder(pathVal)
    ePath = os.path.join(pathVal,'Electrical')
    if(elec.bom.get()):
        GenerateSpaces(level+1)
        ELEC_Generate_BOM_Template(ePath,template)
        
    if(elec.interfacedoc.get()):
        GenerateSpaces(level+1)
        ELEC_Generate_InterfaceDocument_Template(ePath,template)
        
##    if(elec.userman.get()):
##        GenerateSpaces(level+1)
##        ELEC_Generate_UserManual_Template(ePath,template)

    if(elec.powerbudget.get()):
        GenerateSpaces(level+1)
        ELEC_Generate_Powerbudget_Template(ePath,template)

    if(elec.wd.get()):
        GenerateSpaces(level+1)
        ELEC_Generate_WD_Sub(ePath)
        wPath = os.path.join(ePath,'WiringDiagrams')
        if(elec.wd_template.get()):
            GenerateSpaces(level+2)
            ELEC_Generate_WD_Template(wPath,template)

    if(elec.schem_path.get()):
        GenerateSpaces(level+1)
        ELEC_Generate_Schem_Sub(ePath)
        wPath = os.path.join(ePath,'Schematics')
        if(elec.schem_template.get()):
            GenerateSpaces(level+2)
            ELEC_Generate_Schem_Template(pathVal,template)
            
    if(elec.photos.get()):
        GenerateSpaces(level+1)
        ELEC_Generate_Photo_Folder(ePath)

    if(elec.datasheets.get()):
        GenerateSpaces(level+1)
        ELEC_Generate_Datasheet_Folder(ePath)
    
    if(elec.firm.top.get()):
        GenerateSpaces(level+1)
        FIRM_Generate(elec.firm,ePath,level+1)
##        ELEC_Generate_Firmware_Folder(ePath)
##        fPath = os.path.join(ePath,'Firmware')
##        if(elec.firm.api.get()):
##            GenerateSpaces(level+2)
##            ELEC_Generate_Firmware_API_Template(fPath)
##        if(elec.firm.binaries.get()):
##            GenerateSpaces(level+2)
##            ELEC_Generate_Firmware_Binaries_Folder(fPath)
##
##        if(elec.firm.source.get()):
##            GenerateSpaces(level+2)
##            ELEC_Generate_Firmware_Source_Folder(fPath)
##            fsPath = os.path.join(fPath,'src')
##            if(elec.firm.source_c.get()):
##                GenerateSpaces(level+3)
##                ELEC_Generate_Firmware_Source_C_Template(fsPath)
##            if(elec.firm.source_h.get()):
##                GenerateSpaces(level+3)
##                ELEC_Generate_Firmware_Source_H_Template(fsPath)

    
    return



