from tkinter import *

def ELEC_Generate_File_BOM(pathVal):
    print("Generating BOM Template")
    return

def ELEC_Generate_WD_Sub(pathVal):
    print("Generating Wiring Diagram  Folder")
    return

def ELEC_Generate_Schem_Sub(pathVal):

    return

def ELEC_Generate_Firmware_Sub(pathVal):

    return




def ELEC_Generate(elec,pathVal):

    if(elec.top.get() != 1):
        return
    if(elec.bom.get()):
        ELEC_Generate_File_BOM(pathVal)

    
    ##ELEC_Generate_WD_Sub(path)
    ##ELEC_Generate_Schem_Sub(path)
    ##ELEC_Generate_Firmwar_Sub(path)

    return



