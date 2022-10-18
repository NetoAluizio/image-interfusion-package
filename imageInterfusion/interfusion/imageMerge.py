import numpy as np
from skimage.color import rgb2gray
from skimage.exposure import match_histograms
from skimage.metrics import structural_similarity

def findDifference(image1, image2):
    assert image1.shape == image2.shape, 'Specify 2 images with the same format.'
    grayImage1 = rgb2gray(image1)
    grayImage2 = rgb2gray(image2)
    (score, differenceImage) = structural_similarity(grayImage1, grayImage2, full=True)
    print('Similarity between images', score)
    normalizedDifferenceImage = (differenceImage-np.min(differenceImage))/(np.max(differenceImage)-np.min(differenceImage))
    return normalizedDifferenceImage

def transferHistogram(image1, image2):
    matchedImage = match_histograms(image1, image2, multichannel=True)
    return matchedImage
    