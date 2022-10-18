from email.mime import image
from numpy import insert
from skimage.io import imread, imsave

def readImage(path, isGray=False):
    image = imread(path, as_gray=isGray)
    return image

def saveImage(image, path):
    imsave(path, image)
    