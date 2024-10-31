import cv2
from PIL import Image
import numpy as np

def watercolor_effect(image, sigma_s=5, filter_n=2):
    image = np.array(image)
    
    image_resized = cv2.resize(image, None, fx=0.5, fy=0.5)
    
    image_cleared = cv2.medianBlur(image_resized, 3)
    image_cleared = cv2.medianBlur(image_cleared, 3)
    image_cleared = cv2.medianBlur(image_cleared, 3)

    image_cleared = cv2.edgePreservingFilter(image_cleared, sigma_s=sigma_s)
    
    image_filtered = cv2.bilateralFilter(image_cleared, 3, 10, 5)

    for i in range(filter_n):
        image_filtered = cv2.bilateralFilter(image_filtered, 3, 20, 10)


    gaussian_mask= cv2.GaussianBlur(image_filtered, (7,7), 2)
    image_sharp = cv2.addWeighted(image_filtered, 1.5, gaussian_mask, -0.5, 0)
    image_sharp = cv2.addWeighted(image_sharp, 1.4, gaussian_mask, -0.2, 10)
    
    return Image.fromarray(image_sharp)
        
    
    
    
    
    