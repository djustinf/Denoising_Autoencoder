'''
Justin Foxhoven
3/17/18
'''

import cv2
import _thread
import numpy as np

def create_noise(img, fract):
  corrupt_image = img.copy()

  x_shape = img.shape[0]
  y_shape = img.shape[1]
  img_max = img.max()
  img_min = img.min()

  for i,x in enumerate(img):
    noise = np.random.randint(0, y_shape, int(fract*x_shape))
    for j in noise:
      corrupt_image[i][j] = img_max if (np.random.random() < 0.5) else img_min

  return corrupt_image

def display_img(name, img):
  cv2.imshow(name, img)
  cv2.waitKey(0)

def noise_and_compare(img, fract):
  display_img('Good Image', img)
  display_img('Noisy Image', create_noise(img, fract))
