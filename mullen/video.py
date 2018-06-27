import cv2
import os
import numpy as np
import moviepy.editor as mp
import math

def video_to_array(filepath):
    """Returns the video as a numpy array"""
    cap = cv2.VideoCapture(filepath)
    total_frames=int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    return np.array([cap.read()[1] for i in range(total_frames)])

def downsample(frame_array, num_samples):
    """Reduce the number of frames of a video to num_samples frames"""
    total_frames = frame_array.shape[0]
    step = total_frames/ num_samples
    if step <= 1:        
        return frame_array
    else:
        return np.array(
            [frame_array[i] for i in map(lambda x: int(round(x)), np.arange(0,total_frames, step))]
        )
    
def resize(video, size=(250,140), remove=True):
    clip = mp.VideoFileClip(video,audio=False)
    clip_resized = clip.resize(size)
    clip_resized.write_videofile(video[:-4]+'.mp4')
    if remove:
        os.remove(video)


if __name__ == "__main__":
    pass