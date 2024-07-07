import streamlit as st
import numpy as np
import cv2

# Set page background color
st.markdown(
    """
    <style>
    body {
        background-color: #f0f2f6;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Centered title
st.markdown(
    """
    <h1 style='text-align: center;'>Aplikasi Manajemen Citra Warna</h1>
    """,
    unsafe_allow_html=True
)

# Layout for image upload, adjustments, and operations
col1, col2 = st.columns([1, 2])

with col2:
    def adjust_brightness_contrast(image, brightness=0, contrast=0):
        alpha = (contrast + 127) / 127.0  # Normalize contrast
        beta = brightness
        return cv2.convertScaleAbs(image, alpha=alpha, beta=beta)

    def detect_contours(image):
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)[1]  # Improved binarization
        contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        return cv2.drawContours(image.copy(), contours, -1, (0, 255, 0), 3)

    def detect_faces(image):
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
        
        if face_cascade.empty():
            st.error("Error loading cascade classifier")
            return image, 0
        
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
        for (x, y, w, h) in faces:
            cv2.rectangle(image, (x, y), (x+w, y+h), (255, 0, 0), 2)
        return image, len(faces)

    def detect_eyes(image):
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')
        
        if eye_cascade.empty():
            st.error("Error loading eye cascade classifier")
            return image, 0
        
        eyes = eye_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=10, minSize=(20, 20))
        for (x, y, w, h) in eyes:
            cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)
        return image, len(eyes)

    uploaded_image = st.file_uploader("Upload Gambar", type=['jpg', 'jpeg', 'png'])
    camera_image = st.camera_input("Ambil Gambar dari Kamera")

    if uploaded_image is not None or camera_image is not None:
        if uploaded_image is not None:
            file_bytes = np.asarray(bytearray(uploaded_image.read()), dtype=np.uint8)
        else:
            file_bytes = np.asarray(bytearray(camera_image.read()), dtype=np.uint8)
        
        image = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)

        st.image(image, channels="BGR", caption="Gambar Original")

        brightness = st.slider("Kecerahan", -100, 100, 0)
        contrast = st.slider("Kontras", -100, 100, 0)

        if st.button("Atur Kecerahan dan Kontras 💡"):
            adjusted_image = adjust_brightness_contrast(image, brightness, contrast)
            st.image(adjusted_image, channels="BGR", caption="Gambar dengan Kecerahan dan Kontras Disesuaikan")

        if st.button("Deteksi Kontur 🔍"):
            contoured_image = detect_contours(image)
            st.image(contoured_image, channels="BGR", caption="Gambar dengan Kontur Terdeteksi")

        if st.button("Deteksi Wajah 😃"):
            face_detected_image, num_faces = detect_faces(image.copy())
            st.image(face_detected_image, channels="BGR", caption=f"Deteksi Wajah: {num_faces} wajah terdeteksi")

        if st.button("Deteksi Mata 👁️"):
            eye_detected_image, num_eyes = detect_eyes(image.copy())
            st.image(eye_detected_image, channels="BGR", caption=f"Deteksi Mata: {num_eyes} mata terdeteksi")

with col1:
    def convert_to_hsv(image):
        return cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    def calculate_histogram(image):
        return cv2.calcHist([image], [0], None, [256], [0, 256])

    if uploaded_image is not None or camera_image is not None:
        st.subheader("Pilih Operasi yang Ingin Dilakukan:")
        operation = st.selectbox("", ["Ubah ke HSV", "Hitung Histogram"])

        if operation == "Ubah ke HSV":
            hsv_image = convert_to_hsv(image)
            st.image(hsv_image, channels="HSV", caption="Gambar dalam HSV")

        elif operation == "Hitung Histogram":
            hist = calculate_histogram(image)
            st.bar_chart(hist.ravel(), width=600, height=300)
