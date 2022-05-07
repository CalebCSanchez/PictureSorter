# from skimage.metrics import structural_similarity
import cv2
import numpy as np

# img1 = cv2.imread('./Images/nobitches.jpeg', 0)
# img2 = cv2.imread('./Images/nobitches.jpeg', 0)


def pictureSorter(img1url, img2url):
    img1 = cv2.imread(str(img1url), 0)
    img2 = cv2.imread(str(img2url), 0)

    if (img2 is None or img1 is None):
        print('image type none')
        return 1
    if (img1.shape == img2.shape):
        pass
    elif (img1.shape < img2.shape):
        img2 = cv2.resize(img2, tuple(reversed(img1.shape)))
    else:
        img1 = cv2.resize(img1, tuple(reversed(img2.shape)))



    res = cv2.absdiff(img1, img2)

    res = res.astype(np.uint8)
    percentage =(100 - (np.count_nonzero(res) * 100)/ res.size )
    if (percentage >= 95):
        cv2.imshow('img1', img1)
        cv2.waitKey(0)
        cv2.imshow('img2', img2)
        cv2.waitKey(0)
        

    
    return percentage
