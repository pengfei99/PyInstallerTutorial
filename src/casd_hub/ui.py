from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QGridLayout, QPushButton
from PyQt6.QtGui import QIcon
from importlib import resources
import tomllib

class IconApp(QWidget):
    def __init__(self):
        super().__init__()
        # get config
        _cfg = tomllib.loads(resources.read_text("casd_hub.conf", "config.toml"))

        self.setWindowTitle(str(_cfg.get("ui")["app_title"]))
        self.setGeometry(100, 100, 400, 300)

        # Create a vertical layout for the main window
        self.layout = QVBoxLayout()

        # Add a label to display text associated with the icon
        self.label = QLabel("Click on an icon", self)
        self.layout.addWidget(self.label)

        # Create a grid layout for icons
        self.icon_layout = QGridLayout()

        # Icons and associated texts
        self.icons = {
            "icon1": {"icon": "path_to_icon1.png", "text": "This is Icon 1"},
            "icon2": {"icon": "path_to_icon2.png", "text": "This is Icon 2"},
            "icon3": {"icon": "path_to_icon3.png", "text": "This is Icon 3"},
            "icon4": {"icon": "path_to_icon4.png", "text": "This is Icon 4"},
        }

        # Create buttons with icons
        row, col = 0, 0
        for icon_key, icon_info in self.icons.items():
            button = QPushButton(QIcon(icon_info["icon"]), "")
            button.clicked.connect(lambda checked, key=icon_key: self.show_text(key))
            self.icon_layout.addWidget(button, row, col)
            col += 1
            if col > 2:
                col = 0
                row += 1

        # Add the grid layout with icons to the main layout
        self.layout.addLayout(self.icon_layout)

        # Set the main layout of the window
        self.setLayout(self.layout)

    def show_text(self, icon_key):
        """Update the label with the text associated with the clicked icon"""
        self.label.setText(self.icons[icon_key]["text"])


