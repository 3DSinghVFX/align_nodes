import bpy
from . import keymap
from . snap_op import *
from . align_op import *
from . snap_pie_mt import *
from . preferences import *
from . align_pie_mt import *
from . import preferences

ordered_classes = [AlignPieMenuProperties, AlignNodesPreferences, AlignPieMenu, SnapPieMenu,
                   AlignDependentNodes, AlignDependenciesNodes, StakeUpSelectionNodes,
                   StakeDownSelectionNodes, AlignTopSelectionNodes, AlignRightSideSelectionNodes,
                   AlignLeftSideSelectionNodes, SnapBottomSideSelectionNodes, SnapTopSideSelectionNodes,
                   SnapRightSideSelectionNodes, SnapLeftSideSelectionNodes, SnapHeightCenterSideSelectionNodes,
                   SnapWidthCenterSideSelectionNodes]
module = keymap

def register():
    for cls in ordered_classes:
        bpy.utils.register_class(cls)

    bpy.types.AddonPreferences.alignPieMenuProp = bpy.props.PointerProperty(type = AlignPieMenuProperties)

    if module.__name__ == __name__:
            pass
    if hasattr(module, "register"):
        module.register()

def unregister():
    del bpy.types.AddonPreferences.alignPieMenuProp

    for cls in reversed(ordered_classes):
        bpy.utils.unregister_class(cls)

    if module.__name__ == __name__:
            pass
    if hasattr(module, "unregister"):
        module.unregister()

if __name__ == "__main__":
    register()
