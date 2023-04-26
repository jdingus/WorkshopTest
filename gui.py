import sys
import json
import logging
import threading
from PyQt5.QtGui import QStandardItem, QStandardItemModel
from PyQt5.QtCore import QModelIndex
from PyQt5.QtWidgets import QApplication, QTreeView, QWidget, QVBoxLayout, QAbstractItemView, QLabel

app = QApplication(sys.argv)

model = QStandardItemModel()
model.setHorizontalHeaderLabels(["Topic", "Payload"])

tree_view = QTreeView()
tree_view.setModel(model)
tree_view.setSelectionMode(QAbstractItemView.SingleSelection)
tree_view.setAnimated(True)

main_window = QWidget()
layout = QVBoxLayout()
layout.addWidget(tree_view)

selected_topic_value = QLabel("Selected Topic Value: None")
layout.addWidget(selected_topic_value)

main_window.setLayout(layout)
main_window.show()

def on_tree_view_item_clicked(index):
    payload_index = model.index(index.row(), 1, index.parent())
    payload = payload_index.data()
    selected_topic_value.setText(f"Selected Topic Value: {payload}")

tree_view.clicked.connect(on_tree_view_item_clicked)

gui_update_lock = threading.Lock()
logging.info(json.dumps({"object_created": "threading.Lock", "name": "gui_update_lock"}))

def find_or_create_item(model, current_item, value):
    for row in range(current_item.rowCount()):
        if current_item.child(row).data() == value:
            return current_item.child(row)

    new_item = QStandardItem(value)
    current_item.appendRow(new_item)
    logging.info(json.dumps({"object_created": "QStandardItem", "value": value}))
    return new_item

def update_gui(topic, payload):
    with gui_update_lock:
        levels = topic.split("/")
        root_item = model.invisibleRootItem()
        current_item = root_item

        for level_index, level in enumerate(levels):
            current_item = find_or_create_item(model, current_item, level)

            if level_index == len(levels) - 1:
                found = False
                for row in range(current_item.rowCount()):
                    if current_item.child(row, 0).data() == levels[-1]:
                        current_item.child(row, 1).setData(payload, 0)
                        found = True
                        break

                if not found:
                    current_item.appendRow([QStandardItem(levels[-1]), QStandardItem(payload)])
