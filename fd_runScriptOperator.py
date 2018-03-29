import bpy
import os

class FDRunScriptOperator (bpy.types.Operator):
    bl_idname = "view3d.fd_run_script"
    bl_label = "Run the script from context"
    scriptName=bpy.props.StringProperty()
    
    def execute(self, context):        
        
        # Use your own script name here:
        filename = self.scriptName

        filepath = os.path.join(os.path.dirname(bpy.data.filepath), filename)
        global_namespace = {"__file__": filepath, "__name__": "__main__"}
        with open(filepath, 'rb') as file:
            exec(compile(file.read(), filepath, 'exec'), global_namespace)
        
        return {'FINISHED'}

   
bpy.utils.register_class(FDRunScriptOperator)