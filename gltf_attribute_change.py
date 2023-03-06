import bpy

bl_info = {
    "name": "glTF Attribute Change",
    "category": "Generic",
    "version": (1, 0, 0),
    "blender": (3, 5, 0),
    'location': '',
    'description': 'Changing some attributes or vertex color',
    'tracker_url': "",
    'isDraft': False,
    'developer': "Julien Duroure",
    'url': 'https://julienduroure.com',
}

class glTF2ExportUserExtension:

    def __init__(self):
        pass

    def gather_attribute_change(self, attribute, data, is_normalized_byte_color, export_settings):
    	if attribute.startswith("COLOR_") and is_normalized_byte_color is False:
    		data['data'][:, 2] = data['data'][:, 0]
    		data['data'][:, 1] = data['data'][:, 1] - 0.8
    		data['data'][:, 0] = 0.0
        
def register():
    pass
    
def unregister():
    pass
