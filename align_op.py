import bpy
from mathutils import Vector
from . preferences import getAlignPieMenuSettings

class NodeOperator:
    @classmethod
    def poll(cls, context):
        tree = context.space_data.node_tree
        if tree is None: return False
        if tree.nodes.active is None: return False
        return True

class AlignDependentNodes(bpy.types.Operator, NodeOperator):
    bl_idname = "node.align_dependent_nodes"
    bl_label = "Align Dependent Nodes"
    bl_description = "Aligns all dependent nodes w.r.t active node to its right side"

    def execute(self, context):
        offset = getAlignPieMenuSettings().offsetHorizontal
        activeNode = context.active_node
        alignDependent(offset, getNodesWhenFollowingBranchedLinks(activeNode, followOutputs = True))
        return {"FINISHED"}

def alignDependent(offset, nodes):
    activeNode = nodes[0]
    lastNode = activeNode
    for node in nodes[1:]:
        if type(node) == list:
            alignDependent(offset, node)
        else:
            if node.type != 'REROUTE':
                if lastNode.type == 'REROUTE':
                    location = node.location.copy()
                else:
                    location = lastNode.location.copy()
                    node.location = location + Vector((lastNode.width + offset, 0))
            lastNode = node

class AlignDependenciesNodes(bpy.types.Operator, NodeOperator):
    bl_idname = "node.align_dependencies"
    bl_label = "Align Dependencies"
    bl_description = "Aligns all dependencies nodes w.r.t active node to its left side"

    def execute(self, context):
        offset = getAlignPieMenuSettings().offsetHorizontal
        activeNode = context.active_node
        alignDependencies(offset, getNodesWhenFollowingBranchedLinks(activeNode, followInputs = True))
        return {"FINISHED"}

def alignDependencies(offset, nodes):
    activeNode = nodes[0]
    lastNode = activeNode
    for node in nodes[1:]:
        if type(node) == list:
            alignDependencies(offset, node)
        else:
            if node.type != 'REROUTE':
                if lastNode.type == 'REROUTE':
                    location = node.location.copy()
                else:
                    location = lastNode.location.copy()
                    node.location = location + Vector((- node.width - offset, 0))
            lastNode = node

class StakeUpSelectionNodes(bpy.types.Operator, NodeOperator):
    bl_idname = "node.stake_up_selection_nodes"
    bl_label = "Stake Up Selection Nodes"
    bl_description = "Stacks up all selected nodes w.r.t active node"

    def execute(self, context):
        offset = getAlignPieMenuSettings().offsetVertical
        activeNode = context.active_node
        selectedNodes = context.selected_nodes
        if activeNode not in selectedNodes: return {"FINISHED"}

        previousNode = activeNode
        for node in selectedNodes:
            if node != activeNode:
                node.location = getStakeUpNodeLocation(previousNode, node, offset)
                previousNode = node
        return {"FINISHED"}

def getStakeUpNodeLocation(previousNode, node, offset):
    location = previousNode.location.copy()
    if node.type == "REROUTE":
        location.y += offset
        return location
    location.y += node.dimensions.y + offset
    return location

class StakeDownSelectionNodes(bpy.types.Operator, NodeOperator):
    bl_idname = "node.stake_down_selection_nodes"
    bl_label = "Stake Down Selection Nodes"
    bl_description = "Stacks down all selected nodes w.r.t active node"

    def execute(self, context):
        offset = getAlignPieMenuSettings().offsetVertical
        activeNode = context.active_node
        selectedNodes = context.selected_nodes
        if activeNode not in selectedNodes: return {"FINISHED"}

        previousNode = activeNode
        for node in selectedNodes:
            if node != activeNode:
                node.location = getStakeDownNodeLocation(previousNode, offset)
                previousNode = node
        return {"FINISHED"}

def getStakeDownNodeLocation(previousNode, offset):
    location = previousNode.location.copy()
    if previousNode.type == "REROUTE":
        location.y -= offset
        return location
    location.y -= previousNode.dimensions.y + offset
    return location

