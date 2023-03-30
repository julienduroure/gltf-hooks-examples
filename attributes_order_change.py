import bpy

bl_info = {
    "name": "glTF Attributes Change",
    "category": "Generic",
    "version": (1, 0, 0),
    "blender": (3, 6, 0),
    'location': '',
    'description': 'Changing attributes data, as order',
    'tracker_url': "",
    'isDraft': False,
    'developer': "Julien Duroure",
    'url': 'https://julienduroure.com',
}

class glTF2ExportUserExtension:

    def __init__(self):
        pass

    def gather_attributes_change(self, attributes, export_settings):

        def sorted_item(item):
            
            sort_items = {
                "POSITION": 0,
                "NORMAL": 1,
                "TEXCOORD_0": 2
            }

            return sort_items.get(item, 999)

        attributes.sort(key=lambda item: sorted_item(item['gltf_attribute_name']))


def register():
    pass
    
def unregister():
    pass

