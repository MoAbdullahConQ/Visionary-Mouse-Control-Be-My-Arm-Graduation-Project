from utils.libraries import *


class FaceControlView(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__()
        self.parent = parent
        self.init_ui()

    def init_ui(self):

        # Main Layout
        main_layout = QHBoxLayout(self)
        main_layout.setContentsMargins(40, 40, 40, 40)
        main_layout.setSpacing(60)


        # Left Content
        left_content = QVBoxLayout()


        # Back Button with image
        back_button = QPushButton()
        back_button.setFixedSize(50, 50)  # Ensure the width and height are the same for a circle
        back_button.setGeometry(100, 100, 50, 50)  # x, y, width, height

        # Set an image as the button's icon
        back_button.setIcon(QIcon("images/arrow_back.png"))
        back_button.clicked.connect(self.go_back_home)
        # Set the icon size to make it smaller
        icon_size = 30  # Adjust this value to change the size of the icon
        back_button.setIconSize(QtCore.QSize(icon_size, icon_size))

        # Apply custom style
        back_button.setStyleSheet("""
        QPushButton {
            background-color: #2A3055;  /* Set the background color */
            color: white;
            border: 1px solid white;
            border-radius: 25px;  /* Set the border radius to half of the size to make it circular */
        }

        """)

        left_content.addWidget(back_button)


        ############################# Title
        title_label = QLabel("Face Control")
        title_label.setFont(QFont("Arial", 30, QFont.Weight.Bold))
        title_label.setStyleSheet("color: white;")
        back_button.setGeometry(100, 250, 150, 50)  # x, y, width, height
        left_content.addWidget(title_label)


        # Add custom spacer item for spacing
        # spacer = QSpacerItem(5, 5, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
        # left_content.addItem(spacer)

        # Description
        description_label = QLabel(
            "With Face Control, experience a hands-\n\nfree way to navigate the app, "
            "using simple\n\n facial expressions and head movements.\n\n"
            "This innovative feature makes interaction \n\n effortless, accessible, and convenient."
        )
        description_label.setFont(QFont("Arial", 14))
        description_label.setStyleSheet("color: white;")
        description_label.setWordWrap(True)
        back_button.setGeometry(100, 450, 150, 50)  # x, y, width, height
        left_content.addWidget(description_label)

        # Add custom spacer item for spacing
        # spacer = QSpacerItem(5, 5, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
        # left_content.addItem(spacer)


        # Run/Stop Button

        # Button: "Run Now!"
        run_button = QPushButton("Run Now! ...", self)
        run_button.setGeometry(30, 550, 300, 50)  # X, Y, Width, Height
        run_button.setStyleSheet(
            """
            QPushButton {
                background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1,
                stop:0.3 #151b58,
                stop:0.5 #C1D3F5,
                stop:0.6 #151b58);
                color: white;
                font-size: 18px;
                font-weight: bold;
                border: none;
                border-radius: 25px;
            }
            QPushButton:hover {
                background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1,
                stop:0.6 #151b58,
                stop:0.5 #C1D3F5
                stop:0.3 #151b58);
            }
            """
        )


        # Add some stretch at the bottom
        left_content.addStretch()

        # Add custom spacer item for spacing
        # spacer = QSpacerItem(5, 5, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
        # left_content.addItem(spacer)

        ################################################### video player ##########################
        # Right Content (Video Player)
        # video_frame = QFrame()
        # video_frame.setStyleSheet("background-color: #2C3262; border-radius: 15px;")
        # video_frame.setFixedSize(300, 400)

        # Add a video widget inside the frame
        # video_player = QVideoWidget(video_frame)
        # video_player.setGeometry(10, 10, 280, 380)

        # Set up media player (optional for video playback)
        # self.media_player = QMediaPlayer()
        # self.media_player.setVideoOutput(video_player)
        # Uncomment the next line and replace 'video_path.mp4' with your video file path
        # self.media_player.setSource(QUrl.fromLocalFile("C:/Users/El2sr/Pictures/graduation project/WhatsApp Video 2024-11-14 at 01.10.54_39093217.mp4"))


        # Adding to the layout
        main_layout.addLayout(left_content)
        # main_layout.addWidget(video_frame)

        # Set Layout
        self.setLayout(main_layout)


    def go_back_home(self):
        self.parent.navigate_to_page(1)  # Navigate back to HomePage

