# Save & Grayscale with OpenCV

import cv2

# read the original image
img = cv2.imread("images/nature.jpeg")

# check if the image is loaded or not

if img is None:
    print("Error: Image not found")
    exit()
else:
    # convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # save the grayscale image
    cv2.imwrite("images/gray_nature.jpg", gray)

    print("Grayscale image saved successfully!")