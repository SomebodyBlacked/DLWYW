from pytubefix import YouTube
import sys

if len(sys.argv) < 2:
  print("Error: Please provide a YouTube URL as an argument.")
  sys.exit(1)

url = sys.argv[1]

yt = YouTube(url)
print(yt.title)
yt.streams.get_highest_resolution().download()
