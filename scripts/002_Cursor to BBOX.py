import bpy
import math
from mathutils import Vector
import collections

 
class InterfaceVars(bpy.types.PropertyGroup):
    align_x = bpy.props.EnumProperty(
        items=[
            ('min', 'min', 'min', '', 0),
            ('mid', 'mid', 'mid', '', 1),
            ('max', 'max', 'max', '', 2),
        ],
        default='min'
    )
    align_y = bpy.props.EnumProperty(
        items=[
            ('min', 'min', 'min', '', 0),
            ('mid', 'mid', 'mid', '', 1),
            ('max', 'max', 'max', '', 2),
        ],
        default='min'
    )
    align_z = bpy.props.EnumProperty(
        items=[
            ('min', 'min', 'min', '', 0),
            ('mid', 'mid', 'mid', '', 1),
            ('max', 'max', 'max', '', 2),
        ],
        default='min'
    )

class ClosePanel(bpy.types.Operator):    
    bl_idname="object.close_panel"
    bl_label="close panel"
    
    def execute(self, context):        
        print("juhhhhhuuuuuu")
        unregister()
        return {'FINISHED'}
    
class AlignCursor(bpy.types.Operator):

    bl_idname = "object.fd_align"
    bl_label = "AlignCursor"
        
    def execute(self, context):
                
        alignX = context.window_manager.interface_vars.align_x
        alignY = context.window_manager.interface_vars.align_y
        alignZ = context.window_manager.interface_vars.align_z
        
        obj = bpy.context.scene.objects.active
        object_details = bounds(obj)
        
        xval=0
        yval=0
        zval=0
        
        if alignX=="min":
            xval=object_details.x.min
        elif alignX=="mid":
            xval=(object_details.x.min+object_details.x.max)/2.0
        elif alignX=="max":
            xval=object_details.x.max
            
            
        if alignY=="min":
            yval=object_details.y.min
        elif alignY=="mid":
            yval=(object_details.y.min+object_details.y.max)/2.0
        elif alignY=="max":
            yval=object_details.y.max
            
        if alignZ=="min":
            zval=object_details.z.min
        elif alignZ=="mid":
            zval=(object_details.z.min+object_details.z.max)/2.0
        elif alignZ=="max":
            zval=object_details.z.max
        
        bpy.context.space_data.cursor_location[0] = xval
        bpy.context.space_data.cursor_location[1] = yval
        bpy.context.space_data.cursor_location[2] = zval       
        
        print("The Values are:"+str(xval))
   
        #unregister()
        return {'FINISHED'}
 
class AlignCursorPanel(bpy.types.Panel):
    bl_idname = "object.alignpanel"
    bl_label = "Align Cursor Tools"
    bl_space_type = "VIEW_3D"
    bl_region_type = "TOOL_PROPS"
    bl_category = "AlignCursorPanel"
 
    def draw(self, context):
        self.layout.label('Align cursor to:')
        row = self.layout.row()
        row.label('X:')
        row.prop(context.window_manager.interface_vars, 'align_x', expand=True)
        row = self.layout.row()
        row.label('Y:')
        row.prop(context.window_manager.interface_vars, 'align_y', expand=True)
        row = self.layout.row()
        row.label('Z:')
        row.prop(context.window_manager.interface_vars, 'align_z', expand=True)
        row = self.layout.row()
        row.operator("object.fd_align", text="Align")
        row.operator("object.origin_set",text="Objectorigin to Cursor").type='ORIGIN_CURSOR'
        self.layout.separator()
        self.layout.operator("object.close_panel", text="Close")




def bounds(obj, local=False):

    local_coords = obj.bound_box[:]
    om = obj.matrix_world

    if not local:    
        worldify = lambda p: om * Vector(p[:]) 
        coords = [worldify(p).to_tuple() for p in local_coords]
    else:
        coords = [p[:] for p in local_coords]

    rotated = zip(*coords[::-1])

    push_axis = []
    for (axis, _list) in zip('xyz', rotated):
        info = lambda: None
        info.max = max(_list)
        info.min = min(_list)
        info.distance = info.max - info.min
        push_axis.append(info)    

    originals = dict(zip(['x', 'y', 'z'], push_axis))

    o_details = collections.namedtuple('object_details', 'x y z')
    return o_details(**originals)

    
def register():
    bpy.utils.register_class(ClosePanel)
    bpy.utils.register_class(AlignCursor)
    bpy.utils.register_class(AlignCursorPanel)    
    bpy.utils.register_class(InterfaceVars)
    bpy.types.WindowManager.interface_vars = bpy.props.PointerProperty(type=InterfaceVars)
    
def unregister():
    del bpy.types.WindowManager.interface_vars
    bpy.utils.unregister_class(ClosePanel)
    bpy.utils.unregister_class(InterfaceVars)
    bpy.utils.unregister_class(AlignCursorPanel)
    bpy.utils.unregister_class(AlignCursor)
    

        
if __name__ == "__main__":
    print("sadfdsf")
    register()
    
