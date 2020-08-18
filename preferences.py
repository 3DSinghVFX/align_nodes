import os
import bpy
import sys
from bpy.props import *

addonName = os.path.basename(os.path.dirname(__file__))

class AlignPieMenuProperties(bpy.types.PropertyGroup):
    bl_idname = "apn_PieMenuProperties"

    offset: FloatProperty(name = "Offset for Align Pie Menu",
        description = "Offset between nodes for Align Pi Menu",
        default = 30, soft_min = 0.0, soft_max = 100.0)

class AlignNodesPreferences(bpy.types.AddonPreferences):
    bl_idname = addonName

    alignPieMenuProp: PointerProperty(type = AlignPieMenuProperties)

    def draw(self, context):
        layout = self.layout

        row = layout.row()

        col = row.column(align = True)
        col.prop(self.alignPieMenuProp, "offset")

def getPreferences():
    return bpy.context.preferences.addons[addonName].preferences

def getAlignPieMenuSettings():
    return getPreferences().alignPieMenuProp
