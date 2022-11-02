import bpy

bl_info = {
    "name": "glTF Hooks",
    "category": "Generic",
    "version": (1, 0, 0),
    "blender": (3, 3, 0),
    'location': '',
    'description': 'glTF: roundtrip asset extras',
    'tracker_url': "",
    'isDraft': False,
    'developer': "Julien Duroure",
    'url': 'https://julienduroure.com',
}

class glTF2ExportUserExtension:

    def __init__(self):
        pass

    def gather_asset_hook(self, asset, export_settings):
        if 'gltf2_asset' in bpy.data.scenes[0]:
            asset.extras = bpy.data.scenes[0]['gltf2_asset']

class glTF2ImportUserExtension:

    def __init__(self):
        pass

    def gather_import_gltf_before_hook(self, gltf):
        if 'gltf2_asset' not in bpy.data.scenes[0]:
            bpy.data.scenes[0]['gltf2_asset'] = {}
        bpy.data.scenes[0]['gltf2_asset'].update(gltf.data.asset.extras)


def register():
    pass


def unregister():
    pass
