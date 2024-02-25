#!/usr/bin/env python
# coding: utf-8

# In[13]:


import cv2
import numpy as np
import matplotlib.pyplot as plt
img=cv2.imread('flower.jpg')
img_RGB=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
img_HSV=cv2.cvtColor(img_RGB,cv2.COLOR_RGB2HSV)
lower=np.array([0,0,210])
upper =np.array([255,255,255])
mask = cv2.inRange(img_HSV,lower,upper)
plt.imshow(mask)


# In[8]:


res=cv2.bitwise_and(img_RGB,img_RGB,mask=mask)
plt.imshow(res)


# In[14]:


img2 = img_RGB.copy()
img2[mask > 0] = [50,0,0]
img3 = cv2.addWeighted( res, 0.7, img2,1,5, res);

plt.imshow(img3)
img3=cv2.cvtColor(img3,cv2.COLOR_BGR2RGB)
cv2.imwrite('newimg.jpg', img3)


# In[ ]:




