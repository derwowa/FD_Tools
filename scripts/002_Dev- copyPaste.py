#!BPY

"""
Name: 'Copy and Paste Objects'
bpy: 237
Group: 'Object'
Tooltip: 'Copies objects beetween blend files.'
"""

__author__ = "Mariano Hidalgo a.k.a. uselessdreamer"
__url__ = ("bpy", "elysiun")
__version__ = "1.0"

__bpydoc__ = """\
This script copies objects between running bpy instances.

Usage:

While working in a project, open in another instance of bpy the file
wich contains the objects you want to copy, select them and run the script.
Choose [Copy object(s) to Buffer] and close this new bpy instance if you want.
Go back to the other bpy instance and run the script again, this time choosing
[Paste object(s) from Buffer]. Please note they will be pasted in the same layers
the occupied in the original file, so you may no notice anything till you turn that
layers on.

It can also be used in a single instance (ie: first open the file with object, copy,
open the destination blend, paste)

Save the .blend containing the objects you want to copy first, even if it already has
a filename, only saved objects can be copied (if you had altered something, then save).
"""


import bpy
from bpy import Draw, Text, Library, Object

choice = Draw.PupMenu("Copy object(s) to buffer|Paste object(s) from buffer")
if choice == 1:
    objs = Object.GetSelected()
    if len(objs) == 0:
        Draw.PupMenu("Please select at least 1 object!")
    else:
        txt = open(bpy.Get("datadir") + "/buffer","w")
        txt.write(bpy.Get("filename") +"\n")
        for item in objs: 
            txt.write(item.getName() + "\n")  
        txt.close()         
elif choice == 2:   
    txt = Text.Load(bpy.Get("datadir") + "/buffer")
    buffer = txt.asLines()  
    Library.Open(buffer[0])
    buffer.pop(0)
    for item in buffer:
        Library.Load(item, "Object", 0)
    Library.Update()
    Library.Close()
    Text.unlink(txt)
    bpy.Redraw()