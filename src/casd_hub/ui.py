from PyQt6.QtCore import Qt, QSize, QEvent
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QGridLayout, QPushButton, QGroupBox
from PyQt6.QtGui import QIcon, QPixmap, QFont, QPalette, QColor, QCursor
from importlib import resources
import tomllib

from casd_hub.resources import get_icon_path

class ClickableWidget(QWidget):
    """Custom QWidget that acts like a button, with a QGroupBox containing an icon and text."""
    def __init__(self, icon_path, text, callback):
        super().__init__()
        self.setFixedSize(120, 120)  # Adjust size to fit content

        # Styles
        self.default_style = """
            QGroupBox {
                background-color: white;
                border: 2px solid #cccccc;
                border-radius: 10px;
            }
        """
        self.hover_style = """
            QGroupBox {
                background-color: #e0e0e0;
                border: 2px solid #999999;
                border-radius: 10px;
            }
        """
        self.clicked_style = """
            QGroupBox {
                background-color: #b3e5fc;
                border: 2px solid #666666;
                border-radius: 10px;
            }
        """

        self.layout = QVBoxLayout(self)

        # GroupBox (contains icon + text)
        self.group_box = QGroupBox()
        self.group_box.setStyleSheet(self.default_style)
        self.group_box_layout = QVBoxLayout(self.group_box)
        self.group_box_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Icon
        self.icon_label = QLabel(self)
        pixmap = QPixmap(icon_path).scaled(50, 50, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)
        self.icon_label.setPixmap(pixmap)
        self.icon_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.group_box_layout.addWidget(self.icon_label)

        # Text
        self.text_label = QLabel(text, self)
        self.text_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.text_label.setFont(QFont("Arial", 10))
        self.group_box_layout.addWidget(self.text_label)

        self.layout.addWidget(self.group_box)

        # Set cursor
        self.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        # Event handling
        self.mousePressEvent = lambda event: self.on_click(callback)
        self.enterEvent = self.on_hover
        self.leaveEvent = self.on_leave

    def on_click(self, callback):
        """Change background color on click and trigger callback"""
        self.group_box.setStyleSheet(self.clicked_style)
        callback()

    def on_hover(self, event: QEvent):
        """Change background color when hovered"""
        self.group_box.setStyleSheet(self.hover_style)

    def on_leave(self, event: QEvent):
        """Revert background color when mouse leaves"""
        self.group_box.setStyleSheet(self.default_style)

class SecureHubWidget(QWidget):
    def __init__(self):
        super().__init__()
        # get config
        _cfg = tomllib.loads(resources.read_text("casd_hub.conf", "config.toml"))

        self.setWindowTitle(str(_cfg.get("ui")["app_title"]))
        self.setGeometry(100, 100, 800, 600)

        # Create a vertical layout for the main window
        self.layout = QVBoxLayout()
        # center the items
        self.layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # add casd main logo
        casd_logo_path = get_icon_path("casd.svg")  # Replace with your logo file
        self.logo_label = QLabel(self)
        self.logo_pixmap = QPixmap(casd_logo_path).scaled(600, 120)
        self.logo_label.setPixmap(self.logo_pixmap)
        self.logo_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.layout.addWidget(self.logo_label)

        # add casd welcome below the logo
        self.logo_text_label = QLabel("Welcome to the CASD Secure HUB", self)
        # change font size
        casd_welcome_font = QFont("Arial", 18)  # Set font size (14pt)
        self.logo_text_label.setFont(casd_welcome_font)
        # change text color
        palette = self.logo_text_label.palette()
        palette.setColor(QPalette.ColorRole.WindowText, QColor("grey"))  # Set text color to grey
        self.logo_text_label.setPalette(palette)
        # change text alignment
        self.logo_text_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.layout.addWidget(self.logo_text_label)


        # Create a grid layout for icons
        self.icon_layout = QGridLayout()
        server_icon_path = get_icon_path("server.png")
        # Icons and associated texts
        self.icons = {
            "icon1": {"path": server_icon_path, "text": "Server 1"},
            "icon2": {"path": server_icon_path, "text": "Server 2"},
            "icon3": {"path": server_icon_path, "text": "Server 3"},
            "icon4": {"path": server_icon_path, "text": "Server 4"},
        }

        # Create buttons with icons
        row, col = 0, 0
        for icon_key, icon_info in self.icons.items():
            icon_path = icon_info.get("path")
            icon_text = icon_info.get("text")
            button = ClickableWidget(icon_path, icon_text, lambda key=icon_key: self.show_text(key))
            self.icon_layout.addWidget(button, row, col)
            col += 1
            if col > 3:
                col = 0
                row += 1

        # Add the grid layout with icons to the main layout
        self.layout.addLayout(self.icon_layout)

        # add output label
        # Add a label to display text associated with the icon
        self.output_label = QLabel("Select the sever which you want to connect", self)
        # set font
        output_font = QFont("Arial", 12)  # Set font size (14pt)
        self.output_label.setFont(output_font)
        self.output_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.layout.addWidget(self.output_label)

        # Set the main layout of the window
        self.setLayout(self.layout)

    def show_text(self, icon_key:str):
        """Update the label with the text associated with the clicked icon"""
        serer_id:str = self.icons[icon_key]["text"]
        self.output_label.setText(f"Connecto to server: {serer_id}")

