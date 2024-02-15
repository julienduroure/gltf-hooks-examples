import bpy

bl_info = {
    "name": "glTF Extra Animation",
    "category": "Generic",
    "version": (1, 0, 0),
    "blender": (4, 2, 0),
    'location': '',
    'description': 'Add additional animation at export',
    'tracker_url': "",
    'isDraft': False,
    'developer': "Julien Duroure",
    'url': 'https://julienduroure.com',
}

class glTF2ExportUserExtension:

    def __init__(self):
        pass

    def extra_animation_manage(self, extra_samplers, obj_uuid, blender_object, blender_action, gltf_animation, export_settings):
        if len(extra_samplers) != 0:
            node = export_settings['vtree'].nodes[obj_uuid].node
            if node.extras is None:
                node.extras = {}
            if 'animations' not in node.extras.keys():
                node.extras['animations'] = {}

            for extra_sampler in extra_samplers:
                node.extras['animations'][blender_action.name + "_" + extra_sampler[0]] = extra_sampler[1]


def register():
    pass

def unregister():
    pass
