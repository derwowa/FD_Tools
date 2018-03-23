bl_info = {
        "name": "framedivision Menu",
        "category": "framedivision",
        "author": "Wowa"
        }        

import bpy
import os
import platform
import importlib

class fdMenu(bpy.types.Menu):
    bl_label="framedivision Menu"
    bl_idname="view3d.fd_menu"
   
    
    global arr_scripts, fd_scriptPath
    if os.name == "posix":
        fd_basePath="/_Daten/OneDrive/Blender/Plugins/FD_Menu"
        fd_scriptPath=fd_basePath+"/scripts"
        exec(compile(open(fd_basePath+"/fd_runScriptOperator.py").read(), fd_basePath+"fd_runScriptOperator.py", 'exec'))
    else:
        fd_basePath="C:\\Users\\axel\\OneDrive\\Blender\\Git Repository FD\\FD_Tools"
        fd_scriptPath=fd_basePath+"\\scripts"
        exec(compile(open(fd_basePath+"\\fd_runScriptOperator.py").read(), fd_basePath+"\\fd_runScriptOperator.py", 'exec'))
        
    
    #create an array and store all the scriptnames in it
    
    arr_scripts = []
    
    for subdir, dirs, files in os.walk(fd_scriptPath):
        for file in files:
            arr_scripts.append(file)            
    arr_scripts=sorted(arr_scripts)
    print(arr_scripts)
    
    scriptName = bpy.props.StringProperty()
    
    def draw(self, context):
        layout = self.layout
        layout.separator()
      
        layout.operator("mesh.faces_select_linked_flat")
        global arr_scripts, fd_scriptPath
        for script in arr_scripts:
            if "seperator" in script: 
                layout.separator()
            else:
                layout.operator("view3d.fd_run_script",text=script[4:-3]).scriptName=fd_scriptPath+"\\"+script
        


def register():
    bpy.utils.register_class(fdMenu)
    bpy.ops.wm.call_menu(name=fdMenu.bl_idname)
    
def unregister():
    bpy.utils.unregister_class(fdMenu)
    
if __name__ == "__main__":
    register()