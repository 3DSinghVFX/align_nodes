import bpy

class SnapPieMenu(bpy.types.Menu):
    bl_idname = "SPN_MT_snap_pie"
    bl_label = "Snap Pie"

    def draw(self, context):
        layout = self.layout
        pie = layout.menu_pie()

        pie = pie.row()
        pie.label(text = "")
        pie = layout.menu_pie()

        pie = pie.row()
        pie.label(text = "")
        pie = layout.menu_pie()

        pie.operator("node.snap_width_center_selection_nodes", text = "Snap Width", icon = "ALIGN_CENTER")

        pie.operator("node.snap_height_center_selection_nodes", text = "Snap Height", icon = "ALIGN_MIDDLE")

        pie.operator("node.snap_bottom_side_selection_nodes", text = "Snap Bottom", icon = "ALIGN_BOTTOM")

        pie.operator("node.snap_top_side_selection_nodes", text = "Snap Top", icon = "ALIGN_TOP")

        pie.operator("node.snap_left_side_selection_nodes", text = "Snap Left", icon = "ALIGN_LEFT")

        pie.operator("node.snap_right_side_selection_nodes", text = "Snap Right", icon = "ALIGN_RIGHT")
