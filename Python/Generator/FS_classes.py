from tkinter import *


#Electrical Subclass
class Elec:
    def __init__(self):
        #Initialize variables
        self.top = IntVar()
        self.bom = IntVar()
        #self.userman = IntVar()
        self.powerbudget = IntVar()
        self.interfacedoc = IntVar()
        self.wd = IntVar()
        self.wd_template = IntVar()
        self.schem_path = IntVar()
        self.schem_template = IntVar()
        self.firm = Firm()
        self.photos = IntVar()
        self.datasheets = IntVar()
    def toggle(self):
        #self.top.set(self.wd.get()^1)
        self.wd_template.set(self.top.get())
        self.bom.set(self.top.get())
        #self.userman.set(self.top.get())
        self.powerbudget.set(self.top.get())
        self.wd.set(self.top.get())
        self.wd_template.set(self.top.get())
        self.schem_path.set(self.top.get())
        self.schem_template.set(self.top.get())
        self.interfacedoc.set(self.top.get())
        self.photos.set(self.top.get())
        self.firm.top.set(self.top.get())
        self.firm.toggle()
        self.datasheets.set(self.top.get())
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
        self.assemblies = IntVar()
        self.drawings = IntVar()
    def toggle(self):
        self.assemblies.set(self.top.get())
        self.drawings.set(self.top.get())
        
    def toggle_assemblies(self):
        return
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

class Software:
    def __init__(self):
        self.top = IntVar()
        self.gui = IntVar()
        self.userman = IntVar()
    def toggle(self):
        self.gui.set(self.top.get())
        self.userman.set(self.top.get())
    def toggle_gui(self):
        self.userman.set(self.gui.get())

#Test Subclass
class FTest:
    def __init__(self):
        self.top = IntVar()
        self.data = IntVar()
        self.report = IntVar()
        self.plan = IntVar()
    def toggle(self):
        self.data.set(self.top.get())
        self.report.set(self.top.get())
        self.plan.set(self.top.get())
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

class Docu:
    def __init__(self):
        self.top = IntVar()
        self.projreqs = IntVar()
        self.userman = IntVar()
        self.deploy = IntVar()
    def toggle(self):
        self.projreqs.set(self.top.get())
        self.userman.set(self.top.get())
        self.deploy.set(self.top.get())
        return

class Purchases:
    def __init__(self):
        self.top = IntVar()
        self
    def toggle(self):
        return
