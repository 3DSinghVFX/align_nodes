# Align Nodes
![](./align_pie_img.png?raw=true "Align Pie menu") ![](./snap_pie_img.png?raw=true "Snap Pie menu")

This tool allows to align the nodes in any nodes editor *e.g., Shader Nodes Editor, Compositing Nodes Editor, Simulation Editor, Animation Nodes Editor, Sverchok Nodes Editor*.

**Installation:**
- Download the zip file [Align Nodes](https://github.com/3DSinghVFX/align_nodes/archive/master.zip) add-on.
- Open the Blender, go to `Edit -> Preferences -> Add-ons`.
- Press the `Install` button, locate the zip file of *Align Nodes* add-on, install it.

**How to Use Align Pie:**
- Press the shortcut key `Shift + E` in any node-editor, an *Align Pie* menu will pop up.
- The *Align Pie* menu has eight nodes alignment operations:
  - *Dependent (Right)* - Aligns all dependent nodes w.r.t active node to its right side.
  - *Dependencies (Left)* - Aligns all dependencies nodes w.r.t active node to its left side.
  - *Selection (Top)* - Stacks up all selected nodes w.r.t active node.
  - *Selection (Bottom)* - Stacks down all selected nodes w.r.t active node.
  - *Selection (Top Right)* - Aligns only the header of all selected nodes w.r.t active node.
  - *Selection (Top Left)* - Aligns only the header of all selected nodes w.r.t active node.
  - *Selection (Bottom Right)* - Aligns only the side of all selected nodes w.r.t active node to its right side.
  - *Selection (Bottom Left)* - Aligns only the side of all selected nodes w.r.t active node to its left side.
- You can change the default *Horizontal Offset* (side distance between nodes) and *Vertical Offset* (height distance between nodes) from the preferences of the add-on.

**How to Use Snap Pie:**
- Press the shortcut key `Shift + Q` in any node-editor, an *Snap Pie* menu will pop up.
- The *Snap Pie* menu has six nodes snaps operations:
  - *Snap Bottom (Top Left)* - Snaps the bottom of all selected nodes w.r.t active node.
  - *Snap Height (Top)* - Snaps the height center of all selected nodes w.r.t active node.
  - *Snap Top (Top Right)* - Snaps the top of all selected nodes w.r.t active node.
  - *Snap Left (Left)* - Snaps the left side of all selected nodes w.r.t active node.
  - *Snap Width (Bottom)* - Snaps the width center of all selected nodes w.r.t active node.
  - *Snap Right (Right)* - Snaps the right side of all selected nodes w.r.t active node.
