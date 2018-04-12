import bpy
global withUV, noUV, no_uv_arr, with_uv_arr
withUV=""
noUV=""
no_uv_arr=[]
with_uv_arr=[]

for obj in bpy.context.selected_objects:    
    if obj.data.uv_layers:
      global withUV
      with_uv_arr.append(obj.name)
      withUV+=obj.name+", "
      
    else:
        global noUV
        noUV+=obj.name+", "
        no_uv_arr.append(obj.name)
        #obj.data.uv_textures.new()
 
class CreateUVs(bpy.types.Operator):    
    bl_idname="object.createuvs"
    bl_label="create uvs"
    
    def execute(self, context):
        for obj in bpy.context.selected_objects:    
            if obj.data.uv_layers:
              pass
              
            else:                
                obj.data.uv_textures.new()
        
        return {'FINISHED'}
    
class CustomDrawOperator(bpy.types.Operator):
    bl_idname = "object.custom_draw"
    bl_label = "Create Missing UV Maps"
    #bl_options = {'REGISTER', 'UNDO'}

    filepath = bpy.props.StringProperty(subtype="FILE_PATH")

    no_uv = bpy.props.StringProperty(name="No UVs")    
    yes_uv = bpy.props.StringProperty(name="With UVs")
    
    
    
    def draw(self, context):
        layout = self.layout
        layout.label('----------------------------------------NO UV------------------------------------------')
        for entry in no_uv_arr:
            layout.label(entry)
        layout.separator()
        layout.label('----------------------------------------With UV----------------------------------------')
        for entry in with_uv_arr:
            layout.label(entry)
        layout.separator()
        layout.operator("object.createuvs", text="Create UVs")
        
        #layout.label('No UVs: '+noUV+"\n")
        #row = self.layout.split(0.5)
        #layout.separator()
        #layout.label('No UVs: '+withUV)
        #row = self.layout.split(0.5)
        #row.prop(self, "no_uv")
        #row.prop(self, "yes_uv")
      
    
    def execute(self, context):
        print('EXECUTE')
        return {'FINISHED'}

    def invoke(self, context, event):
        wm = context.window_manager
        return wm.invoke_props_dialog(self)
        
bpy.utils.register_class(CreateUVs)
bpy.utils.register_class(CustomDrawOperator)
bpy.ops.object.custom_draw('INVOKE_DEFAULT')

    
#print("We have UV's: "+withUV)
#print("We dont have UV's: "+noUV)