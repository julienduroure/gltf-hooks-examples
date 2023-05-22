import bpy

bl_info = {
    "name": "glTF Node Name",
    "category": "Generic",
    "version": (1, 0, 0),
    "blender": (3, 6, 0),
    'location': '',
    'description': 'Change gltf node name',
    'tracker_url': "",
    'isDraft': False,
    'developer': "Julien Duroure",
    'url': 'https://julienduroure.com',
}

class glTF2ExportUserExtension:

    def __init__(self):
        pass

    def gather_node_name_hook(self, gltf_hook_name, blender_object, export_settings):
    	# Example: Any duplicated name in Blender (Cube / Cube.001 / Cube.002 / ... will be exported as Cube for glTF node names
    	if len(gltf_hook_name.name) > 4 and gltf_hook_name.name[-4] == "." and gltf_hook_name.name[-3:].isdigit():
    		gltf_hook_name.name = gltf_hook_name.name[:-4]
        
def register():
    pass
    
def unregister():
    pass
