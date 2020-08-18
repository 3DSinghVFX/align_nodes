import bpy

addon_keymaps = []

def register():
    if not canRegisterKeymaps(): return

    wm = bpy.context.window_manager
    km = wm.keyconfigs.addon.keymaps.new(name = "Node Editor", space_type = "NODE_EDITOR")

    # Align Pie Menu
    kmi = km.keymap_items.new("wm.call_menu_pie", type = "E", value = "PRESS", ctrl = True)
    kmi.properties.name = "APN_MT_align_pie"

    addon_keymaps.append(km)

def unregister():
    if not canRegisterKeymaps(): return

    wm = bpy.context.window_manager
    for km in addon_keymaps:
        for kmi in km.keymap_items:
            km.keymap_items.remove(kmi)
        wm.keyconfigs.addon.keymaps.remove(km)
    addon_keymaps.clear()

def canRegisterKeymaps():
    return not bpy.app.background
