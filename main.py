# import sys
# from PyQt6.QtWidgets import QApplication, QWidget, QSplashScreen, QMainWindow
#
# from views.ai_pad_view import AIPadView
# from views.basic_pad_view import BasicPadView
# from views.control_view import ControlView
# from views.face_control_view import FaceControlView
# from views.hand_control_view import HandControlView
# from views.home_view import HomeView
# from PyQt6.QtGui import QPixmap
# from PyQt6.QtCore import Qt
# import time
#
# from views.virtual_pad_view import VirtualPadView

import sys
from PyQt6.QtWidgets import QApplication, QWidget, QSplashScreen, QMainWindow, QStackedWidget
from views.control_view import ControlView
from views.hand_control_view import HandControlView
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt
import time


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Control View")
        self.setGeometry(100, 100, 1200, 800)  # تعديل الحجم حسب احتياجك
        self.showMaximized()  # تكبير النافذة لتملأ الشاشة

        # إنشاء StackedWidget للتنقل بين الصفحات
        self.stacked_widget = QStackedWidget()
        self.setCentralWidget(self.stacked_widget)

        # إنشاء الصفحات
        self.control_view = ControlView(self)
        self.hand_control_view = HandControlView(self)

        # إضافة الصفحات إلى StackedWidget
        self.stacked_widget.addWidget(self.control_view)
        self.stacked_widget.addWidget(self.hand_control_view)

    def navigate_to_hand_control(self):
        self.stacked_widget.setCurrentWidget(self.hand_control_view)
        self.setWindowTitle("Hand Control View")  # تحديث العنوان

    def navigate_to_control(self):
        self.stacked_widget.setCurrentWidget(self.control_view)
        self.setWindowTitle("Control View")  # تحديث العنوان

    def navigate_to_page(self, index):
        self.stacked_widget.setCurrentIndex(index)
        if index == 0:
            self.setWindowTitle("Control View")  # تحديث العنوان
        elif index == 1:
            self.setWindowTitle("Hand Control View")  # تحديث العنوان


def main():
    app = QApplication(sys.argv)

    # Splash Screen
    pixmap = QPixmap("images/splash.png")
    splash = QSplashScreen(pixmap)
    splash.setWindowFlag(Qt.WindowType.FramelessWindowHint)  # remove frame
    splash.show()

    splash.showMessage("Loading resources...", Qt.AlignmentFlag.AlignBottom | Qt.AlignmentFlag.AlignCenter,
                       Qt.GlobalColor.white)
    time.sleep(3)

    # home_view_window = HomeView()
    # home_view_window.show()
    # splash.finish(home_view_window) # close splash
    main_window = MainWindow()
    main_window.show()
    splash.finish(main_window)


    sys.exit(app.exec())

if __name__ == "__main__":
    main()
