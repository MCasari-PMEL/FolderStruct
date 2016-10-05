#!/usr/bin/python

"""
@author Matt Casari, matthew.casari@noaa.org
@date July 19th, 2016
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
ELEC_SD_TEMPLATE = 'ELEC_SystemDiagram_template.docx'
ELEC_WD_TEMPLATE = 'ELEC_WiringDiagram_template.docx'
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

def FTEM_ProjectRequirements(template_path,project_path):
	print("\r\nGenerating Project Requirement Templates...")
	
	# Generate System Reqs Doc for Project
	srcfile = os.path.join(template_path,PROJ_REQUIREMENTS_TEMPLATE)
	dstfolder = os.path.join(project_path,'Project Requirements')

	# Transfer the file
	if(os.path.isfile(srcfile)):
		_TransferFile(srcfile,dstfolder)
	else:
		print( file + ' does not exist')

	# Generate System Reqs Ammendments for Project
	srcfile = os.path.join(template_path,PROJ_AMMENDMENTS_TEMPLATE)
	dstfolder = os.path.join(project_path,'Project Requirements')

	# Transfer the file
	if(os.path.isfile(srcfile)):
		_TransferFile(srcfile,dstfolder)
	else:
		print( srcfile + ' does not exist')
	
def FTEM_Electrical(template_path,project_path, num_subsystems):
	print("\r\nGenerating Electrical Templates...")
	
	#generate System Diagram for System
	srcfile = os.path.join(template_path,ELEC_SD_TEMPLATE)
	dstfolder = os.path.join(project_path,'Electrical')
	
	#generate System Power Budget for System
	srcfile = os.path.join(template_path,ELEC_PB_TEMPLATE)
	dstfolder = os.path.join(project_path,'Electrical')
	
	#generate BOM for System
	srcfile = os.path.join(template_path,ELEC_BOM_TEMPLATE)
	dstfolder = os.path.join(project_path,'Electrical')
	
	# Transfer the file
	if(os.path.isfile(srcfile)):
		_TransferFile(srcfile,dstfolder)
	else:
		print( srcfile + ' does not exist')
	
	#put BOM templates in each SubSystem
	for i in range(1,num_subsystems):
		
		next_path = os.path.join(project_path,'Electrical')
		next_path = os.path.join(next_path,'Subsystems')
		next_path = os.path.join(next_path,'Subsystem_' + str(i))
		
		#Add BOM to SubSystem
		srcfile = os.path.join(template_path,ELEC_BOM_TEMPLATE)
		if(os.path.isfile(srcfile)):
			_TransferFile(srcfile,next_path)
		else:
			print( srcfile + ' does not exist')
		
		#Add Wiring Diagram to SubSystem
		srcfile = os.path.join(template_path,ELEC_WD_TEMPLATE)
		if(os.path.isfile(srcfile)):
			_TransferFile(srcfile,next_path)
		else:
			print( srcfile + ' does not exist')
			
		#Add Power Budget to SubSystem
		srcfile = os.path.join(template_path,ELEC_PB_TEMPLATE)
		if(os.path.isfile(srcfile)):
			_TransferFile(srcfile,next_path)
		else:
			print( srcfile + ' does not exist')
		
		#Add Interface Document to SubSystem
		srcfile = os.path.join(template_path,ELEC_INTERFACE_TEMPLATE)
		if(os.path.isfile(srcfile)):
			_TransferFile(srcfile,next_path)
		else:
			print( srcfile + ' does not exist')
			
		#Add User Manual Document to SubSystem
		srcfile = os.path.join(template_path,ELEC_USERMAN_TEMPLATE)
		if(os.path.isfile(srcfile)):
			_TransferFile(srcfile,next_path)
		else:
			print( srcfile + ' does not exist')
	#

def FTEM_Firmware(template_path,project_path):
	print( "\r\nGenerating Firmware Templates...")
	
	# Generate System Reqs Doc for Project
	srcfile = os.path.join(template_path,FIRM_README_TEMPLATE)
	dstfolder = os.path.join(project_path,'Firmware')

	# Transfer the file
	if(os.path.isfile(srcfile)):
		_TransferFile(srcfile,dstfolder)
	else:
		print( srcfile + ' does not exist')
	
def FTEM_Software(template_path,project_path):
	print( "\r\nGenerating Software Templates...")
	
	# Generate System Reqs Doc for Project
	srcfile = os.path.join(template_path,SOFT_README_TEMPLATE)
	dstfolder = os.path.join(project_path,'Software')

	# Transfer the file
	if(os.path.isfile(srcfile)):
		_TransferFile(srcfile,dstfolder)
	else:
		print( srcfile + ' does not exist')
	
def FTEM_Mechanical(template_path,project_path):
	print( "\r\nGenerating Mechanical Templates...")
	
	# Generate System Reqs Doc for Project
	srcfile = os.path.join(template_path,MECH_BOM_TEMPLATE)
	dstfolder = os.path.join(project_path,'Mechanical')

	# Transfer the file
	if(os.path.isfile(srcfile)):
		_TransferFile(srcfile,dstfolder)
	else:
		print( srcfile + ' does not exist')
	
def FTEM_Documentation(template_path,project_path):
	print( "\r\nGenerating Documentation Templates...")
	
	# Generate System Reqs Doc for Project
	srcfile = os.path.join(template_path,DOCU_USERMAN_TEMPLATE)
	dstfolder = os.path.join(project_path,'Documentation')

	# Transfer the file
	if(os.path.isfile(srcfile)):
		_TransferFile(srcfile,dstfolder)
	else:
		print( srcfile + ' does not exist')
	
	
def FTEM_Testing(template_path,project_path):
	print( "\r\nGenerating Testing Templates...")
	
	# Generate System Reqs Doc for Project
	srcfile = os.path.join(template_path,TEST_PLAN_TEMPLATE)
	dstfolder = os.path.join(project_path,'Testing')

	# Transfer the file
	if(os.path.isfile(srcfile)):
		_TransferFile(srcfile,dstfolder)
	else:
		print( srcfile + ' does not exist')
		
	# Generate Test Report for Project
	srcfile = os.path.join(template_path,TEST_REPORT_TEMPLATE)
	dstfolder = os.path.join(project_path,'Testing')

	# Transfer the file
	if(os.path.isfile(srcfile)):
		_TransferFile(srcfile,dstfolder)
	else:
		print( srcfile + ' does not exist')
		
def FTEM_AddManual(template_path,destination_path,filename):
	print( '\r\nAdding: ' + filename + ' to: ' + destination_path)
	
	srcfile = os.path.join(template_path,filename)

	# Transfer the file
	if(os.path.isfile(srcfile)):
		_TransferFile(srcfile,destination_path)
	else:
		print( srcfile + ' does not exist')
	
def FTEM_GenerateAll(template_path,project_path,num_subsystems):
	#Project
	ProjectRequirements(template_path,project_path)
	
	#Electrical 
	Electrical(template_path,project_path,num_subsystems)
	
	#Firmware
	Firmware(template_path,project_path)
	
	#Software
	Software(template_path,project_path)
	
	#Mechanical
	Mechanical(template_path,project_path)
	
	#Documentation
	Documentation(template_path,project_path)
	
	#Testing
	Testing(template_path,project_path)
	
	
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
	
		
		
