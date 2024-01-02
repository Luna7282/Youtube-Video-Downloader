from pytube import YouTube
import sys
import wget
wget.download('http://download.geonames.org/export/zip/US.zip') # it is the loader... You can change it to any other loader you want
 
# total arguments
link = sys.argv[1]

# print("Enter The YT Video Link below ↓  ")
# link = input("")
yt = YouTube(link)        # provide the link in the box 

print("\nVideo Title : ",yt.title)
print("\nThumbnail Downlod Link : ",yt.thumbnail_url)
print("\nVideo Views : ",yt.views)


yd = yt.streams.get_highest_resolution()
yd.download()  # paste the path where you want to save the video
