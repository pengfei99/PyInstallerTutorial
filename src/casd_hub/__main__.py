import sys

from PyQt6.QtWidgets import QApplication

from casd_secure_hub.main_widget import IconApp

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = IconApp()
    window.show()
    sys.exit(app.exec())