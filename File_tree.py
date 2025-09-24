import sys
import os
from PyQt5.QtWidgets import QApplication, QMainWindow, QTreeView, QFileSystemModel, QMenu, QFileDialog
from PyQt5.QtCore import QDir
from PyQt5.QtGui import QCursor, QClipboard


class FileTree(QMainWindow):
    def __init__(self, root_path):
        super().__init__()
        self.setWindowTitle("Lazy Loading Directory Tree")
        self.setGeometry(100, 100, 800, 600)

        # Set up model
        self.model = QFileSystemModel()
        self.model.setRootPath(root_path)
        self.model.setFilter(QDir.AllDirs | QDir.NoDotAndDotDot)

        # Set up tree view
        self.tree = QTreeView(self)
        self.tree.setModel(self.model)
        self.tree.setRootIndex(self.model.index(root_path))
        self.tree.setColumnHidden(1, True)  # Hide Size column
        self.tree.setColumnHidden(2, True)  # Hide Type column
        self.tree.setColumnHidden(3, True)  # Hide Date Modified column
        self.tree.setContextMenuPolicy(3)   # Enable custom context menu

        self.setCentralWidget(self.tree)

        # Connect context menu
        self.tree.customContextMenuRequested.connect(self.open_menu)

    def open_menu(self, position):
        index = self.tree.indexAt(position)
        if not index.isValid():
            return

        menu = QMenu()
        copy_action = menu.addAction("Copy Path")
        action = menu.exec_(QCursor.pos())

        if action == copy_action:
            path = self.model.filePath(index)
            clipboard = QApplication.clipboard()
            clipboard.setText(path)
            print("Copied path:", path)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    # Open folder selection dialog instead of asking for input
    folder = QFileDialog.getExistingDirectory(None, "Select Root Folder", os.path.expanduser("~"))
    if not folder:
        print("No folder selected.")
        sys.exit(0)

    window = FileTree(folder)
    window.show()
    sys.exit(app.exec_())