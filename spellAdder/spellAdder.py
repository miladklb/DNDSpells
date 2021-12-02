from tkinter import *
from tkinter import ttk
import tkinter as tk
import json
# Create a spell from GUI fields
def createSpell():
    with open(fileName.get(), "a+") as spellBookFile:
        try:
            spellBookFile.seek(0)
            spellBook = json.load(spellBookFile)
            print(spellBook)
        except Exception as e:
            print("Creating new spellbook file.")
            spellBook = []
        newSpell = {
            "name": name.get(),
            "desc": desc.get("1.0", "end"),
            "range": range.get(),
            "ritual": ritualVar.get(),
            "duration": duration.get(),
            "concentration": concentrationVar.get(),
            "casting_time": cast.get(),
            "level": levelVar.get(),
            "school": school.get(),
            "class": charClass.get(),
            "verbal": verbalVar.get(),
            "material": materialVar.get(),
            "somatic": somaticVar.get()
        }
        spellBook.append(newSpell)
    with open(fileName.get(), "w+") as spellBookFile:
        json.dump(spellBook, spellBookFile)


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
addButton = ttk.Button(applyGrid, text="Add spell", command= createSpell)
addButton.grid(column=0, row=1,sticky="n")
clearButton = ttk.Button(applyGrid, text="Clear fields")
clearButton.grid(column=0, row=2, sticky="n")

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

# Page
pageLabel = ttk.Label(frm, text="Page:")
page= ttk.Entry(frm)
pageLabel.grid(column=0, row=2, sticky="w")
page.grid(column=1, row=2, sticky="w")

# Range
rangeLabel = ttk.Label(frm, text="Range:")
range = ttk.Entry(frm)
rangeLabel.grid(column=0, row=3, sticky="w")
range.grid(column=1, row=3, sticky="w")

# Components
compLabel = ttk.Label(frm, text="Components:")
compLabel.grid(column=0, row=4, sticky="w")

componentFrm = ttk.Frame(frm)
componentFrm.grid()
componentFrm.grid(column=1, row=4, sticky="w")

verbalVar = tk.IntVar()
somaticVar = tk.IntVar()
materialVar = tk.IntVar()
verbal = ttk.Checkbutton(componentFrm, text="Verbal", variable=verbalVar)
somatic = ttk.Checkbutton(componentFrm, text="Somatic", variable=somaticVar)
material = ttk.Checkbutton(componentFrm, text="Material", variable=materialVar)
verbal.grid(column=0, row=0, sticky="w")
somatic.grid(column=1, row=0, sticky="w")
material.grid(column=2, row=0, sticky="w")

# Materials
materialLabel = ttk.Label(frm, text="Materials:")
material = ttk.Entry(frm)
materialLabel.grid(column=0, row=5, sticky="w")
material.grid(column=1, row=5, sticky="w")

# Ritual
ritualLabel = ttk.Label(frm, text="Ritual:")
ritualVar = tk.IntVar()
ritual = ttk.Checkbutton(frm, variable=ritualVar)
ritualLabel.grid(column=0, row=6, sticky="w")
ritual.grid(column=1, row=6, sticky="w")

# Duration
durationLabel = ttk.Label(frm, text="Duration:")
duration= ttk.Entry(frm)
durationLabel.grid(column=0, row=7, sticky="w")
duration.grid(column=1, row=7, sticky="w")

# Concentration
concentrationLabel = ttk.Label(frm, text="Concentration:")
concentrationVar = tk.IntVar()
concentration = ttk.Checkbutton(frm, variable=concentrationVar)
concentrationLabel.grid(column=0, row=8, sticky="w")
concentration.grid(column=1, row=8, sticky="w")

# Casting Time
castLabel = ttk.Label(frm, text="Cast time:")
cast = ttk.Entry(frm)
castLabel.grid(column=0, row=9, sticky="w")
cast.grid(column=1, row=9, sticky="w")

# Level
levelVar = tk.IntVar()
levelLabel = ttk.Label(frm, text="Level:")
level = ttk.OptionMenu(frm, levelVar, "Choose Level", 0,1,2,3,4,5,6,7,8,9)
levelLabel.grid(column=0, row=10, sticky="w")
level.grid(column=1, row=10, sticky="w")

# School
schoolLabel = ttk.Label(frm, text="School:")
school = ttk.Entry(frm)
schoolLabel.grid(column=0, row=11, sticky="w")
school.grid(column=1, row=11, sticky="w")

# Class
classLabel = ttk.Label(frm, text="Class:")
charClass = ttk.Entry(frm)
classLabel.grid(column=0, row=12, sticky="w")
charClass.grid(column=1, row=12, sticky="w")

root.mainloop()

