from tkinter import *

class Grid:
    def __init__(self):
        self.val = 0
    def add(self,num=0):
        self.val += (1+num)
        return self.val
    def current(self):
        return self.val

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
        self.photos = IntVar()
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
        self.photos.set(self.top.get())
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
        return

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
        return
    def toggle_diag(self):
        return

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
        return

class Photos:
    def __init__(self):
        self.top = IntVar()
    def toggle(self):
        return

class Cruise:
    def __init__(self):
        self.top = IntVar()
        self.report = IntVar()
        self.data = IntVar()
    def toggle(self):
        self.report.set(self.top.get())
        self.data.set(self.top.get())


#Main File Structure
class FileStructure:
    def __init__(self):
        self.grid = Grid()
        
        self.master = Tk()
        self.master.wm_title("Include the following")
        self.master.resizable(width=False,height=True)
        #self.master.geometry('{}x{}'.format(600,1100))
        #self.master.geometry("550x800+30+30")

        
        self.header()
        self.split()
        
        #Add the names in the order you wish 
        
        #Mechanical
        #self.split()
        self.mech = Mech()
        self.addMechanical(self.mech,0)


        #Electrical
        #self.split()
        self.elec = Elec()
        self.addElectrical(self.elec,0)

        #Mooring
        #self.split()
        self.moor = Moor()
        self.addMooring(self.moor,0)

        #Photos
        self.photos = Photos()
        self.addPhotos(self.photos,0)

        #Cruise
        self.cruise = Cruise()
        self.addCruise(self.cruise,0)
        
        #Test
        #self.split()
        self.test = FTest()
        self.addTest(self.test,0)

        

        #Subsystem
        #Add Subsystem
        self.split()

        
        self.subsystem = self.addPath("SubSystems",0)
        #self.sub1 = SubSys()
        self.numsub_val = self.addNumberOfSubsystems(1)
        #self.sub1 = self.addSubsystem(1)

        print(self.grid.current())
        self.grid.add(10)
        print(self.grid.current())
        #self.grid.add()
        self.qButton = Button(self.master,text="Finished",command=self.quit).grid(row=self.grid.current(),column=3)
        #,sticky=E+S,pady=4
    def SetInt(self):
        #mechanical systems
        self.mech.set(1)

        #electrical systems
        self.elec.set(1)
        self.elec_wd.set(1)

                               
    def get(self):
        self.Mechanical = self.mech.top.get()
        self.Electrical = self.elec.top.get()

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
        #self.addElectrical(temp.elec,1)
        #self.addMechanical(temp.mech,1)
        return temp
    
    def addNewSubsystem(self):
        temp = 0
        
    def addMechanical(self,path,level):
        path.top = self.addPathWithCommand('Mechanical',level,path.toggle)
        path.drawings = self.addPathWithCommand('Drawings',level+1,path.toggle_drawings)
        
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

    def addMooring(self,path,level):
        path.top = self.addPathWithCommand("Mooring",level,path.toggle)
        path.bath = self.addPathWithCommand("Bathymetry",level+1,path.toggle_bath)
        path.diag = self.addPathWithCommand("Diagrams",level+1,path.toggle_diag)

    def addPhotos(self,path,level):
        path.top = self.addPathWithCommand("Photos",level,path.toggle)

    def addCruise(self,path,level):
        path.top = self.addPathWithCommand("Cruise",level,path.toggle)
        path.report = self.addFile("Cruise Report",level+1)
        path.data = self.addPath("Data",level+1)
        
    def addTest(self,path,level):
        path.top = self.addPathWithCommand("Test",level,path.toggle)
        path.report = self.addFile("Test Report",level + 1)
        path.data = self.addPath("Data",level+1)
        
    def split(self,level=0):
        
        temp = Label(self.master,text=('__________________________')).grid(row = self.grid.add(),column=0)
        temp = Label(self.master,text=('__________________________')).grid(row = self.grid.current(),column=1)
        temp = Label(self.master,text=('__________________________')).grid(row = self.grid.current(),column=2)
        temp = Label(self.master,text=('__________________________')).grid(row = self.grid.current(),column=3)
        #temp = Label(self.master,text=('__________________________')).grid(row = self.grid.current(),column=4)

    def header(self):
        temp = Label(self.master,text=('Top Level'),font="Calibri 11 bold").grid(row=self.grid.current(),column=0)
        temp = Label(self.master,text=('Subfolder Level 1'),font="Calibri 11 bold").grid(row=self.grid.current(),column=1)
        temp = Label(self.master,text=('Subfolder Level 3'),font="Calibri 11 bold").grid(row=self.grid.current(),column=2)
        temp = Label(self.master,text=('Subfolder Level 4'),font="Calibri 11 bold").grid(row=self.grid.current(),column=3)
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
