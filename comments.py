import googleapiclient.discovery
import creds

api_service_name = "youtube"
api_version = "v3"
DEVELOPER_KEY = creds.apiKey

youtube = googleapiclient.discovery.build(
        api_service_name, api_version, developerKey = DEVELOPER_KEY)

# Fetching comment threads of all videos
def getComments(video):
    commentInfoReq = youtube.commentThreads().list(
        part="snippet,replies",
        maxResults=100,
        textFormat="plainText",
        videoId=video
    )
    commentInfoRes = commentInfoReq.execute()
    
    # For comments spread across multiple pages
    nextPageToken = commentInfoRes.get('nextPageToken')
    morePagesExist = True

    while morePagesExist:
        if nextPageToken is None:
            morePagesExist = False
        else:
            nextPagecommentInfoReq = youtube.commentThreads().list(
                part="snippet,replies",
                videoId=video,
                maxResults=100,
                textFormat="plainText",
                pageToken=nextPageToken
            )
            nextPagecommentInfoRes = nextPagecommentInfoReq.execute()
            commentInfoRes['items'].append(nextPagecommentInfoRes['items'])
            nextPageToken = nextPagecommentInfoRes.get('nextPageToken')

    return(commentInfoRes)