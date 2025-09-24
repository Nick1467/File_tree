import sys
import os
from PyQt5.QtWidgets import QApplication, QMainWindow, QGraphicsScene, QGraphicsView, QGraphicsEllipseItem, QGraphicsTextItem
from PyQt5.QtCore import Qt, QRectF, QPointF


class Node(QGraphicsEllipseItem):
    def __init__(self, path, radius=40):
        super().__init__(-radius / 2, -radius / 2, radius, radius)
        self.setBrush(Qt.lightGray)
        self.setFlag(QGraphicsEllipseItem.ItemIsSelectable)
        self.setFlag(QGraphicsEllipseItem.ItemIsMovable)
        self.path = path
        self.label = QGraphicsTextItem(os.path.basename(path) or path, self)
        self.label.setDefaultTextColor(Qt.black)
        self.label.setPos(-self.label.boundingRect().width() / 2, -radius)
        self.children_loaded = False


class MindMap(QMainWindow):
    def __init__(self, root_path):
        super().__init__()
        self.setWindowTitle("Mind Map Style Directory Tree")
        self.setGeometry(100, 100, 1000, 800)

        self.scene = QGraphicsScene()
        self.view = QGraphicsView(self.scene, self)
        self.setCentralWidget(self.view)

        # Create root node
        self.root_node = Node(root_path)
        self.scene.addItem(self.root_node)
        self.root_node.setPos(0, 0)

        # Mouse click detection
        self.scene.mousePressEvent = self.on_click

    def on_click(self, event):
        item = self.scene.itemAt(event.scenePos(), self.view.transform())
        if isinstance(item, Node):
            if not item.children_loaded:
                self.expand_node(item)
                item.children_loaded = True
        super(QGraphicsScene, self.scene).mousePressEvent(event)

    def expand_node(self, node):
        try:
            children = [c for c in os.listdir(node.path) if os.path.isdir(os.path.join(node.path, c))]
        except PermissionError:
            children = []

        angle_step = 360 / max(1, len(children))
        radius = 150

        for i, child in enumerate(children):
            angle = i * angle_step
            dx = radius * (Qt.cos(angle * 3.14159 / 180))
            dy = radius * (Qt.sin(angle * 3.14159 / 180))

            child_path = os.path.join(node.path, child)
            child_node = Node(child_path)
            self.scene.addItem(child_node)
            child_node.setPos(node.pos() + QPointF(dx, dy))

            # Draw line
            line = self.scene.addLine(node.pos().x(), node.pos().y(),
                                      child_node.pos().x(), child_node.pos().y())
            line.setZValue(-1)  # Put line behind nodes


if __name__ == "__main__":
    app = QApplication(sys.argv)

    folder = os.path.expanduser("~")  # default to home directory
    window = MindMap(folder)
    window.show()
    sys.exit(app.exec_())