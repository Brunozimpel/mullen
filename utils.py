"""Usefull functions to manipulate, read, write and plot images"""

import os
import matplotlib.pyplot as plt

def get_sample(num, img_dir='samples/img/'):
    """Quick alias to get the image in the correct path"""
    file_path = '%ss%i.jpg' % (img_dir, num)
    if os.path.exists(file_path):
        return file_path
    else:
        raise ValueError('File not found')

def plot_single_image(img, fsize=(7,5), axis=False):
	plt.figure(figsize=fsize)
	plt.imshow(img)
	if not axis:
		plt.axis('off')


def plot_side_by_side(imgs, fsize=(15,10), axis=False):
	"""Plot two images side by side"""
	plt.figure(figsize=fsize)
	for i in [0,1]:
		plt.subplot(1,2,i+1)
		plt.imshow(imgs[i])
		if not axis:
			plt.axis('off')

