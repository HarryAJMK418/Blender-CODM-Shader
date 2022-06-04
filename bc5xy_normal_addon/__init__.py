bl_info = {
    "name" : "BC5/XY Normal Addon",
    "author" : "COD©Devil", 
    "description" : "This addon adds a node group in the  shader editor which can convert the BC5/XY normal maps to the  Tangent space normal map",
    "blender" : (3, 0, 0),
    "version" : (1, 0, 0),
    "location" : "",
    "waring" : "",
    "doc_url": "", 
    "tracker_url": "", 
    "category" : "Node" 
}


import bpy
import bpy.utils.previews

import os
import os
import os


def string_to_int(value):
    if value.isdigit():
        return int(value)
    return 0

def string_to_icon(value):
    if value in bpy.types.UILayout.bl_rna.functions["prop"].parameters["icon"].enum_items.keys():
        return bpy.types.UILayout.bl_rna.functions["prop"].parameters["icon"].enum_items[value].value
    return string_to_int(value)
    
def icon_to_string(value):
    for icon in bpy.types.UILayout.bl_rna.functions["prop"].parameters["icon"].enum_items:
        if icon.value == value:
            return icon.name
    return "NONE"
    
def enum_set_to_string(value):
    if type(value) == set:
        if len(value) > 0:
            return "[" + (", ").join(list(value)) + "]"
        return "[]"
    return value
    
def string_to_type(value, to_type, default):
    try:
        value = to_type(value)
    except:
        value = default
    return value

addon_keymaps = {}
_icons = None
bc5xy_normal_addon = {}


def get_blend_contents(path, data_type):
    if os.path.exists(path):
        with bpy.data.libraries.load(path) as (data_from, data_to):
            return getattr(data_from, data_type)
    return []

def sna_add_to_node_mt_add_DD18B(self, context):
    if not (False):
        layout = self.layout
        layout.menu('SNA_MT_DA1C2', text='Normal Map ', icon_value=871)
class SNA_OT_Operator_64809(bpy.types.Operator):
    bl_idname = "sna.operator_64809"
    bl_label = "Operator"
    bl_description = ""
    bl_options = {"REGISTER", "UNDO"}
    
    
    sna_group_name: bpy.props.StringProperty(name='Group Name', description='', default='', subtype='NONE', maxlen=0)
    
    @classmethod
    def poll(cls, context):
        return not False
    def execute(self, context):
        print('Running.....')
        if (self.sna_group_name in bpy.data.node_groups):
            pass
        else:
            bpy.ops.wm.append(directory=os.path.join(os.path.dirname(__file__), 'assets', 'Node_asset.blend') + r'\NodeTree', filename=self.sna_group_name, link=False)
        bpy.ops.node.add_node('INVOKE_DEFAULT', type='ShaderNodeGroup', use_transform=True)
        print('Node Added')
        bpy.context.active_node.node_tree = bpy.data.node_groups[self.sna_group_name]
        return {"FINISHED"}
    
    def invoke(self, context, event):
        
        
        return self.execute(context)
class SNA_MT_DA1C2(bpy.types.Menu):
    bl_idname = "SNA_MT_DA1C2"
    bl_label = ""
    @classmethod
    def poll(cls, context):
        return not (False)
    def draw(self, context):
        layout = self.layout.column_flow(columns=1)
        for i_683FC in range(len(get_blend_contents(os.path.join(os.path.dirname(__file__), 'assets', 'Node_asset.blend'), 'node_groups'))):
            if 'BC5' in get_blend_contents(os.path.join(os.path.dirname(__file__), 'assets', 'Node_asset.blend'), 'node_groups')[i_683FC]:
                op = layout.operator('sna.operator_64809', text=get_blend_contents(os.path.join(os.path.dirname(__file__), 'assets', 'Node_asset.blend'), 'node_groups')[i_683FC], icon_value=33, emboss=True, depress=False)
                op.sna_group_name = get_blend_contents(os.path.join(os.path.dirname(__file__), 'assets', 'Node_asset.blend'), 'node_groups')[i_683FC]
            else:
                pass
        



def register():
    
    global _icons
    _icons = bpy.utils.previews.new()
    
    
    bpy.types.NODE_MT_add.append(sna_add_to_node_mt_add_DD18B)
    bpy.utils.register_class(SNA_OT_Operator_64809)
    bpy.utils.register_class(SNA_MT_DA1C2)

def unregister():
    
    global _icons
    bpy.utils.previews.remove(_icons)
    
    wm = bpy.context.window_manager
    kc = wm.keyconfigs.addon
    for km, kmi in addon_keymaps.values():
        km.keymap_items.remove(kmi)
    addon_keymaps.clear()
    
    
    bpy.types.NODE_MT_add.remove(sna_add_to_node_mt_add_DD18B)
    bpy.utils.unregister_class(SNA_OT_Operator_64809)
    bpy.utils.unregister_class(SNA_MT_DA1C2)

