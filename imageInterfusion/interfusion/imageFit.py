from turtle import resizemode
from skimage.transform import resize

def resizeImage(image, proportion):
    assert 0 <= proportion <= 1, 'Specify a valid ratio between 0 and 1.'
    height = round(image.shape[0] * proportion)
    width = round(image.shape[1] * proportion)
    imageResized = resize(image, (height, width), anti_aliasing=True)
    return imageResized
    