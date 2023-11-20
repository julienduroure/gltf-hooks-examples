import bpy

bl_info = {
    "name": "glTF export unused textures",
    "category": "Generic",
    "version": (1, 0, 0),
    "blender": (4, 1, 0),
    'location': 'File > Export > glTF 2.0',
    'description': 'Export unused textures',
    'tracker_url': "https://github.com/julienduroure/gltf-hooks-examples",
    'isDraft': False,
    'developer': "Julien Duroure",
    'url': 'https://github.com/julienduroure',
}



class GlTFUnusedTexturesProperties(bpy.types.PropertyGroup):
    enabled: bpy.props.BoolProperty(
        name="Export Unused Textures",
        description='Export unused textures',
        default=True
        )

def register():
    bpy.utils.register_class(GlTFUnusedTexturesProperties)
    bpy.types.Scene.GlTFUnusedTexturesProperties = bpy.props.PointerProperty(type=GlTFUnusedTexturesProperties)

def register_panel():
    # Register the panel on demand, we need to be sure to only register it once
    # This is necessary because the panel is a child of the extensions panel,
    # which may not be registered when we try to register this extension
    try:
        bpy.utils.register_class(GLTF_PT_UserExtensionPanel)
    except Exception:
        pass

    # If the glTF exporter is disabled, we need to unregister the extension panel
    # Just return a function to the exporter so it can unregister the panel
    return unregister_panel


def unregister_panel():
    # Since panel is registered on demand, it is possible it is not registered
    try:
        bpy.utils.unregister_class(GLTF_PT_UserExtensionPanel)
    except Exception:
        pass


def unregister():
    unregister_panel()
    bpy.utils.unregister_class(GlTFUnusedTexturesProperties)
    del bpy.types.Scene.GlTFUnusedTexturesProperties

class GLTF_PT_UserExtensionPanel(bpy.types.Panel):

    bl_space_type = 'FILE_BROWSER'
    bl_region_type = 'TOOL_PROPS'
    bl_label = "Enabled"
    bl_parent_id = "GLTF_PT_export_user_extensions"
    bl_options = {'DEFAULT_CLOSED'}

    @classmethod
    def poll(cls, context):
        sfile = context.space_data
        operator = sfile.active_operator
        return operator.bl_idname == "EXPORT_SCENE_OT_gltf"

    def draw(self, context):
        layout = self.layout
        layout.use_property_split = True
        layout.use_property_decorate = False  # No animation.

        row = layout.row()
        row.prop(context.scene.GlTFUnusedTexturesProperties, "enabled")


class glTF2ExportUserExtension:

    def __init__(self):
        # We need to wait until we create the gltf2UserExtension to import the gltf2 modules
        # Otherwise, it may fail because the gltf2 may not be loaded yet
        from io_scene_gltf2.io.com.gltf2_io_extensions import Extension
        self.Extension = Extension
        self.properties = bpy.context.scene.GlTFUnusedTexturesProperties

    def gather_gltf_additional_textures_hook(self, json, additional_json_textures, export_settings):
        print("======>ok")
        if self.properties.enabled:
            if len(additional_json_textures) > 0:
                if json.get('extras') is None:
                    json['extras'] = {}
                json['extras']['additionalTextures'] = additional_json_textures