class AlignTopSelectionNodes(bpy.types.Operator, NodeOperator):
    bl_idname = "node.align_top_selection_nodes"
    bl_label = "Align Top Selection Nodes"
    bl_description = "Aligns only the header of all selected nodes w.r.t active node"

    def execute(self, context):
        activeNode = context.active_node
        selectedNodes = context.selected_nodes
        if activeNode not in selectedNodes: return {"FINISHED"}

        previousNode = activeNode
        for node in selectedNodes:
            if node != activeNode:
                node.location.y = previousNode.location.y
                previousNode = node
        return {"FINISHED"}

class AlignRightSideSelectionNodes(bpy.types.Operator, NodeOperator):
    bl_idname = "node.align_right_side_selection_nodes"
    bl_label = "Align Right Side Selection Nodes"
    bl_description = "Aligns only the side of all selected nodes w.r.t active node to its right side"

    def execute(self, context):
        offset = getAlignPieMenuSettings().offsetHorizontal
        activeNode = context.active_node
        selectedNodes = context.selected_nodes
        if activeNode not in selectedNodes: return {"FINISHED"}

        previousNode = activeNode
        for node in selectedNodes:
            if node != activeNode:
                node.location.x = getRightOffsetForNode(previousNode, offset)
                previousNode = node
        return {"FINISHED"}

def getRightOffsetForNode(previousNode, offset):
    if previousNode.type == "REROUTE":
        return previousNode.location.x + offset
    return previousNode.location.x + previousNode.width + offset

class AlignLeftSideSelectionNodes(bpy.types.Operator, NodeOperator):
    bl_idname = "node.align_left_side_selection_nodes"
    bl_label = "Align Left Side Selection Nodes"
    bl_description = "Aligns only the side of all selected nodes w.r.t active node to its left side"

    def execute(self, context):
        offset = getAlignPieMenuSettings().offsetHorizontal
        activeNode = context.active_node
        selectedNodes = context.selected_nodes
        if activeNode not in selectedNodes: return {"FINISHED"}

        previousNode = activeNode
        for node in selectedNodes:
            if node != activeNode:
                node.location.x = getLeftOffsetForNode(previousNode, node, offset)
                previousNode = node
        return {"FINISHED"}

def getLeftOffsetForNode(previousNode, node, offset):
    if node.type == "REROUTE":
        return previousNode.location.x - offset
    return previousNode.location.x - (node.width + offset)

def getNodesWhenFollowingBranchedLinks(startNode, followInputs = False, followOutputs = False):
    nodes = []
    nodesToCheck = {startNode}
    while nodesToCheck:
        node = nodesToCheck.pop()
        nodes.append(node)
        sockets = []
        if followInputs:
            sockets.extend(node.inputs)
            nodesLinked = getLinkedDependenciesNodes(sockets)
        if followOutputs:
            sockets.extend(node.outputs)
            nodesLinked = getLinkedDependentNodes(sockets)
        if len(nodesLinked) > 1:
            for node in nodesLinked:
                nodes.append(getNodesWhenFollowingBranchedLinks(node, followInputs, followOutputs))
        else:
            for node in nodesLinked:
                if node not in nodes: nodesToCheck.add(node)
    return nodes

def getLinkedDependenciesNodes(sockets):
    nodesLinked = []
    for socket in sockets:
        for linkedSocket in getDirectlyLinkedSocketsToInput(socket):
            node = linkedSocket.node
            if node not in nodesLinked: nodesLinked.append(node)
    return nodesLinked

def getLinkedDependentNodes(sockets):
    nodesLinked = []
    for socket in sockets:
        for linkedSocket in getDirectlyLinkedSocketsToOutput(socket):
            node = linkedSocket.node
            if node not in nodesLinked: nodesLinked.append(node)
    return nodesLinked

def getDirectlyLinkedSocketsToInput(socket):
    links = socket.links
    return [link.from_socket for link in links]

def getDirectlyLinkedSocketsToOutput(socket):
    links = socket.links
    return [link.to_socket for link in links]
