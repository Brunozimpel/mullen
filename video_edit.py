import cv2
import fire
import os

def split_to_frames(video, path, prefix):
	if not os.path.exists(path):
		os.makedirs(path)

	vidcap = cv2.VideoCapture(video)
	success,image = vidcap.read()
	count = 0
	while success:
		cv2.imwrite(path + prefix +"%d.jpg" % count, image)     # save frame as JPEG file
		success,image = vidcap.read()
		print(count, end='\r')
		count += 1
	print('Done!')

if __name__ == "__main__":
	fire.Fire(split_to_frames)
