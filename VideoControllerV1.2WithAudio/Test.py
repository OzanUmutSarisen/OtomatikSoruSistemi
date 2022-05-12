from moviepy.editor import *
from pafy import pafy

video = pafy.new("https://www.youtube.com/watch?v=azPJGYvGFto&list=RDazPJGYvGFto&start_radio=1")
stream = video.getbest(preftype='mp4')

video = VideoFileClip(stream.url)
audio = video.audio
for t, video_frame in video.iter_frames(with_times=True):
    audio_frame = audio.get_frame(t)
    print(audio_frame)
    print(video_frame)