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

def ProjectRequirements(project_path):
	# next_path = project_path + '/Project Requirements'
	next_path = os.path.join(project_path,'Project Requirements')
	if not os.path.isdir(next_path):
		os.makedirs(next_path)

def Electrical(project_path, num_subsystems):
	
	# next_path = project_path + '/Electrical'
	next_path = os.path.join(project_path,'Electrical')
	if not os.path.isdir(next_path):
		os.makedirs(next_path)
		
	# next_path = project_path + '/Electrical/System Diagrams'
	next_path = os.path.join(project_path,'Electrical')
	next_path = os.path.join(next_path,'System Diagrams')
	if not os.path.isdir(next_path):
		os.makedirs(next_path)

	# next_path = project_path + '/Electrical/Wiring Diagrams'
	next_path = os.path.join(project_path,'Electrical')
	next_path = os.path.join(next_path,'Wiring Diagrams')
	if not os.path.isdir(next_path):
		os.makedirs(next_path)

	for i in range(1,num_subsystems+1):
		# next_path = project_path + '/Electrical/Subsystems/Subsystem_' + str(i)
		next_path = os.path.join(project_path,'Electrical')
		next_path = os.path.join(next_path,'Subsystems')
		next_path = os.path.join(next_path,'Subsystem_' + str(i))
		if not os.path.isdir(next_path):
			os.makedirs(next_path)
		
		# next_path = project_path + '/Electrical/Subsystems/Subsystem_' + str(i) + '/Datasheets'
		next_path = os.path.join(project_path,'Electrical')
		next_path = os.path.join(next_path,'Subsystems')
		next_path = os.path.join(next_path,'Subsystem_' + str(i))
		next_path = os.path.join(next_path,'Datasheets')
		if not os.path.isdir(next_path):
			os.makedirs(next_path)
			
def Firmware(project_path):
	# next_path = project_path + '/Firmware'
	next_path = os.path.join(project_path,'Firmware')
	if not os.path.isdir(next_path):
		os.makedirs(next_path)
		
def Software(project_path):
	# next_path = project_path + '/Software'
	next_path = os.path.join(project_path,'Firmware')
	if not os.path.isdir(next_path):
		os.makedirs(next_path)
	
	# next_path = project_path + '/Software/User Interface'
	next_path = os.path.join(project_path,'Software')
	next_path = os.path.join(next_path,'User Interface')
	if not os.path.isdir(next_path):
		os.makedirs(next_path)
		
def Mechanical(project_path):
	# next_path = project_path + '/Mechanical'
	next_path = os.path.join(project_path,'Mechanical')
	if not os.path.isdir(next_path):
		os.makedirs(next_path)
		
	# next_path = project_path + '/Mechanical/Drawing Package'
	next_path = os.path.join(project_path,'Mechanical')
	next_path = os.path.join(next_path,'Drawing Package')
	if not os.path.isdir(next_path):
		os.makedirs(next_path)
		
def Documentation(project_path):
	# next_path = project_path + '/Documentation'
	next_path = os.path.join(project_path,'Documentation')
	if not os.path.isdir(next_path):
		os.makedirs(next_path)
		
def Testing(project_path):
	# next_path = project_path + '/Testing'
	next_path = os.path.join(project_path,'Testing')
	if not os.path.isdir(next_path):
		os.makedirs(next_path)

	# next_path = project_path + '/Testing/Test Data'
	next_path = os.path.join(project_path,'Testing')
	next_path = os.path.join(next_path,'Test Data')
	if not os.path.isdir(next_path):
		os.makedirs(next_path)	
		
		
def GenerateAll(project_path,num_subsystems):
	ProjectRequirements(project_path)
	Electrical(project_path,num_subsystems)
	Firmware(project_path)
	Software(project_path)
	Mechanical(project_path)
	Documentation(project_path)
	Testing(project_path)
