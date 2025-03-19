import sys

from PyQt6.QtWidgets import QApplication
from casd_hub.ui import SecureHubWidget


def main():
    app = QApplication(sys.argv)
    window = SecureHubWidget()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()