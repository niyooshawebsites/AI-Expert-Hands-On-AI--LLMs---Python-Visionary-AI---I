# image filtering

# Image filtering is a technique used to modify an image by applying mathematical operations to its pixels.

# For example:
# Remove unwanted noise.
# Blur an image.
# Smooth image details.
# Sharpen edges.
# Improve image quality.

import cv2
import numpy as np

img = cv2.imread('images/nature.jpeg')

def show_org(img):
    cv2.imshow("Original Image", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def avg_mean_blur(img):
    # syntax => cv2.blur(image, kernel_size)

    # Understanding kernel size:
    # (3, 3) = Small blur.
    # (5, 5) = Medium blur.
    # (9, 9) = Stronger blur.

    blur1 = cv2.blur(img, (5, 5))
    blur2 = cv2.blur(img, (10, 10))
    blur3 = cv2.blur(img, (20, 20))
    cv2.imshow('Original Image', img)
    cv2.imshow('Blur with Kernel size: (5, 5)', blur1)
    cv2.imshow('Blur with Kernel size: (10, 10)', blur2)
    cv2.imshow('Blur with Kernel size: (20, 20)', blur3)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

def avg_median_blur():
    # avg median filter is useful for removing salt and pepper noise
    # Salt-and-pepper noise is a type of image noise where random pixels become either completely white or completely black. It makes an image look like someone has sprinkled salt and black pepper over it.

    # syntax => cv2.medianBlur(image, kernel_size)
    img = cv2.imread('images/salt_pepper.jpg')
    median = cv2.medianBlur(img, 5)
    cv2.imshow('Original Image', img)
    cv2.imshow('Median Blur - Removing Salt and Pepper noise', median)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

def guassian_blur(img):
    # Gaussian Filtering
    # Gaussian filtering is one of the most commonly used image filtering techniques. It reduces noise by assigning more weight to pixels near the center of the kernel.
    # syntax => cv2.GuassianBlur(image, kernel, sigmaX)

    # sigmaX represents the standard deviation of the Gaussian distribution in the horizontal (X) direction.

    # In simple words:
    # sigmaX controls how widely the Gaussian weights are distributed.
    # Smaller sigma means weights are concentrated near the center pixel.
    # Larger sigma means more neighboring pixels contribute significantly to the output.

    blur1 = cv2.GaussianBlur(img, (5, 5), 0)
    blur2 = cv2.GaussianBlur(img, (5, 5), 2)
    blur3 = cv2.GaussianBlur(img, (5, 5), 5)

    cv2.imshow('Original image',img)
    cv2.imshow('Guassian Blurred Image with sigmX = 1', blur1)
    cv2.imshow('Guassian Blurred Image with sigmX = 2', blur2)
    cv2.imshow('Guassian Blurred Image with sigmX = 5', blur3)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

while True:
    print("Enter 1 for original image\nEnter 2 for avg mean blur\nEnter 3 for avg mean blur for removing salt and pepper noise\nEnter 4 for Guassian Blurred Image\n")

    user_input = int(input("Enter your choice: "))

    match user_input:
        case 1:
            show_org(img)
            break
        case 2:
            avg_mean_blur(img)
            break
        case 3:
            avg_median_blur()
            break
        case 4:
            guassian_blur(img)
            break