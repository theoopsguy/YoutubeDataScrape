import videoInfo
import comments
import channelId
import YTvideoList
import videoInfo

# Get list of ids of all videos in uploads playlist of a youtube channel
videoList = YTvideoList.getvideoIdList(channelId.channelId)

#Prints json containing info about n videos
for idx in range(len(videoList)):
    print(videoInfo.getVideoInfo(videoList[idx]))
    print(comments.getComments(videoList[idx]))
