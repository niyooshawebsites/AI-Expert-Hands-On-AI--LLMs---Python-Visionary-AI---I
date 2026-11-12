import cv2

# load the original image
img = cv2.imread('images/nature.jpeg')

if img is None:
    print('Error: Image not found!')
    exit()

# convert BGR to RGB
rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# convert BGR to Grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# convert BGR to HSV
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# save converted images
cv2.imwrite('images/nature_rgb.jpg', rgb)
cv2.imwrite('images/nature_gray.jpg', gray)
cv2.imwrite('images/nature_hsv.jpg', hsv)

print('All color conversions completed')

# image cropping
# crop the image

# Syntax: img[y1:y2, x1:x2]
# 50 = Starting Y-coordinate.
# 300 = Ending Y-coordinate.
# 100 = Starting X-coordinate.
# 400 = Ending X-coordinate.

# The cropped image will have:
# Height = 250 pixels.
# Width = 300 pixels.

cropped = img[50:300, 100:400]

# save the cropped image
cv2.imwrite('images/cropped_nature.jpg', cropped)
print("Image cropped and saved successfully!")
