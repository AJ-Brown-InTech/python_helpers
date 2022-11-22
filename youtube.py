#download youtube videos

#pip3 install pytube
import pytube

link = input("Enter a YouTube video url/link(recommend copy & paste): ")
yt = pytube.YouTube(link)
yt.streams.first().download()
print('Downloaded', link)