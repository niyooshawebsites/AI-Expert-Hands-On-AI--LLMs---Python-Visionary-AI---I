# Edge detection identifies boundaries between different regions of an image.

# For example, consider a photograph of a car.

# Edge detection can identify:

# Car boundaries.
# Windows.
# Wheels.
# Headlights.
# Other object outlines.

import cv2

img = cv2.imread('images/car.jpeg')
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# sobel edge detection
# cv2.Sobel(image, ddepth, dx, dy, ksize)
def sobel_edge_detection(gray_img):
    sobel_x = cv2.Sobel(gray_img, cv2.CV_64F, 1, 0, ksize=3)

    sobel_y = cv2.Sobel(gray_img, cv2.CV_64F, 0, 1, ksize=3)

    # convert to absolute values
    sobel_x = cv2.convertScaleAbs(sobel_x)
    sobel_y = cv2.convertScaleAbs(sobel_y)

    # combined gradients
    sobel = cv2.addWeighted(sobel_x,0.5, sobel_y, 0.5, 0)

    cv2.imshow("Original", img)
    cv2.imshow("Sobel X", sobel_x)
    cv2.imshow("Sobel Y", sobel_y)
    cv2.imshow("Sobel Combined", sobel)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

# laplacian edge detection
# cv2.Laplacian(image, ddepth, ksize)
def laplacian_edge_detection(gray_img):
    # for laplacian edge detection always apply the guassian blur first
    blur = cv2.GaussianBlur(gray_img, (3, 3), 0)

    laplacian = cv2.Laplacian(blur, cv2.CV_64F, ksize=3)

    laplacian = cv2.convertScaleAbs(laplacian)

    cv2.imshow("Original", img)
    cv2.imshow("Laplacian", laplacian)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

# canny edge detection
# cv2.canny(image, threshold1, threshold2)
def canny_edge_detection(gray_img):
    blur = cv2.GaussianBlur(gray_img, (5,5),0)

    canny = cv2.Canny(blur, 100, 200)

    cv2.imshow("Original", img)
    cv2.imshow("Canny Edges", canny)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

while True:
    print("Enter 1 for Sobel Egde Detection\nEnter 2 for Laplacian Edge Detection\nEnter 3 for Canny Edge Detection\n")

    user_input = int(input("Enter your choice: "))

    match user_input:
        case 1:
            sobel_edge_detection(gray_img)
            break
        case 2:
            laplacian_edge_detection(gray_img)
            break
        case 3:
            canny_edge_detection(gray_img)
            break