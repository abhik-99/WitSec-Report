import cv2
import numpy as np

def pose_estimation(input_image):
    '''
    Given some input image, preprocess the image so that
    it can be used with the related pose estimation model
    you downloaded previously. You can use cv2.resize()
    to resize the image.
    '''
    preprocessed_image = np.copy(input_image)

    # TODO: Preprocess the image for the pose estimation model
    print("Before", preprocessed_image.shape)
    h, w = 256, 456
    preprocessed_image = cv2.resize(preprocessed_image, (w,h))
    preprocessed_image = preprocessed_image.transpose(2,0,1)
    print("After", preprocessed_image.shape)
    preprocessed_image = preprocessed_image.reshape(1,3, h, w)
    print("After", preprocessed_image.shape)
    return preprocessed_image


def text_detection(input_image):
    '''
    Given some input image, preprocess the image so that
    it can be used with the related text detection model
    you downloaded previously. You can use cv2.resize()
    to resize the image.
    '''
    preprocessed_image = np.copy(input_image)

    # TODO: Preprocess the image for the text detection model
    h, w = 768, 1280
    preprocessed_image = cv2.resize(preprocessed_image, (w, h))
    preprocessed_image = preprocessed_image.transpose(2,0,1)
    
    return preprocessed_image


def car_meta(input_image):
    '''
    Given some input image, preprocess the image so that
    it can be used with the related car metadata model
    you downloaded previously. You can use cv2.resize()
    to resize the image.
    '''
    preprocessed_image = np.copy(input_image)

    # TODO: Preprocess the image for the car metadata model

    return preprocessed_image
