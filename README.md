# 🎹 Hand Gesture Controlled Virtual Piano

---

# Features

* 🎹 Play a virtual piano using hand gestures
* ✋ Real-time hand and finger tracking using MediaPipe
* 📷 Webcam-based interaction (no external sensors required)
* 🔊 Instant piano sound playback with low latency
* 🎼 Support for multiple piano keys (14 or 21 keys)
* 🎵 White and black piano keys (sharps/flats)
* 🎨 Animated key highlighting when pressed
* 🤚 Multi-finger chord detection
* 🔈 Gesture-based volume control
* 📹 Performance recording and playback
* 🌐 Flask-based web interface
* 🖥️ Modern full-screen responsive user interface
* ⚡ Smooth real-time performance using OpenCV and NumPy

---

# Technologies Used

 Technology | Purpose                          
 ---------- | -------------------------------- 
 Python     | Backend Programming              
 OpenCV     | Webcam Capture & Computer Vision 
 MediaPipe  | Hand Landmark Detection          
 NumPy      | Numerical Processing             
 Pygame     | Piano Sound Playback             
 Flask      | Web Application Framework        
 HTML5      | User Interface                   
 CSS3       | Styling                          
 JavaScript | Frontend Interaction             

---

# Project Structure

```text
Hand_Gesture_Virtual_Piano/
│
├── app.py
├── generate_sounds.py
├── hand_tracker.py
├── piano.py
│── sounds/
│         C4.wav
│         C#4.wav
│         D4.wav
│         ...
│
├── vision/
│     hand_detector.py
│     gesture_detector.py
│     volume_control.py
│
└── README.md

---

# Installation

## Clone the Repository

```bash
git clone https://github.com/yourusername/Hand-Gesture-Virtual-Piano.git
```

```bash
cd Hand-Gesture-Virtual-Piano
```

---

## Create a Virtual Environment

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Required Libraries

```text
opencv-python
mediapipe
numpy
pygame
flask
```

---

# Run the Application

```bash
python app.py
```

Open your browser and visit:

```text
http://127.0.0.1:5000
```

---

# How It Works

1. The webcam captures live video.
2. MediaPipe detects and tracks hand landmarks.
3. The system identifies fingertip positions.
4. Virtual piano keys are displayed on the screen.
5. When a fingertip touches a virtual key:

   * The key changes color.
   * The corresponding piano note is played.
6. Multiple fingers can press different keys simultaneously to create chords.
7. Hand gestures can also adjust the piano volume.
8. Users can record and replay their performances.

---

# Workflow

```text
Webcam
   │
   ▼
OpenCV Video Capture
   │
   ▼
MediaPipe Hand Detection
   │
   ▼
Finger Tracking
   │
   ▼
Virtual Piano Keyboard
   │
   ▼
Collision Detection
   │
   ▼
Pygame Sound Engine
   │
   ▼
Real-Time Piano Playback
---

# Author

**Bishnu Brata Shome**

Master of Computer Applications (MCA)

---

# License

This project is released under the **MIT License**.


Special thanks to the open-source communities behind:

* OpenCV
* MediaPipe
* Pygame
* Flask
* NumPy

Their tools and libraries made this project possible.
