import googleapiclient.discovery
import creds
import comments

api_service_name = "youtube"
api_version = "v3"
DEVELOPER_KEY = creds.apiKey

youtube = googleapiclient.discovery.build(
        api_service_name, api_version, developerKey = DEVELOPER_KEY)

def getvideoIdList(channel_id):
    channelInfoReq = youtube.channels().list(
        part="contentDetails",
        id=channel_id
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

    # Generate a list of ids of the 10 videos in uploads playlist
    videoIdList = []

    for idx in range(len(playlistInfoRes['items'])):
        videoIdList.append(playlistInfoRes['items'][idx]['contentDetails']['videoId'])

    return videoIdList