from tkinter import *



#Electrical Subclass
class Elec:
    def __init__(self):
        #Initialize variables
        self.top = IntVar()
        self.bom = IntVar()
        self.userman = IntVar()
        self.powerbudget = IntVar()
        self.interfacedoc = IntVar()
        self.wd = IntVar()
        self.wd_template = IntVar()
        self.schem_path = IntVar()
        self.schem_template = IntVar()
        self.firm = Firm()
    def toggle(self):
        #self.top.set(self.wd.get()^1)
        self.wd_template.set(self.top.get())
        self.bom.set(self.top.get())
        self.userman.set(self.top.get())
        self.powerbudget.set(self.top.get())
        self.wd.set(self.top.get())
        self.wd_template.set(self.top.get())
        self.schem_path.set(self.top.get())
        self.schem_template.set(self.top.get())
        self.interfacedoc.set(self.top.get())
        self.firm.top.set(self.top.get())
        self.firm.toggle()
    def toggle_schem(self):
        self.schem_template.set(self.schem_path.get())

    def toggle_wd(self):
        self.wd_template.set(self.wd.get())
    
#Firmware Subclass
class Firm:
    def __init__(self):
        self.top = IntVar()
        self.binaries = IntVar()
        self.api = IntVar()
        self.readme = IntVar()
        self.source = IntVar()
        self.source_c = IntVar()
        self.source_h = IntVar()
    def toggle(self):
        self.binaries.set(self.top.get())
        self.api.set(self.top.get())
        self.readme.set(self.top.get())
        self.source.set(self.top.get())
        self.source_c.set(self.top.get())
        self.source_h.set(self.top.get())
    def toggle_source(self):
        self.source_c.set(self.source.get())
        self.source_h.set(self.source.get())
#Mechanical Subclass
class Mech:
    def __init__(self):
        self.top = IntVar()
        self.drawings = IntVar()
    def toggle(self):
        self.drawings.set(self.top.get())
    def toggle_drawings(self):
        print("toggle drawings")

#Mooring Subclass
class Moor:
    def __init__(self):
        self.top = IntVar()
        self.bath = IntVar()
        self.diag = IntVar()
    def toggle(self):
        self.bath.set(self.top.get())
        self.diag.set(self.top.get())
    def toggle_bath(self):
        print("toggle bath")
    def toggle_diag(self):
        print("toggle diagrams")

#Test Subclass
class FTest:
    def __init__(self):
        self.top = IntVar()
        self.data = IntVar()
        self.report = IntVar()
    def toggle(self):
        self.data.set(self.top.get())
        self.report.set(self.top.get())
    def toggle_data(self):
        print("Add toggle data")

#Subsystem Subclass
class SubSys:
    def __init__(self):
        self.name_entry = 0
        self.name = 0
        self.top = IntVar()
        self.elec = Elec()
        self.mech = Mech()
        self.bom = IntVar()
        self.userman = IntVar()

    def toggle(self):
        self.elec.toggle()
        self.mech.toggle()
        self.bom.set(self.top.get())
        self.userman.set(self.top.get())

#Main File Structure
class FileStructure:
    def __init__(self):
        self.master = Tk()
        self.master.wm_title("Include the following")
        self.master.resizable(width=False,height=True)
        self.master.geometry('{}x{}'.format(600,1100))
        #Add the names in the order you wish 
        
        #Mechanical
        #self.split()
        self.mech = Mech()
        self.mech.top = self.addPathWithCommand('Mechanical',0,self.mech.toggle)
        self.mech.drawings = self.addPathWithCommand('Drawings',1,self.mech.toggle_drawings)


        #Electrical
        #self.split()
        self.elec = Elec()
        self.addElectrical(self.elec,0)
##        self.elec.top = self.addPathWithCommand("Electrical",0,self.elec.toggle)
##        self.elec.bom = self.addFile("BOM.csv",1)
##        self.elec.powerbudget = self.addFile("PowerBudget.csv",1)
##        self.elec.interfacedoc = self.addFile("InterfaceDocument",1)
##        self.elec.userman = self.addFile("User Manual",1)
##        self.elec.wd = self.addPathWithCommand("Wire Diagrams",1,self.elec.toggle_wd)
##        self.elec.wd_template = self.addFile("Template",2)
##        self.elec.schem_path = self.addPathWithCommand("Schematics",1,self.elec.toggle_schem)
##        self.elec.schem_template = self.addFile("Template",2)
##        self.elec.firm.top = self.addPathWithCommand("Firmware",1,self.elec.firm.toggle)
##        
##        self.elec.firm.api = self.addFile("API Document",2)
##        self.elec.firm.readme = self.addFile("README.md",2)
##        self.elec.firm.source = self.addPathWithCommand("Source",2,self.elec.firm.toggle_source)
##        self.elec.firm.source_c = self.addFile("source.c",3)
##        self.elec.firm.source_h = self.addFile("source.h",3)
##
##        self.elec.firm.binaries = self.addPath("Binaries",2)
##        self.top = IntVar()
##        self.binaries = IntVar()
##        self.api = IntVar()
##        self.readme = IntVar()
##        self.source = IntVar()
##        self.source_c = IntVar()
##        self.source_h = IntVar()
        #Mooring
        #self.split()
        self.moor = Moor()
        self.addMooring(self.moor,0)
