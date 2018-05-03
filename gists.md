## Some video editing via terminal

### Video download from yt
```
youtube-dl url -k
```
* `-k` is to keep the file

### Video time slicing

```
ffmpeg -i in.mp4 -ss 00:01:10 -t 00:00:10 -c copy out.mp4
```

* `-ss` is the start time
* `-t` duration time

### Video resize
```
avconv -i in.mp4 -s 640x480 out.mp4
```

### Video spatial slicing

```
ffmpeg -i in.mp4 -filter:v "crop=x_q:y_q:x_s:y_s" out.mp4
```

* `x_q` is number of pixels in x direction
* `y_q` is number of pixels in y direction
* `x_s` x coord start
* `x_s` y coord start


