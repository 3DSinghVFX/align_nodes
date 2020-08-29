import bpy
from mathutils import Vector

class NodeOperator:
    @classmethod
    def poll(cls, context):
        tree = context.space_data.node_tree
        if tree is None: return False
        if tree.nodes.active is None: return False
        return True

class SnapBottomSideSelectionNodes(bpy.types.Operator, NodeOperator):
    bl_idname = "node.snap_bottom_side_selection_nodes"
    bl_label = "Snap Bottom Side Selection Nodes"
    bl_description = "Snaps the bottom of all selected nodes w.r.t active node"

    def execute(self, context):
        activeNode = context.active_node
        selectedNodes = context.selected_nodes
        if activeNode not in selectedNodes: return {"FINISHED"}

        activeLocation = activeNode.location
        activeDimensions = activeNode.dimensions
        for node in selectedNodes:
            if node != activeNode:
                node.location.y = activeLocation.y + (node.dimensions.y - activeDimensions.y)
        return {"FINISHED"}

class SnapTopSideSelectionNodes(bpy.types.Operator, NodeOperator):
    bl_idname = "node.snap_top_side_selection_nodes"
    bl_label = "Snap Top Side Selection Nodes"
    bl_description = "Snaps the top of all selected nodes w.r.t active node"

    def execute(self, context):
        activeNode = context.active_node
        selectedNodes = context.selected_nodes
        if activeNode not in selectedNodes: return {"FINISHED"}

        activeLocation = activeNode.location
        for node in selectedNodes:
            if node != activeNode:
                node.location.y = activeLocation.y
        return {"FINISHED"}

class SnapRightSideSelectionNodes(bpy.types.Operator, NodeOperator):
    bl_idname = "node.snap_right_side_selection_nodes"
    bl_label = "Snap Right Side Selection Nodes"
    bl_description = "Snaps the right side of all selected nodes w.r.t active node"

    def execute(self, context):
        activeNode = context.active_node
        selectedNodes = context.selected_nodes
        if activeNode not in selectedNodes: return {"FINISHED"}

        xOffset = activeNode.location.x + activeNode.width
        for node in selectedNodes:
            if node != activeNode:
                node.location.x = xOffset - node.width
        return {"FINISHED"}

class SnapLeftSideSelectionNodes(bpy.types.Operator, NodeOperator):
    bl_idname = "node.snap_left_side_selection_nodes"
    bl_label = "Snap Left Side Selection Nodes"
    bl_description = "Snaps the left side of all selected nodes w.r.t active node"

    def execute(self, context):
        activeNode = context.active_node
        selectedNodes = context.selected_nodes
        if activeNode not in selectedNodes: return {"FINISHED"}

        activeLocation = activeNode.location
        for node in selectedNodes:
            if node != activeNode:
                node.location.x = activeLocation.x
        return {"FINISHED"}

class SnapHeightCenterSideSelectionNodes(bpy.types.Operator, NodeOperator):
    bl_idname = "node.snap_height_center_selection_nodes"
    bl_label = "Snap Height Center Side Selection Nodes"
    bl_description = "Snaps the height center of all selected nodes w.r.t active node"

    def execute(self, context):
        activeNode = context.active_node
        selectedNodes = context.selected_nodes
        if activeNode not in selectedNodes: return {"FINISHED"}

        yOffset = activeNode.location.y - activeNode.dimensions.y / 2
        for node in selectedNodes:
            if node != activeNode:
                node.location.y = yOffset + node.dimensions.y / 2
        return {"FINISHED"}

class SnapWidthCenterSideSelectionNodes(bpy.types.Operator, NodeOperator):
    bl_idname = "node.snap_width_center_selection_nodes"
    bl_label = "Snap Width Center Side Selection Nodes"
    bl_description = "Snaps the width center of all selected nodes w.r.t active node"

    def execute(self, context):
        activeNode = context.active_node
        selectedNodes = context.selected_nodes
        if activeNode not in selectedNodes: return {"FINISHED"}

        xOffset = activeNode.location.x + activeNode.width / 2
        for node in selectedNodes:
            if node != activeNode:

                node.location.x = xOffset - node.width / 2
        return {"FINISHED"}
