import bpy

class AlignPieMenu(bpy.types.Menu):
    bl_idname = "APN_MT_align_pie"
    bl_label = "Align Pie"

    def draw(self, context):
        pie = self.layout.menu_pie()

        pie.operator("node.align_dependencies", text = "Dependencies", icon = "REW")

        pie.operator("node.align_dependent_nodes", text = "Dependent", icon = "FF")

        pie.operator("node.stake_down_selection_nodes", text = "Selection", icon = "FILE_TEXT")

        pie.operator("node.stake_up_selection_nodes", text = "Selection", icon = "FILE_TEXT")

        pie.operator("node.align_top_selection_nodes", text = "Selection", icon = "TRIA_UP_BAR")

        pie.operator("node.align_top_selection_nodes", text = "Selection", icon = "TRIA_UP_BAR")

        pie.operator("node.align_left_side_selection_nodes", text = "Selection", icon = "TRIA_LEFT_BAR")

        pie.operator("node.align_right_side_selection_nodes", text = "Selection", icon = "TRIA_RIGHT_BAR")