##        self.moor.top = self.addPathWithCommand("Mooring",0,self.moor.toggle)
##        self.moor.bath = self.addPathWithCommand("Bathymetry",1,self.moor.toggle_bath)
##        self.moor.diag = self.addPathWithCommand("Diagrams",1,self.moor.toggle_diag)

        
        #Test
        #self.split()
        self.test = FTest()
        self.addTest(self.test,0)
##        self.test.top = self.addPathWithCommand("Test",0,self.test.toggle)
##        self.test.report = self.addFile("Test Report",1)
##        self.test.data = self.addPath("Data",1)
        

        #Subsystem
        #Add Subsystem
        self.split()
        self.subsystem = self.addPath("SubSystems",0)
        #self.sub1 = SubSys()
        self.numsub_val = self.addNumberOfSubsystems(1)
        self.sub1 = self.addSubsystem(1)



        self.qButton = Button(self.master,text="Finished",command=self.quit).grid(sticky=E+S,pady=4)  
    def SetInt(self):
        #mechanical systems
        self.mech.set(1)

        #electrical systems
        self.elec.set(1)
        self.elec_wd.set(1)
  
                               
    def get(self):
        self.Mechanical = self.mech.top.get()
        self.Electrical = self.elec.top.get()
    def addMooring(self,path,level):
        path.top = self.addPathWithCommand("Mooring",level,path.toggle)
        path.bath = self.addPathWithCommand("Bathymetry",level+1,path.toggle_bath)
        path.diag = self.addPathWithCommand("Diagrams",level+1,path.toggle_diag)

    def addTest(self,path,level):
        path.top = self.addPathWithCommand("Test",level,path.toggle)
        path.report = self.addFile("Test Report",level + 1)
        path.data = self.addPath("Data",level+1)
    def addPath(self,name,level=0):
        tempVar = IntVar()
        tempVar.set(1)
        Checkbutton(self.master,text=(name+'/'),variable=tempVar,justify=RIGHT,font="Helvetica 9 italic",fg="green").grid(column=level,sticky="W")
        return tempVar;

    def addPathWithCommand(self,name,level,cmd):
        tempVar = IntVar()
        tempVar.set(1)
        Checkbutton(self.master,text=(name+'/'),variable=tempVar,command=cmd,justify=RIGHT,font="Helvetica 9 italic",fg="green").grid(column=level,sticky="W")
        return tempVar;

    def addFile(self,name,level=0):
        tempVar = IntVar()
        tempVar.set(1)
        Checkbutton(self.master,text=(name),variable=tempVar,justify=RIGHT,font="Helvetica 8 bold",fg="blue").grid(column=level,sticky="w")
        return tempVar
    def addNumberOfSubsystems(self,level):
        val = Entry(self.master)
        val.insert(10,"# SubSys To Add")
        val.grid(column=level)
        return val
    def addSubsytemName(self,level):
        name = Entry(self.master)
        name.insert(10,"SubSys Name")
        name.grid(column=level)
        return name
    def addSubsystem(self,num):
        temp = SubSys()
        #temp.top = self.addPathWithCommand("Subsystem #"+str(num),1,temp.toggle)
        #temp.name_entry = self.addSubsytemName(1)
##        temp.elec.top = self.addPathWithCommand("Electrical",2,self.elec.toggle)
##        temp.elec.bom = self.addFile('BOM.csv',3)
##        temp.elec.userman = self.addFile('UserManual',3)
##        temp.elec.schem_path = self.addPath('Schematics',3)
##        temp.elec.schem_template = self.addFile('Template',4)
        self.addElectrical(temp.elec,1) 

        return temp
    def addNewSubsystem(self):
        temp = 0

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
##        path.top = IntVar()
##        path.binaries = IntVar()
##        path.api = IntVar()
##        path.readme = IntVar()
##        path.source = IntVar()
##        path.source_c = IntVar()
##        path.source_h = IntVar()
    def split(self,level=0):
        temp = Label(self.master,text=('______________')).grid(column=0)

    def quit(self):
        #self.sub1.name = self.sub1.name_entry.get()
        try:
            self.numsubs = int(self.numsub_val.get())
        except:
            self.numsubs = 0
        print(self.numsubs)
        self.master.quit
        self.master.destroy()

print("Start ")

fs = FileStructure()

mainloop()



#fs.get()
#print(fs.Mechanical)
#print(fs.Electrical)

#print(fs.mech.get())
