import sys
from PyQt6.QtWidgets import QApplication, QWidget, QSplashScreen, QMainWindow

from views.control_view import ControlView
from views.face_control_view import FaceControlView
from views.home_view import HomeView
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt
import time

def main():
    app = QApplication(sys.argv)

    # Splash Screen
    pixmap = QPixmap("images/splash.png")
    splash = QSplashScreen(pixmap)
    splash.setWindowFlag(Qt.WindowType.FramelessWindowHint)  # remove frame
    splash.show()

    time.sleep(3)

    splash.showMessage("Loading resources...", Qt.AlignmentFlag.AlignBottom | Qt.AlignmentFlag.AlignCenter,
                       Qt.GlobalColor.white)

    home_view_window = FaceControlView()
    home_view_window.show()

    splash.finish(home_view_window) # close splash

    sys.exit(app.exec())

if __name__ == "__main__":
    main()
