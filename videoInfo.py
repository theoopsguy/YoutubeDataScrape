import googleapiclient.discovery
import creds
import comments

api_service_name = "youtube"
api_version = "v3"
DEVELOPER_KEY = creds.apiKey

youtube = googleapiclient.discovery.build(
        api_service_name, api_version, developerKey = DEVELOPER_KEY)

# Fetching video details
def getVideoInfo(video_id):
    videoInfoReq = youtube.videos().list(
        part="snippet,contentDetails,statistics",
        id=video_id
    )
    videoInfoRes = videoInfoReq.execute()

    return(videoInfoRes)
