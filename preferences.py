import os
import bpy
import sys
from bpy.props import *

addonName = os.path.basename(os.path.dirname(__file__))

class AlignPieMenuProperties(bpy.types.PropertyGroup):
    bl_idname = "apn_PieMenuProperties"

    offsetHorizontal: FloatProperty(name = "Horizontal Offset",
        description = "Horizontal separation distance between nodes",
        default = 30, soft_min = 0.0, soft_max = 100.0)

    offsetVertical: FloatProperty(name = "Vertical Offset",
        description = "Vertical separation distance between nodes",
        default = 15, soft_min = 0.0, soft_max = 100.0)

class AlignNodesPreferences(bpy.types.AddonPreferences):
    bl_idname = addonName

    alignPieMenuProp: PointerProperty(type = AlignPieMenuProperties)

    def draw(self, context):
        layout = self.layout

        row = layout.row(align = True)

        row.prop(self.alignPieMenuProp, "offsetHorizontal")
        row.prop(self.alignPieMenuProp, "offsetVertical")

def getPreferences():
    return bpy.context.preferences.addons[addonName].preferences

def getAlignPieMenuSettings():
    return getPreferences().alignPieMenuProp
