import pytesseract
from pytesseract import Output
import cv2

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

img = cv2.imread("test_image_2300.png")
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# image_to_osd() function will give us details about the orientation of the text in the image data.
results = pytesseract.image_to_osd(img, output_type=Output.DICT)

print("detected orientation : {}".format(results['orientation']))
