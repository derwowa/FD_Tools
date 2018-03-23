import bpy

class FDRunScriptOperator (bpy.types.Operator):
    bl_idname = "view3d.fd_run_script"
    bl_label = "Run the script from context"
    scriptName=bpy.props.StringProperty()
    print("asdf",scriptName)

    def execute(self, context):
        # rather than printing, use the report function,
        # this way the message appears in the header,
        #print(scriptName)
        print({'INFO'}, self.scriptName)
        #exec(compile(open(self.scriptName).read(), self.scriptName, 'exec'))
        myCode = open(self.scriptName).read()
        
        #d = dict(locals(), **globals())
        exec (myCode,globals())
        #print (myCode)
        
        #self.report({'INFO'}, context )
        #bpy.utils.unregister_class(FDRunScriptOperator) 
        return {'FINISHED'}

   
bpy.utils.register_class(FDRunScriptOperator)