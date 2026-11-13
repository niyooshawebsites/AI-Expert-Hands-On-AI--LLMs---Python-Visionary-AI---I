# Rotating & Adjusting Image Brightness


import cv2

# Read the original image
img = cv2.imread("images/nature.jpeg")

if img is None:
    print("Error: Image not found!")
    exit()

# image shape
print("Image Shape:", img.shape) # Image Shape: (1281, 1920, 3)

# Get image dimensions
height, width = img.shape[:2]

# Define the center of rotation
center = (width // 2, height // 2)

# Create rotation matrix (45 degrees)
matrix = cv2.getRotationMatrix2D(center, 45, 1.0)

# Rotate the image
rotated = cv2.warpAffine(img, matrix, (width, height))

# Save the rotated image
cv2.imwrite("images/rotated_nature.jpg", rotated)

print("Image rotated successfully!")
