from utils.libraries import *

class HomeView(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__()
        self.parent = parent

        # Add first image (base image)
        self.image_label1 = QtWidgets.QLabel(self)
        pixmap1 = QtGui.QPixmap("images/Rectangle_home.png")
        if pixmap1.isNull():
            print("Image 1 failed to load! Check the path.")
        else:
            self.image_label1.setPixmap(pixmap1.scaled(500, 600, QtCore.Qt.AspectRatioMode.KeepAspectRatio,
                                                       QtCore.Qt.TransformationMode.SmoothTransformation))
            self.image_label1.move(300, 0)  # Position the first image

        # Add second image to overlay on top of the first image
        self.image_label2 = QtWidgets.QLabel(self)
        pixmap2 = QtGui.QPixmap("images/home.png")
        if pixmap2.isNull():
            print("Image 2 failed to load! Check the path.")
        else:
            self.image_label2.setPixmap(pixmap2.scaled(450, 450, QtCore.Qt.AspectRatioMode.KeepAspectRatio,
                                                       QtCore.Qt.TransformationMode.SmoothTransformation))
            self.image_label2.move(310, 150)  # Adjust position for overlay

        # Add title label
        self.title_label = QtWidgets.QLabel("BE MY ARM", self)
        self.title_label.setStyleSheet("font-size: 70px; font-weight: bold; color: white;")
        self.title_label.move(700, 200)  # Adjust position for title


        # Add vertical line beside the title
        self.vertical_line = QtWidgets.QLabel(self)
        self.vertical_line.setFixedWidth(15)  # Width of the line
        self.vertical_line.setFixedHeight(50)  # Height of the line
        self.vertical_line.setStyleSheet("background-color: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1, "
                                         "stop:0.3 #151b58, stop:0.5 #C1D3F5, stop:0.6 #151b58);")  # Color of the line
        self.vertical_line.move(1080, 200)  # Positioning it beside the title (adjust as necessary)



        # Add subtitle label with manual line breaks
        self.subtitle_label = QtWidgets.QLabel("Together, we make technology work for you\n\n"
                                               "supporting your independence and bringing you\n\n comfort at every step.", self)
        self.subtitle_label.setWordWrap(True)
        self.subtitle_label.setStyleSheet \
            ("font-size: 15px; color: white; padding-top: 5px;")  # Add padding-top for spacing
        self.subtitle_label.move(770, 300)  # Adjust position for subtitle


        # Add line beside the subtitle
        self.subtitle_line = QLabel(self)
        self.subtitle_line.setStyleSheet("background-color: white;")
        self.subtitle_line.setFixedHeight(2)
        self.subtitle_line.setFixedWidth(50)
        self.subtitle_line.move(700, 330)


        # Initialize variables for animation
        self.angle = 0  # Angle for orbiting circles
        self.num_circles = 5  # Number of circles to draw
        self.base_radius = 150  # Base radius for the largest circle
        self.radius_increment = 30  # Increment for the radius of each subsequent circle

        # Set up a timer for animation
        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.update_animation)
        self.timer.start(50)  # Update every 50 ms


    def paintEvent(self, event):
        # Gradient background
        painter = QPainter(self)
        gradient = QLinearGradient(0, 0, 0, self.height())
        gradient.setColorAt(0.0, QColor("#141727"))  # Dark blue at the top
        gradient.setColorAt(1.0, QColor("#2C3262"))  # Dark pink at the bottom
        painter.fillRect(self.rect(), gradient)

        # Draw concentric circles below the images
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)

        # Coordinates to center circles under the images
        circle_center_x = 500  # Adjust to align with the images
        circle_center_y = 650  # Adjust to position below images

        # Draw multiple concentric circles with increasing radii
        for i in range(self.num_circles):
            # Calculate radius for each circle with pulsing effect
            pulse_scale = 1 + 0.1 * math.sin(math.radians(self.angle + (i * 30)))  # Pulsing effect
            radius = int((self.base_radius + i * self.radius_increment) * pulse_scale)  # Adjust radius

            # Calculate the orbiting effect around its own center
            orbit_angle = self.angle + (i * (360 / self.num_circles))  # Angle for current circle
            y_offset = int(10 * math.sin(math.radians(orbit_angle)))  # Orbit effect along the y-axis

            # Set circle color gradient
            gradient = QLinearGradient(circle_center_x - radius, circle_center_y, circle_center_x + radius, circle_center_y)
            gradient.setColorAt(0.0, QColor(255, 255, 255, 150))  # Red color at the top
            gradient.setColorAt(1.0, QColor(255, 255, 255, 150))  # Blue color at the bottom

            # Draw each circle with orbiting effect and pulsing size
            painter.setPen(QPen(gradient, 2, Qt.PenStyle.SolidLine))  # Use gradient pen for the ring
            painter.drawEllipse(circle_center_x - radius,
                                circle_center_y + y_offset - int(radius * 0.35),
                                radius * 2,
                                int(radius * 0.7))  # Flatten the ellipses

        super().paintEvent(event)

    def update_animation(self):
        self.angle += 5  # Increment angle for animation
        self.angle %= 360  # Keep angle within 0-360
        self.update()  # Trigger repaint



