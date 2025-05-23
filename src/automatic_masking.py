# automatic_masking.py is discontinued because corresponding functionality now included in Metashape.
# Please, instead:
# 1) Select photos in Workspace or in Photos pane
# 2) Mouse right-click on them -> Masks -> Generate Masks...
# 3) Method: Automatic (AI)

import Metashape
from PySide2 import QtWidgets

# Checking compatibility
compatible_major_version = "2.2"
found_major_version = ".".join(Metashape.app.version.split('.')[:2])
if found_major_version != compatible_major_version:
    raise Exception("Incompatible Metashape version: {} != {}".format(found_major_version, compatible_major_version))

def generate_automatic_background_masks_with_rembg():
    app = QtWidgets.QApplication.instance()
    parent = app.activeWindow()

    dialog = QtWidgets.QDialog(parent)
    dialog.setWindowTitle("Error")
    layout = QtWidgets.QVBoxLayout(dialog)

    label = QtWidgets.QLabel(
        "automatic_masking.py is discontinued because corresponding functionality now included in Metashape 2.2.<br>"
        "Please, instead:<br>"
        "1) Select photos in Workspace or in Photos pane<br>"
        "2) <b>Mouse Right-Click on them->Masks->Generate Masks...</b><br>"
        "3) Method: Automatic (AI)"
    )
    label.setWordWrap(False)
    layout.addWidget(label)

    button = QtWidgets.QPushButton("OK")
    button.clicked.connect(dialog.accept)
    layout.addWidget(button)

    dialog.exec()

label = "Scripts/[DISCONTINUED] Automatic background masking"
Metashape.app.addMenuItem(label, generate_automatic_background_masks_with_rembg)
print("To execute this script press {}".format(label))
