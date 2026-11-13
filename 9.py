# image annotation with shapes and measurements
import cv2
# load the image
img = cv2.imread('images/nature.jpeg')

def show_original_img(img):
    # display the image
    cv2.imshow("Orginal Image", img)

    # wait for keypress
    cv2.waitKey(0)

    # close all windows
    cv2.destroyAllWindows()

# drawa a line
def line_draw(img):
    # syntax = cv2.line(image, start_point, end_point, color, line_width)
    cv2.line(img, (50, 50), (300,300), (0, 255, 0), 3)
    cv2.imshow("Line Annotation", img)

    # wait for keypress
    cv2.waitKey(0)

    # close all windows
    cv2.destroyAllWindows()

# draw a rectangle
def draw_rect(img):
    # syntax => cv2.rectangle(image, top_left, bottom_right, color, thickness)
    cv2.rectangle(img, (100, 100), (400, 300), (255, 0, 0), 3)
    cv2.imshow("Rectange Annotation", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# draw a circle
def draw_circle(img):
    # syntax => cv2.circle(image, center, radius, color, thickness)
    cv2.circle(img, (250, 250), 80, (0, 0, 255), 3)
    cv2.imshow("Circle Annotation", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# draw a filled circle
def filled_circle(img):
    # syntax => cv2.circle(image, center, radius, color, -1)
    cv2.circle(img,(250,250), 80, (0,255,0),-1)
    cv2.imshow("Filled circle", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# add text to image
def add_text(img):
    # syntax => cv2.putText(image, text, position, font, font_scale, color, thickness)
    cv2.putText(img, "Hello OpenCV", (100,100), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 0), 2)
    cv2.imshow('Text Annotation', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

while True:
    print("Enter 1 for Original image\nEnter 2 for image with line\nEnter 3 for image with rectange\nEnter 4 for image with circle")
    user_input = int(input("Enter your selection: "))

    match user_input:
        case 1:
            show_original_img(img)
            break
        case 2:
            line_draw(img)
            break
        case 3:
            draw_rect(img)
            break
        case 4:
            draw_circle(img)
            break
        case 5:
            filled_circle(img)
            break
        case 6:
            add_text(img)
            break

