import mullen.video as vd
from pytube import YouTube
import moviepy.editor as mp
import shutil
import os

TEMP_DIR = 'temp/'

def download(watch_key, path=TEMP_DIR):
    yt = YouTube('https://www.youtube.com/watch?v='+watch_key)
    yt.streams.filter(
        mime_type="video/mp4", res="144p"
    ).first().download(
        filename=watch_key,output_path=path
    )
    print('Done!')
    return path+watch_key+'.mp4'
    
def generate(data_dir, recipe): 
    if not os.path.exists(TEMP_DIR):
        os.makedirs(TEMP_DIR)
    
    for wkey in recipe.keys():
        try:            
            print('Downloading %s ...' % wkey)
            fname = download(wkey) 
            print(fname)
        except:
            print('Failed to Download %s' % wkey)
        else:            
            my_clip = mp.VideoFileClip(fname,audio=False)
            i = 0
            for cut in recipe[wkey]:
                filename = '%s%s/%s_%i.mp4' % (data_dir, cut[0], wkey, i)
                print("Creating %s" % filename)
                my_clip.subclip(t_start=cut[1],t_end=cut[2]
                    ).write_videofile(filename)
                i+=1
        finally:
            shutil.rmtree(TEMP_DIR, ignore_errors=True)
            
            