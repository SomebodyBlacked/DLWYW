from pytubefix import YouTube
import sys

if len(sys.argv) < 2:
  print("Usage: python main.py <YouTube URL>")
  sys.exit(1)

url = sys.argv[1]

yt = YouTube(url)
print(yt.title)
yt.streams.get_highest_resolution().download()
