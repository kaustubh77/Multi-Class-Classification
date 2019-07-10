
# coding: utf-8

# In[1]:


import cv2
import numpy as np


# In[3]:


def transform(array_of_images):
    X = []
    for image in array_of_images:
        image = np.array(image,dtype=float)
        image = cv2.resize(image,(28,28))
        processed_image = image/255
        X.append(processed_image)
        return np.array(X)


