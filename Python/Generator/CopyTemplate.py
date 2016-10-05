#!/usr/bin/python

"""
@author Matt Casari, matthew.casari@noaa.org
@date October 5, 2016
@version 0.0.1
@copyright National Ocean and Atmospheric Administration
@copyright Pacific Marine Environmental Lab
@copyright Engineering Development Division
"""
import sys
import os
import time
import shutil

PROJ_REQUIREMENTS_TEMPLATE = 'PROJ_SystemRequirements_template.docx'
PROJ_AMMENDMENTS_TEMPLATE = 'PROJ_Ammendments_template.docx'

ELEC_BOM_TEMPLATE = 'ELEC_BOM_template.xlsx'
ELEC_SCHEM_TEMPLATE = 'ELEC_Schematic_template.sch'
ELEC_SD_TEMPLATE = 'ELEC_SystemDiagram_template.docx'
ELEC_WD_TEMPLATE = 'WiringDiagram.vsdx'
ELEC_PB_TEMPLATE = 'ELEC_PowerBudget_template.xlsx'
ELEC_INTERFACE_TEMPLATE = 'ELEC_Interface_template.docx'
ELEC_USERMAN_TEMPLATE = 'ELEC_UserManual_template.docx'

FIRM_README_TEMPLATE = 'README_template.txt'

SOFT_README_TEMPLATE = 'README_template.txt'
SOFT_USERMAN_TEMPLATE = 'SOFT_UserManual_template.docx'

MECH_BOM_TEMPLATE = 'MECH_BOM_template.xlsx'

DOCU_USERMAN_TEMPLATE = 'DOCU_UserManual_template.docx'
DOCU_INTERFACE_TEMPLATE = 'DOCU_Interface_template.docx'
DOCU_SYSDIAGRAM_TEMPLATE = 'DOCU_SystemDiagram_template.docx'

TEST_PLAN_TEMPLATE = 'TEST_Plan_template.docx'
TEST_REPORT_TEMPLATE = 'TEST_Report_template.docx'

def COPY_ConvertToFileFormat(templatePath,destFolder,filename):
    #Generate the test plan file
    srcfile = os.path.join(templatePath,filename)
    
    #Transfer the file
    if(os.path.isfile(srcfile)):
        _TransferFile(srcfile,destFolder)
    else:
        print(srcfile + 'does not exist')
    return



def COPY_ProjectRequirements(templatePath,destFolder):
    COPY_ConvertToFileFormat(templatePath,destFolder,PROJ_REQUIREMENTS_TEMPLATE)
    return

def COPY_Electrical_Interface(templatePath,destFolder):
    COPY_ConvertToFileFormat(templatePath,destFolder,ELEC_INTERFACE_TEMPLATE)
    return

def COPY_Electrical_PowerBudget(templatePath,destFolder):
    return

def COPY_ElectricalBOM(templatePath,destFolder):
    COPY_ConvertToFileFormat(templatePath,destFolder,ELEC_BOM_TEMPLATE)
        
    return
def COPY_UserManual(templatePath,destFolder):
    COPY_ConvertToFileFormat(templatePath,destFolder,ELEC_USERMAN_TEMPLATE)
    return

def COPY_TestPlan(templatePath,destFolder):
    COPY_ConvertToFileFormat(templatePath,destFolder,TEST_PLAN_TEMPLATE)
    return

def COPY_TestReport(templatePath,destFolder):
    COPY_ConvertToFileFormat(templatePath,destFolder,TEST_REPORT_TEMPLATE)
    return

def COPY_WiringDiagram(templatePath,destFolder):
    COPY_ConvertToFileFormat(templatePath,destFolder,ELEC_WD_TEMPLATE)
    return

def COPY_Schematic(templatePath,destFolder):
    COPY_ConvertToFileFormat(templatePath,destFolder,ELEC_SCHEM_TEMPLATE)
    return

def _TransferFile(srcfile,dstfolder):
	#find the file name and extenstion type
	file_name = srcfile[srcfile.rindex('\\')+1:]
	file_ext = file_name[file_name.find('.'):]
	
	#remove the _template from file name
	if file_name.find('_template') > 0:
		file_name = file_name[:file_name.find('_template')]
	else:
		file_name = file_name[:file_name.find('.')]
		
	#remove leading identifier (XXXX_) if there is one
	if file_name.find('_') == 4:
		file_name = file_name[5:]
		
	
	#Add the extension back to the Name with V1.0
	file_name += '_v1.0' + file_ext
	

	#Create the destination file name + path
	dstfile = os.path.join(dstfolder,file_name)
	
	#check to see if the file already exists.  Archive the old if yes, then delete the existing
	if os.path.isfile(dstfile):
		_Archive(dstfolder, file_name)
		os.remove(dstfile)
		
	#Copy new file to folder
	shutil.copyfile(srcfile,dstfile)


		
def _Archive(folder_path,filename):
	arch_path = os.path.join(folder_path,'Archive')
	
	# Create an Archive folder if it doesn't exist
	if not os.path.isdir(arch_path):
		os.makedirs(arch_path)
		
	file_ext = filename[filename.rindex('.'):]

	
	
	file_name = filename[:filename.rindex('.')]
	
	#If Previous Archives Exist, rename them to +1 of index
	#delete #999 if exists
	if os.path.isfile(os.path.join(arch_path,file_name) + '_BUP999' + file_ext):
		os.remove(os.path.join(arch_path,file_name) + '_BUP999' + file_ext)
		
		
	for i in range(998,0,-1):
		curr_file = os.path.join(arch_path,file_name)+'_BUP'+str(i) + file_ext
		next_file = os.path.join(arch_path,file_name)+'_BUP'+str(i + 1) + file_ext
		# print curr_file
		# print next_file
		# print '\\r\\n'
		if os.path.isfile(curr_file):
			shutil.copyfile(curr_file,next_file)
			os.remove(curr_file)
			
	
	#Save the latest archive
	save_file = os.path.join(arch_path,file_name) + '_BUP1' + file_ext
	shutil.copyfile(os.path.join(folder_path,filename),os.path.join(arch_path,save_file))
