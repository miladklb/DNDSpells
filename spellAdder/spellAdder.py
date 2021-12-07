from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import tkinter as tk
import json
import os

hasCompiled = True

def startup():
    compileSpells()

# Create a spell from GUI fields
def createSpell():
    # Make sure important fields are filled
    try:
        levelVar.get()
    except TclError:
        messagebox.showerror(title="PLEASE", message="FILL OUT THE LEVEL")
        return
    spellBookFileName = fileName.get()
    # Provide default file name if none is given
    if spellBookFileName == "":
        messagebox.showwarning(title="Empty Spellbook Name", message="Defaulting to spells.json")
        spellBookFileName = "spells"

    # Create folder and file if it doesn't exist
    if not os.path.exists("spellBooks"):
        os.mkdir("spellBooks")
    if not os.path.exists(f"spellBooks/{spellBookFileName}.json"):
        open(f"spellBooks/{spellBookFileName}.json", "w+")

    # Read json list from file and append data
    with open(f"spellBooks/{spellBookFileName}.json", "r") as spellBookFile:
        try:
            spellBook = json.load(spellBookFile)
        except Exception:
            spellBook = []
        newSpell = {
            "name": name.get(),
            "desc": desc.get("1.0", "end").rstrip("\n"),
            "range": range.get(),
            "ritual": intToBool(ritualVar.get()),
            "duration": duration.get(),
            "concentration": intToBool(concentrationVar.get()),
            "casting_time": cast.get(),
            "level": levelVar.get(),
            "school": school.get(),
            "class": (charClass.get()).split(),
            "level_desc": levelToLevelDesc(levelVar.get()),
            "class_desc": ", ".join(charClass.get().split()),
            "range_desc": range.get(),
            "component_desc": generateComponentDesc(intToBool(verbalVar.get()),
                                                    intToBool(somaticVar.get()),
                                                    intToBool(materialVar.get())),
            "verbal": intToBool(verbalVar.get()),
            "material": intToBool(materialVar.get()),
            "somatic": intToBool(somaticVar.get()),
            "source": source.get(),
            "page": 69 if page.get() == "" else int(page.get())
        }
        # Only add material fields if materials is true
        if(newSpell["material"]):
            newSpell["material_desc"] = materialDesc.get()
            newSpell["material_cost"] = intToBool(materialCostVar)
        # Only add higher level field if it's not empty
        if(higherLevel.get("1.0", "end") != "\n"):
            newSpell["higher_level"] = higherLevel.get("1.0", "end").rstrip("\n")
        spellBook.append(newSpell)
    # Write appended json list to file
    with open(f"spellBooks/{spellBookFileName}.json", "w+") as spellBookFile:
        json.dump(spellBook, spellBookFile, indent=2)
    uncompileSpells()


def uncompileSpells():
    global hasCompiled
    ttk.Style().configure("compileStyle.TButton", background="red")
    hasCompiled = False

def compileSpells():
    global hasCompiled
    ttk.Style().configure("compileStyle.TButton", background="green")
    hasCompiled = True

def clearFields():
    # Clear all the text fields
    name.delete(0, "end")
    desc.delete("1.0", "end")
    range.delete(0, "end")
    higherLevel.delete("1.0", "end")
    duration.delete(0, "end")
    page.delete(0, "end")
    materialDesc.delete(0, "end")
    charClass.delete(0, "end")
    school.delete(0, "end")
    source.delete(0, "end")
    cast.delete(0, "end")
    levelVar.set("Choose Again")

    # Toggle all the checkbuttons
    if intToBool(ritualVar.get()):
        ritual.invoke()
    if intToBool(concentrationVar.get()):
        concentration.invoke()
    if intToBool(materialVar.get()):
        material.invoke()
    if intToBool(somaticVar.get()):
        somatic.invoke()
    if intToBool(verbalVar.get()):
        verbal.invoke()
    if intToBool(materialCostVar.get()):
        materialCostVar.set(0)


def levelToLevelDesc(level):
    match level:
        case 0:
            return "Cantrip"
        case 1:
            return "1st-level"
        case 2:
            return "2nd-level"
        case 3:
            return "3rd-level"
        case _ if level > 3:
            return f"{level}th-level"
        case _ :
            raise ValueError

def generateComponentDesc(verbal, somatic, material):
    desc = []
    if verbal:
        desc.append("V")
    if somatic:
        desc.append("S")
    if material:
        desc.append("M")
    return ", ".join(desc)

def intToBool(num):
    return False if num == 0 else True

def toggleMaterialOptions():
    if intToBool(materialVar.get()):
        materialDesc.config(state="normal")
        materialCost.config(state="normal")
    else:
        materialDesc.config(state="disabled")
        materialCost.config(state="disabled")

def closeWindow():
    global hasCompiled
    if not hasCompiled and messagebox.askokcancel("Exit", "You have not compiled the latest spell,"
                                                  " do you want to quit without compiling?"):
        # If they click ok and spells have not been compiled
        root.destroy()
    elif hasCompiled:
        # If the spells have been compiled
        root.destroy()
    else:
        # If they click cancel to the exit prompt
        pass

# GUI code
root = Tk(className='Add a spell!')
frm = ttk.Frame(root, padding=10)
frm.grid()

applyGrid = ttk.Frame(root, padding=20)
applyGrid.grid(column=1, row=0)

