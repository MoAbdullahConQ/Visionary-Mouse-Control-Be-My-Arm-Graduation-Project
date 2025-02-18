import threading

import cv2
import mediapipe as mp

from utils.libraries import *
from models.hand.hand_mouse_control import detect_gesture



class HandControlView(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super().__init__()
        self.parent = parent
        self.is_running = False  # إضافة متغير للتحكم في حالة التشغيل
        self.hand_control_thread = None  # متغير لحفظ الـ thread
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
        title_label = QLabel("Hand Control")
        title_label.setFont(QFont("Arial", 30, QFont.Weight.Bold))
        title_label.setStyleSheet("color: white;")
        back_button.setGeometry(100, 250, 150, 50)  # x, y, width, height
        left_content.addWidget(title_label)


        # Add custom spacer item for spacing
        spacer = QSpacerItem(5, 5, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
        left_content.addItem(spacer)

        # Description
        description_label = QLabel(
            "With Face Control, experience a \nhands-free way to navigate the \napp, using simple facial."
        )
        description_label.setFont(QFont("Arial", 14))
        description_label.setStyleSheet("color: white;")
        description_label.setWordWrap(True)
        back_button.setGeometry(100, 450, 150, 50)  # x, y, width, height
        left_content.addWidget(description_label)

        # Add custom spacer item for spacing
        spacer = QSpacerItem(5, 5, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
        left_content.addItem(spacer)


        # Run/Stop Button

        # Button: "Run Now!"
        self.run_button = QPushButton("Run Now! ...", self)
        # self.run_button.setGeometry(30, 550, 300, 50)  # X, Y, Width, Height
        self.run_button.setFixedSize(250, 50)

        button_layout = QHBoxLayout()
        # button_layout.addStretch(1)
        button_layout.addWidget(self.run_button)
        button_layout.addStretch(1)
        left_content.addLayout(button_layout)
        self.run_button.setStyleSheet(
            """
           QPushButton {
        background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0,
            stop:0 #C1D3F5,
            stop:1 #1A1E4D);
        color: white;
        font-size: 18px;
        font-weight: bold;
        border: none;
        border-radius: 25px;
        padding: 10px 20px;
        
       
    }
    
    /* الصورة الثانية عند hover */
    QPushButton:hover {
        background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0,
            stop:0.13 #5E8CAC,
            stop:1 #2B4056);
    }
    
        """)

        glow = QGraphicsDropShadowEffect()
        glow.setBlurRadius(30)
        glow.setColor(QColor(193, 211, 245, 150))
        glow.setOffset(0, 0)
        self.run_button.setGraphicsEffect(glow)

        self.run_button.clicked.connect(self.toggle_hand_control)
        left_content.addWidget(self.run_button)

        # Set main layout
        main_layout.addLayout(left_content)
        self.setLayout(main_layout)




        # Add some stretch at the bottom
        # left_content.addStretch()

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
        # main_layout.addLayout(left_content)
        # # main_layout.addWidget(video_frame)
        #
        # # Set Layout
        # self.setLayout(main_layout)

    def toggle_hand_control(self):
        if not self.is_running:
            self.is_running = True
            self.run_button.setText("Stop")
            self.hand_control_thread = threading.Thread(target=self.run_hand_control)
            self.hand_control_thread.start()
        else:
            self.is_running = False
            self.run_button.setText("Run Now! ...")

    def run_hand_control(self):
        mpHands = mp.solutions.hands
        hands = mpHands.Hands(
            static_image_mode=False,
            model_complexity=1,
            min_detection_confidence=0.7,
            min_tracking_confidence=0.7,
            max_num_hands=1
        )

        draw = mp.solutions.drawing_utils
        cap = cv2.VideoCapture(0)

        try:
            while self.is_running and cap.isOpened():
                ret, frame = cap.read()
                if not ret:
                    break
                frame = cv2.flip(frame, 1)
                frameRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                processed = hands.process(frameRGB)

                landmark_list = []
                if processed.multi_hand_landmarks:
                    hand_landmarks = processed.multi_hand_landmarks[0]
                    draw.draw_landmarks(frame, hand_landmarks, mpHands.HAND_CONNECTIONS)
                    for lm in hand_landmarks.landmark:
                        landmark_list.append((lm.x, lm.y))

                detect_gesture(frame, landmark_list, processed)

                cv2.imshow('Hand Control', frame)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
        finally:
            cap.release()
            cv2.destroyAllWindows()

    def paintEvent(self, event):
        # Gradient background
        painter = QPainter(self)
        gradient = QLinearGradient(0, 0, 0, self.height())
        gradient.setColorAt(0.0, QColor("#141727"))  # Dark blue at the top
        gradient.setColorAt(1.0, QColor("#2C3262"))  # Dark pink at the bottom
        painter.fillRect(self.rect(), gradient)

        super().paintEvent(event)

    def go_back_home(self):
        if self.is_running:
            self.toggle_hand_control()
        if self.parent:  # Check if the parent exists
            self.parent.navigate_to_page(0)  # Navigate to the main (home) page (page index 0)
