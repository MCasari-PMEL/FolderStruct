from tkinter import *
import os
from CopyTemplate import *

TemplatePath = []

def GenerateSpaces(level):

    while(level > 0):
        sys.stdout.write('  ')
        level -= 1

def TEST_Generate_Top_Folder(pathVal):
    print("+Test folder")
    tempPath = os.path.join(pathVal,'Tests')
    os.makedirs(tempPath)
    return

def TEST_Generate_Report_Template(pathVal,tPath):
    print("-Test Report Template")
    COPY_TestReport(tPath,pathVal)
    return

def TEST_Generate_Data_Folder(pathVal):
    print("+Data Folder")
    tempPath = os.path.join(pathVal,'Data')
    os.makedirs(tempPath)
    return

def TEST_Generate_Plan_Template(pathVal,tPath):
    print("-Test Plan Template")
    COPY_TestPlan(tPath,pathVal)


def TEST_Generate(test,path,level,templatePath):
    #print("\n********************************************")
    #print("Generating Mooring System Files & Folders\n")
    #Gen Drawings
    if(test.top.get() != 1):
        return

    
    
    GenerateSpaces(level)
    TEST_Generate_Top_Folder(path)
    tPath = os.path.join(path,'Tests')        

    if(test.report.get()):
        GenerateSpaces(level+1)
        TEST_Generate_Report_Template(tPath,templatePath)
        
    if(test.plan.get()):
        GenerateSpaces(level+1)
        TEST_Generate_Plan_Template(tPath,templatePath)
        
    if(test.data.get()):
        GenerateSpaces(level+1)
        TEST_Generate_Data_Folder(tPath)
        
    
