class Video:
    def __init__(self,title,link):
        self.title = title
        self.link = link
def read_video():
    title  = input("Enter title: ")
    link  = input("Enter url: ")
    video = Video(title,link)
    return video 
def read_videos():
    videos = []
    total_video = input("Enter how many videos:")
    for i in range(int(total_video)):
        print("Enter video ",i+1)
        vid = read_video()
        videos.append(vid)
    return videos
    
def print_video(video):
    print("Video title: ",video.title)
    print("Video url: ",video.link)
    

def print_videos(videos):
    for i in range(len(videos)):
        print_video(videos[i])
def main():
    vids = read_videos()
    print_video(vids[0])
    print("xxxxxxxxxxxxxxxxxxxx")
    print_videos(vids)
main()