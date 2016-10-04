from tkinter import *

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
    def __init__(self,numSubs=1):
        self.grid = Grid()
        self.master = Tk()
        self.top = IntVar()
        self.name_entry[numSubs] = {}
        for i in range(0,numSubs):
            self.name_entry[i] = self.addSubsytemName(0)
            self.name[i] = 0
            
            self.elec[i] = Elec()
            self.mech[i] = Mech()
            self.bom[i] = IntVar()
            self.userman[i] = IntVar()

            self.addElectrical(self.elec,1)
            self.addMechanical(self.mech,1)

    def toggle(self):
        self.elec.toggle()
        self.mech.toggle()
        self.bom.set(self.top.get())
        self.userman.set(self.top.get())
    def addSubsytemName(self,level):
        name = Entry(self.master)
        name.insert(10,"SubSys Name")
        name.grid(column=level)
        return name

    def addElectrical(self,path,level):
        path.top = self.addPathWithCommand("Electrical",level,path.toggle)
        path.bom = self.addFile("BOM.csv",level+1)
        path.powerbudget = self.addFile("PowerBudget.csv",level+1)
        path.interfacedoc = self.addFile("InterfaceDocument",level+1)
        path.userman = self.addFile("User Manual",level+1)
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
        path.drawings = self.addPathWithCommand('Drawings',level+1,path.toggle_drawings)
        
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



ss = SubSystem(2)

mainloop()
