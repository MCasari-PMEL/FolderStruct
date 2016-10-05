from tkinter import *
from FS_classes import *

class Grid:
    def __init__(self):
        self.val = 0
    def add(self,num=0):
        self.val += (1+num)
        return self.val
    def current(self):
        return self.val

#Subsystem Subclass
class SubSystem:
    def __init__(self,numsubs):
        self.grid = Grid()
        
        self.master = Tk()

        self.header1()
        self.split()
        #self.top = IntVar()
        self.name_entry = []
        self.name = []
        #
        self.numsubs = numsubs
        for i in range(0,numsubs):
            Label(self.master,text="Subsystem #" + str(i+1)).grid(row=self.grid.add())
            self.name_entry.append(self.addSubsytemName(1,self.grid.current(),i))
            self.name.append(0)
            self.grid.add()
        #self.name_entry = self.addSubsytemName(0)


        self.split()
        self.header2()
        self.split()
        #self.name = 0

        #self.top = self.addPathWithCommand("Subsystem",0,self.toggle)
        
        self.userman = self.addFile("User Manual",0)
        self.bom = self.addFile("BOM.csv",0)
        
        self.elec = Elec()
        self.addElectrical(self.elec,0)
        
        self.mech = Mech()
        self.addMechanical(self.mech,0)

        self.photos = Photos()
        self.addPhotos(self.photos,0)

        self.docu = Docu()
        self.addDocumentation(self.docu,0)
        self.split()
        self.grid.add(5)
        self.qButton = Button(self.master,text="Finished",command=self.quit,font="Helvetica 12 bold",bg="green").grid(row=self.grid.add(),column=3)

        
    def toggle(self,num):
        self.elec[num].toggle()
        self.mech[num].toggle()
        self.bom[num].set(self.top.get())
        self.userman[num].set(self.top.get())
    def addSubsytemName(self,level,rval,sysnum):
        name = Entry(self.master)
        name.insert(10,"SubSys#" + str(sysnum+1))
        name.grid(row=rval,column=level)
        return name
    
    def addElectrical(self,path,level):
        path.top = self.addPathWithCommand("Electrical",level,path.toggle)
        path.bom = self.addFile("BOM.csv",level+1)
        path.powerbudget = self.addFile("PowerBudget.csv",level+1)
        path.interfacedoc = self.addFile("InterfaceDocument",level+1)
        path.userman = self.addFile("User Manual",level+1)
        path.datasheets = self.addPath("Data Sheets",level+1)
        path.wd = self.addPathWithCommand("Wire Diagrams",level+1,path.toggle_wd)
        path.wd_template = self.addFile("Template",level+2)
        path.schem_path = self.addPathWithCommand("Schematics",level+1,path.toggle_schem)
        path.schem_template = self.addFile("Template",level+2)
        
        path.firm.top = self.addPathWithCommand("Firmware",level+1,path.firm.toggle)
        
        path.firm.api = self.addFile("API Document",level+2)
        path.firm.readme = self.addFile("README.md",level+2)
        path.firm.source = self.addPathWithCommand("Source",level+2,path.firm.toggle_source)
        path.firm.source_c = self.addFile("source.c",level+3)
        path.firm.source_h = self.addFile("source.h",level+3)

        path.firm.binaries = self.addPath("Binaries",level+2)
        
    def addMechanical(self,path,level):
        path.top = self.addPathWithCommand('Mechanical',level,path.toggle)
        path.assemblies = self.addPathWithCommand('Assemblies',level+1,path.toggle_assemblies)
        path.drawings = self.addPathWithCommand('Drawings',level+1,path.toggle_drawings)
    def addPhotos(self,path,level):
        path.top = self.addPathWithCommand('Photos',level,path.toggle)

    def addDocumentation(self,path,level):
        path.top = self.addPathWithCommand('Documentation',level,path.toggle)
        
    def addPath(self,name,level=0):
        tempVar = IntVar()
        tempVar.set(1)
        Checkbutton(self.master,text=(name+'/'),variable=tempVar,justify=RIGHT,font="Helvetica 9 italic",fg="green").grid(row=self.grid.add(),column=level,sticky="W")
        return tempVar;

    def addPathWithCommand(self,name,level,cmd):
        tempVar = IntVar()
        tempVar.set(1)
        Checkbutton(self.master,text=(name+'/'),variable=tempVar,command=cmd,justify=RIGHT,font="Helvetica 9 italic",fg="green").grid(row=(self.grid.add()),column=level,sticky="W")
        return tempVar;

    def addFile(self,name,level=0):
        tempVar = IntVar()
        tempVar.set(1)
        Checkbutton(self.master,text=(name),variable=tempVar,justify=RIGHT,font="Helvetica 8 bold",fg="blue").grid(row=(self.grid.add()),column=level,sticky="w")
        return tempVar
    def split(self,level=0):
        
        temp = Label(self.master,text=('__________________________')).grid(row = self.grid.add(),column=0)
        temp = Label(self.master,text=('__________________________')).grid(row = self.grid.current(),column=1)
        temp = Label(self.master,text=('__________________________')).grid(row = self.grid.current(),column=2)
        temp = Label(self.master,text=('__________________________')).grid(row = self.grid.current(),column=3)
        self.grid.add()
    def toggle(self):
        self.elec.top.set(self.top.get())
        self.elec.toggle()
        self.mech.top.set(self.top.get())
        self.mech.toggle()
        self.bom.set(self.top.get())
        self.userman.set(self.top.get())

    def header1(self):
        Label(self.master,text='Subsystem #',font="Calibri 11 bold").grid(row=self.grid.current(),column=0)
        Label(self.master,text='Subsytem Name',font="Calibri 11 bold").grid(row=self.grid.current(),column=1)
        self.grid.add()
        
    def header2(self):
        temp = Label(self.master,text=('Top Level'),font="Calibri 11 bold").grid(row=self.grid.current(),column=0)
        temp = Label(self.master,text=('Subfolder Level 1'),font="Calibri 11 bold").grid(row=self.grid.current(),column=1)
        temp = Label(self.master,text=('Subfolder Level 3'),font="Calibri 11 bold").grid(row=self.grid.current(),column=2)
        temp = Label(self.master,text=('Subfolder Level 4'),font="Calibri 11 bold").grid(row=self.grid.current(),column=3)
    def quit(self):

        try:

            for i in range(0,self.numsubs):
                self.name[i] = self.name_entry[i].get()
                #print(self.name[i])
        except:
            print("Invalid")
            
     
        self.master.quit
        self.master.destroy()


##master = Tk()
##ss1 = SubSystem(4)
##
##
##mainloop()
