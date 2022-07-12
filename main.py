import googleapiclient.discovery
import creds
import channelId
import comments

api_service_name = "youtube"
api_version = "v3"
DEVELOPER_KEY = creds.apiKey

youtube = googleapiclient.discovery.build(
        api_service_name, api_version, developerKey = DEVELOPER_KEY)

# Fetching channel details

channelInfoReq = youtube.channels().list(
        part="contentDetails",
        id=channelId.channelId
    )
channelInfoRes = channelInfoReq.execute()

# Fetching uploaded video details which will be present in uploads playlist

uploadsPlaylistId = channelInfoRes['items'][0]['contentDetails']['relatedPlaylists']['uploads']

playlistInfoReq = youtube.playlistItems().list(
        part="contentDetails",
        maxResults=10,
        playlistId=uploadsPlaylistId
    )
playlistInfoRes = playlistInfoReq.execute()

videoIdList = []

for idx in range(len(playlistInfoRes['items'])):
    videoIdList.append(playlistInfoRes['items'][idx]['contentDetails']['videoId'])

# Fetching details of all videoIds in the videoIdList

videoDetails = []

videoInfoReq = youtube.videos().list(
        part="snippet,contentDetails,statistics",
        id=','.join(videoIdList[0:10])
    )
videoInfoRes = videoInfoReq.execute()

for idx in range(len(videoInfoRes['items'])):
    videoData = dict(titleName = videoInfoRes['items'][idx]['snippet']['title'],
                    datePublished = videoInfoRes['items'][idx]['snippet']['publishedAt'],
                    duration = videoInfoRes['items'][idx]['contentDetails']['duration'],
                    viewsCount = videoInfoRes['items'][idx]['statistics']['viewCount'],
                    likesCount = videoInfoRes['items'][idx]['statistics']['likeCount'], 
                    commentsCount = videoInfoRes['items'][idx]['statistics']['commentCount'],
                    comments = comments.getComments(videoInfoRes['items'][idx]['id']))

    videoDetails.append(videoData)

print(videoDetails)