fileNameFrame = ttk.LabelFrame(applyGrid, text="Spellbook Name")
fileName = ttk.Entry(fileNameFrame)
fileName.grid(column=0, row=0, sticky="n")
fileNameFrame.grid(column=0, row=0, sticky="n")
addButton = ttk.Button(applyGrid, text="Add spell", command=createSpell)
addButton.grid(column=0, row=1,sticky="n")
clearButton = ttk.Button(applyGrid, text="Clear fields", command=clearFields)
clearButton.grid(column=0, row=2, sticky="n")
compileButton = ttk.Button(applyGrid, style="compileStyle.TButton", text="Compile spells", command=compileSpells)
compileButton.grid(column=0, row=3, sticky="n")

'''
Label = ttk.Label(frm, text="")
 = ttk.Entry(frm)
Label.grid(column=0, row=, sticky="w")
.grid(column=1, row=, sticky="w")
'''
# Name
nameLabel = ttk.Label(frm, text="Name:")
name = ttk.Entry(frm)
nameLabel.grid(column=0, row=0, sticky="w")
name.grid(column=1, row=0, sticky="w")

# Desc
descLabel = ttk.Label(frm, text="Description:")
desc = Text(frm, height=10)
descLabel.grid(column=0, row=1, sticky="nw")
desc.grid(column=1, row=1, sticky="w")

# Higher Level
higherLabel = ttk.Label(frm, text="Higher Levels:")
higherLevel = Text(frm, height=3)
higherLabel.grid(column=0, row=2, sticky="nw")
higherLevel.grid(column=1, row=2, sticky="w")

# Page
pageLabel = ttk.Label(frm, text="Page:")
page= ttk.Entry(frm)
pageLabel.grid(column=0, row=3, sticky="w")
page.grid(column=1, row=3, sticky="w")

# Range
rangeLabel = ttk.Label(frm, text="Range:")
range = ttk.Entry(frm)
rangeLabel.grid(column=0, row=4, sticky="w")
range.grid(column=1, row=4, sticky="w")



# Materials
materialFrame = ttk.Frame(frm)
materialLabel = ttk.Label(frm, text="Materials:")
materialLabel.grid(column=0, row=6, sticky="w")
materialFrame.grid(column=1, row=6, sticky="w")

materialDesc = ttk.Entry(materialFrame, state="disabled")
materialCostVar = tk.IntVar()
materialCost = ttk.Checkbutton(materialFrame, text="Consume?", variable=materialCostVar, state="disabled")
materialDesc.grid(column=0, row=0, sticky="w")
materialCost.grid(column=1, row=0, sticky="w")

# Components
compLabel = ttk.Label(frm, text="Components:")
compLabel.grid(column=0, row=5, sticky="w")

componentFrm = ttk.Frame(frm)
componentFrm.grid()
componentFrm.grid(column=1, row=5, sticky="w")

verbalVar = tk.IntVar()
somaticVar = tk.IntVar()
materialVar = tk.IntVar()
verbal = ttk.Checkbutton(componentFrm, text="Verbal", variable=verbalVar)
somatic = ttk.Checkbutton(componentFrm, text="Somatic", variable=somaticVar)
material = ttk.Checkbutton(componentFrm, text="Material", variable=materialVar, command=toggleMaterialOptions)
verbal.grid(column=0, row=0, sticky="w")
somatic.grid(column=1, row=0, sticky="w")
material.grid(column=2, row=0, sticky="w")

# Ritual
ritualLabel = ttk.Label(frm, text="Ritual:")
ritualVar = tk.IntVar()
ritual = ttk.Checkbutton(frm, variable=ritualVar)
ritualLabel.grid(column=0, row=7, sticky="w")
ritual.grid(column=1, row=7, sticky="w")

# Duration
durationLabel = ttk.Label(frm, text="Duration:")
duration= ttk.Entry(frm)
durationLabel.grid(column=0, row=8, sticky="w")
duration.grid(column=1, row=8, sticky="w")

# Concentration
concentrationLabel = ttk.Label(frm, text="Concentration:")
concentrationVar = tk.IntVar()
concentration = ttk.Checkbutton(frm, variable=concentrationVar)
concentrationLabel.grid(column=0, row=9, sticky="w")
concentration.grid(column=1, row=9, sticky="w")

# Casting Time
castLabel = ttk.Label(frm, text="Cast time:")
cast = ttk.Entry(frm)
castLabel.grid(column=0, row=10, sticky="w")
cast.grid(column=1, row=10, sticky="w")

# Level
levelVar = tk.IntVar()
levelLabel = ttk.Label(frm, text="Level:")
level = ttk.OptionMenu(frm, levelVar, "Choose Level", 0,1,2,3,4,5,6,7,8,9, direction="below")
levelLabel.grid(column=0, row=11, sticky="w")
level.grid(column=1, row=11, sticky="w")

# School
schoolLabel = ttk.Label(frm, text="School:")
school = ttk.Entry(frm)
schoolLabel.grid(column=0, row=12, sticky="w")
school.grid(column=1, row=12, sticky="w")

# Class
classLabel = ttk.Label(frm, text="Class:")
charClass = ttk.Entry(frm)
classLabel.grid(column=0, row=13, sticky="w")
charClass.grid(column=1, row=13, sticky="w")

# Source
sourceLabel = ttk.Label(frm, text="Source:")
source = ttk.Entry(frm)
sourceLabel.grid(column=0, row=14, sticky="w")
source.grid(column=1, row=14, sticky="w")

# allow grabbing the window close event
root.protocol("WM_DELETE_WINDOW", closeWindow)
root.after_idle(startup)
root.mainloop()

