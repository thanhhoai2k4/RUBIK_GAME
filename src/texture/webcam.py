from ursina import *
import numpy as np
import cv2
from PIL import Image



class WebcamBackground(Entity):
    def __init__(self):
        super().__init__()
        self.parent = camera
        self.model = 'quad'
        self.scale = (14, 6)
        self.z = 20
        self.unlit = True
        self.width = 1280
        self.height = 720
        self.texture = Texture(
            Image.new(mode='RGBA', size=(self.width, self.height), color=(0, 0, 0, 255))
        )

        # Khởi tạo Camera
        self.cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, self.width)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, self.height)

    def update(self):
        if self.cap.isOpened():
            ret, frame = self.cap.read()
            if ret:
                # 2. XỬ LÝ ẢNH
                # Chuyển BGR (OpenCV) -> RGBA (Ursina Texture format)
                # Dùng RGBA (4 kênh màu) để tương thích tốt nhất với Texture
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
                frame = cv2.resize(frame, (self.width, self.height))
                frame = np.flipud(frame)  # Lật ảnh
                frame = np.ascontiguousarray(frame)
                # 3. CẬP NHẬT DỮ LIỆU VÀO TEXTURE CŨ (KHÔNG TẠO MỚI)
                # Truy cập thẳng vào lõi Panda3D (_texture) để set dữ liệu RAM
                # Cách này cực nhanh và không gây lỗi _cached_image
                self.texture._texture.setRamImage(frame)

    def on_destroy(self):
        if self.cap:
            self.cap.release()