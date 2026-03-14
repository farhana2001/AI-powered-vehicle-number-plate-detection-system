import mysql.connector

def get_owner_details(reg_number):
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="numberplate"
    )

    cursor = conn.cursor()

    query = """
    SELECT Name, house_name, house_no, mobile_no
    FROM vechiledata
    WHERE RegNO = %s
    """

    cursor.execute(query, (reg_number,))
    result = cursor.fetchone()

    conn.close()
    return result
from ultralytics import YOLO

model = YOLO("C:\\Users\\VICTUS\\Downloads\\best.pt")
import cv2

def detect_number_plate(image_path):
    img = cv2.imread(image_path)
    results = model(img)

    for result in results:
        boxes = result.boxes.xyxy.cpu().numpy()

        for box in boxes:
            x1, y1, x2, y2 = map(int, box)
            plate = img[y1:y2, x1:x2]
            return plate
    return None
import pytesseract
pytesseract.pytesseract.tesseract_cmd=r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def extract_text(plate_img):
    gray = cv2.cvtColor(plate_img, cv2.COLOR_BGR2GRAY)
    text = pytesseract.image_to_string(gray, config="--psm 8")
    text = ''.join(e for e in text if e.isalnum())
    return text.upper()
image_path = "C:\\Users\\VICTUS\\Desktop\\data science\\deep learning projects\\vehicle_number project\\images\\Cars12.png"  # your test image

plate_img = detect_number_plate(image_path)

if plate_img is not None:
    plate_number = extract_text(plate_img)
    print("Detected Plate:", plate_number)

    owner = get_owner_details(plate_number)

    if owner:
        print("\nOwner Details:")
        print("Owner Name:", owner[0])
        print("House Name:", owner[1])
        print("Place:", owner[2])
        print("Phone:", owner[3])
    else:
        print("Vehicle not found in database.")
else:
    print("No number plate detected.")