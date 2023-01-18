import bpy

bl_info = {
    "name": "glTF Attribute Keep",
    "category": "Generic",
    "version": (1, 0, 0),
    "blender": (3, 5, 0),
    'location': '',
    'description': 'Keeping some attributes',
    'tracker_url': "",
    'isDraft': False,
    'developer': "Julien Duroure",
    'url': 'https://julienduroure.com',
}

class glTF2ExportUserExtension:

    def __init__(self):
        pass

    def gather_attribute_keep(self, params, export_settings):
    	# All attributes starting with _ are kept.
    	# For others, you can change the default value from False to True to keep them
        if params.attr_name == "keep_me":
        	params.keep = True
        
        params.attr_name = params.attr_name + "_test_renaming"
        
def register():
    pass
    
def unregister():
    pass
