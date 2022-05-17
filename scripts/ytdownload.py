# Youtube Downlaoder | Simer@Codeable
import os
from pytube import YouTube, Playlist

#defining colors for a user friendly environment
RED = '\033[31;2m'  # red color
BLUE = '\033[34;2m'  # blue color
GREEN = '\033[32;1m'  # green color
YELLOW = '\033[93m'  # yellow color
PINK = '\033[95m'  # ping color
PURPLE = '\033[35m'  # green color
GREY = '\033[90;1m'  # grey color
WHITE = '\033[37;1m'  # white color
END = '\033[m'  # reset to the default

#banners
header = 'lolcat -a -d 3 -p 2 "./banners/header.txt"'
utility = 'lolcat -a -d 2 -p 2 "./banners/utility.txt"'
footer = 'lolcat -a -d 3 -p 2 "./banners/footer.txt"'
os.system(header)
print()

clear = lambda: os.system('cls' if os.name == 'nt' else 'clear')


#create function to start downloading a single video
def VidDownloader():
    url = YouTube(link)
    print()
    print(GREY + "Title:", END, url.title) #display title
    print(GREY + "Views:", END, url.views) #display views
    print(GREY + "Length:", END, url.length) #display videos
    print(GREY + "Rating:", END, url.rating) #display ratings
    print()
    video = url.streams.get_highest_resolution() #set a variable to the highest resolution stream of the variable url
    video.download(filename='video.mp4') #download the video as video.mp4
    print("Thank you for using our tool, Enjoy!")


#create function to start downloading playlist
def PlaylistDownloader():
    url = Playlist(link) # set a vriable to call back on
    print()
    print(GREY + "Title:", END, url.title) #display title
    print(GREY + "Views:", END, url.views) #display views
    print(GREY + "Videos:", END, url.length) #display videos
    print()
    print(GREEN + "Starting Download!")
    videoscounter = 0 # set a variable to count how many vidoes has been downloaded
    for video in url.videos:
        print(videoscounter, '/%s downloaded' % len(url.video_urls)) #print the variable
        video.streams.get_highest_resolution().download() #download the highest resolution stream
        videoscounter = videoscounter + 1 #add 1 to the variable
    clear()
    print("Finished downloading all the videos, Enjoy!")


#url from user input
link = input(YELLOW + "Please enter your video/playlist url\n>>> " + END)

#check whether the url is valid and execute the appropriate function.
if link.startswith('https://www.youtube.com/playlist?'):
    PlaylistDownloader()
elif link.startswith('www.youtube.com/playlist?'):
    PlaylistDownloader()
elif link.startswith('youtube.com/playlist?'):
    PlaylistDownloader()
elif link.startswith('https://www.youtube.com/watch?'):
    VidDownloader()
elif link.startswith('www.youtube.com/watch?'):
    VidDownloader()
elif link.startswith('youtube.com/watch?'):
    VidDownloader()
else:
    print("Invalid URL.")

# Youtube Downlaoder | Simer@Codeable
