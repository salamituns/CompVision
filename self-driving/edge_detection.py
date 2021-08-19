import cv2  #import the open computer vision library
import numpy as np    #from python for scientific calculations
import matplotlib.pyplot as plt     #for ploting 
from numpy.core.records import array   
import edge_detection as edge   

#cap = cv2.VideoCapture('cardriving.mp4')

def binary_array(array, thresh, value = 0):
#return a 2d binary array in which all pixels are either 1 or 0
    if value == 0:
        #create an array of ones with the same shape and type as the input 2d array.
        binary = np.ones_like(array)
    else:
        #else, create an array of zeros with the same shape and type as in the 2d array.
        binary = np.zeros_like(array)
        value = 1
    binary[(array >= thresh[0]) & (array <= thresh[1])] = value
    return binary

def blur_gaussian(channel, ksize = 3):
    return cv2.GaussianBlur(channel, (ksize, ksize), 0)

def mag_thresh(image, sobel_kernel = 3, thresh=(0,255)):
    sobelx = np.absolute(sobel(image, orient = 'x', sobel_kernel = sobel_kernel))

    sobely = np.absolute(sobel(image, orient = 'y', sobel_kernel = sobel_kernel))

    mag = np.sqrt(sobel ** 2 + sobely ** 2)
    return binary_array(mag, thresh)

def sobel(img_channel, orient = 'x', sobel_kernel = 3):
    if orient == 'x':
        sobel = cv2.Sobel(img_channel, cv2.CV_64F, 1, 0, sobel_kernel)
    if orient == 'y':
        sobel = cv2.Sobel(img_channel, cv2.CV_64F, 0, 1, sobel_kernel)
    
    return sobel

def threshold(channel, thresh =(128, 255), thresh_type = cv2.THRESH_BINARY):
    return cv2.threshold(channel, thresh[0], thresh[1], thresh_type)

