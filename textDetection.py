# importing the libraries

import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

img = cv2.imread('test_image_2.png')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
height, width = img.shape[:2]
center = (height/2, width/2)
rotate_matrix = cv2.getRotationMatrix2D(center=center, angle=180, scale=1)
rotated_image = cv2.warpAffine(src=img, M=rotate_matrix, dsize=(width, height))

#---------------------------------------------------------------------------------------
# # detecting characters
# print(pytesseract.image_to_string(img))
#
# # this will print the boxes around the texts
# # we will have bounding box information corresponding to each character.
# # X, Y, W, H -->> x-coordinate, y-coordinate, width, height
# print(pytesseract.image_to_boxes(img))
#
# # placing these boxes on our image
# hImg, wImg, _ = img.shape
# boxes = pytesseract.image_to_boxes(img)
# for b in boxes.splitlines():
#     print(b)
#     b = b.split(" ")
#     print(b)
#     x, y, w, h = int(b[1]), int(b[2]), int(b[3]), int(b[4])
#     # putting red color
#     cv2.rectangle(img, (x,hImg-y), (w,hImg-h), (0,0,255), 3)
#     # now what we can do is that we can put labels around the characters whether it's correctly classified or not!
#     cv2.putText(img, b[0], (x, hImg-y+25), cv2.FONT_HERSHEY_COMPLEX, 1, (50,50,255), 2)

#------------------------------------------------------------------------------------------------\
# detecting words...
# boxes = pytesseract.image_to_data(img)
# hImg, wImg, _ = img.shape
# # printing the bounding boxes
# print(boxes)
# for x, b in enumerate(boxes.splitlines()):
#     if x!=0:
#         b = b.split()
#         print(b)
#         if len(b)==12:
#             x, y, w, h = int(b[6]), int(b[7]), int(b[8]), int(b[9])
#             cv2.rectangle(img, (x, y), (w+x, h+y), (0,0,255), 3)
#             cv2.putText(img, b[11], (x, y), cv2.FONT_HERSHEY_COMPLEX, 1, (50, 50, 255), 2)

#--------------------------------------------------------------------------------
# detecting numbers
# we can define configurations to detect numbers and many other things. for this we need to define the configuration.

configuration = r"--oem 3--psm 6 outputbase digits"
boxes = pytesseract.image_to_data(img, config=configuration)
hImg, wImg, _ = img.shape
# printing the bounding boxes
print(boxes)
for x, b in enumerate(boxes.splitlines()):
    if x!=0:
        b = b.split()
        print(b)
        if len(b)==12:
            x, y, w, h = int(b[6]), int(b[7]), int(b[8]), int(b[9])
            cv2.rectangle(img, (x, y), (w+x, h+y), (0,0,255), 3)
            cv2.putText(img, b[11], (x, y), cv2.FONT_HERSHEY_COMPLEX, 1, (50, 50, 255), 2)


# showing the image using the pop up window
cv2.imshow("Result", img)
# cv2.imshow("result", rotated_image)
# we will declare the wait key as our window will be open for the infinite period of time till we cancel it.
cv2.waitKey(0)

