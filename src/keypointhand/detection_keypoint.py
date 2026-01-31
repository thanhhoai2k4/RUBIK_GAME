import cv2
from ultralytics import YOLO

# 1. Load Model Pose
model = YOLO('models/best_l1.pt')

# 2. Mở Webcam
cap = cv2.VideoCapture(0)

# Cài đặt kích thước (giảm độ phân giải nếu máy lag)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

if not cap.isOpened():
    print("Không mở được Camera")
    exit()

print("Đang chạy... Nhấn 'q' để thoát.")

while True:
    # 3. Đọc frame
    ret, frame = cap.read()
    if not ret: break

    # 4. Predict (Dự đoán)
    # verbose=False: Ẩn log in ra terminal cho đỡ rối
    results = model(frame, verbose=False, conf=0.5)

    # 5. Lấy kết quả để xử lý
    for result in results:
        # --- CÁCH 1: Vẽ tự động (Dùng cái này để Show lên màn hình cho đẹp) ---
        # Hàm plot() của Pose model sẽ tự nối các điểm xương lại với nhau
        annotated_frame = result.plot()

        # --- CÁCH 2: Truy cập dữ liệu thô (Code của bạn nằm ở đây) ---
        # Nếu bạn muốn lấy toạ độ để tính toán (ví dụ: đếm số lần gập bụng)
        if result.keypoints is not None:
            # Lấy mảng toạ độ x,y của các khớp (Mũi, mắt, vai, khuỷu tay...)
            # xy trả về tensor, chuyển sang numpy để dễ dùng
            keypoints = result.keypoints.xy.cpu().numpy()

            # Ví dụ: In toạ độ của người đầu tiên được phát hiện
            if len(keypoints) > 0:
                pass
                # print(f"Toạ độ mũi người 1: {keypoints[0][0]}") 
                # (Index 0 thường là mũi trong COCO dataset)

    # 6. Show lên màn hình
    # Lưu ý: Show 'annotated_frame' (ảnh đã vẽ xương), đừng show 'frame' gốc
    cv2.imshow('YOLO Pose Estimation', annotated_frame)

    # 7. Thoát
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()