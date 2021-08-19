import cv2  #import the open computer vision library
import numpy as np    #from python for scientific calculations
import matplotlib.pyplot as plt   #for ploting 

video_link = 'https://youtu.be/KWJaBJYJIjI'


def plot_image(image, title):
    plt.imshow(image, cmap = gray)
    plt.title(title)
    plt.show

def save_image(image, title):
    cv2.imwrite(title, image)

def grayscale(image):
    gray_image =cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    return gray_image

def blur(image):
    blur_image = cv2.GaussianBlur(image, (3,3), 0)
    return blur_image

def canny(image):
    canny_image = cv2.Canny(image, 100, 150)
    return canny_image

def aoi(image):
    height = image.shape[0]
    width = image.shape[0]
    bottom_padding = 100
    bottom_left = [0, height-bottom_padding]
    bottom_right = [width, height-bottom_padding]
    top_right = [width*1/3, height*1/3]
    top_left = [width*2/3, height*1/3]
    vertices = [np.array([bottom_left, bottom_right, top_left, top_right, dtype = np.int32])]
    mask = np.zeros_like(image)
    cv2.fillPoly(mask, vertices, 255)
