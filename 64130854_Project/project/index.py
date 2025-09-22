import cv2

# Load bộ nhận diện khuôn mặt Haar Cascade
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Hàm phát hiện khuôn mặt trong ảnh
def detect_faces(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # chuyển ảnh về xám
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)
    for (x, y, w, h) in faces:
        # Vẽ hình chữ nhật quanh khuôn mặt
        cv2.rectangle(image, (x, y), (x+w, y+h), (255, 0, 0), 2)
    return image

# Phát hiện trong ảnh
img = cv2.imread('path_to_image.jpg')
img_faces = detect_faces(img)
cv2.imshow('Face Detection', img_faces)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Phát hiện trong video (webcam)
cap = cv2.VideoCapture(0)  # 0 = webcam máy tính
while True:
    ret, frame = cap.read()
    if not ret:
        break
    frame_faces = detect_faces(frame)
    cv2.imshow('Video Face Detection', frame_faces)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):  # Nhấn 'q' để thoát
        break

cap.release()
cv2.destroyAllWindows()
