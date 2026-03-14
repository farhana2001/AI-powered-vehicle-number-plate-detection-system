AI-powered vehicle number plate recognition system that detects vehicle license plates from images, extracts the plate number using OCR, and retrieves vehicle owner details from a MySQL database.

The system uses **YOLO for object detection**, **Tesseract OCR for text extraction**, and **MySQL for storing owner information**.

---

## 📌 Features

- 🚘 Detects vehicle number plates using YOLO
- 🔍 Extracts text from detected plates using Tesseract OCR
- 🗄 Retrieves owner details from MySQL database
- ⚡ Fast and automated vehicle identification
- 🧠 Deep learning based detection model

---

## 🛠 Technologies Used

- Python
- YOLO (Ultralytics)
- OpenCV
- Tesseract OCR
- MySQL
- MySQL Connector
- NumPy

 ▶ How It Works

1️⃣ Input image is given to the system

2️⃣ YOLO detects the number plate

3️⃣ OpenCV crops the plate region

4️⃣ Tesseract OCR extracts the plate text

5️⃣ The extracted number is searched in the MySQL database

6️⃣ Owner details are displayed
