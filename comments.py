import googleapiclient.discovery
import creds

api_service_name = "youtube"
api_version = "v3"
DEVELOPER_KEY = creds.apiKey

youtube = googleapiclient.discovery.build(
        api_service_name, api_version, developerKey = DEVELOPER_KEY)

# Fetching comment threads of all videos

def getComments(video):
    commentData=[]

    commentInfoReq = youtube.commentThreads().list(
        part="snippet,replies",
        maxResults=50,
        videoId=video
    )
    commentInfoRes = commentInfoReq.execute()
    
    commentNo = 1
    
    for i in range(len(commentInfoRes['items'])):
        repliesDetails = {}
        if 'replies' in commentInfoRes['items'][i]:
            for j in range(len(commentInfoRes['items'][i]['replies']['comments'])):
                repliesDetails = dict(replierName = commentInfoRes['items'][i]['replies']['comments'][j]['snippet']['authorDisplayName'],
                                    date = commentInfoRes['items'][i]['replies']['comments'][j]['snippet']['publishedAt'],
                                    commentText = commentInfoRes['items'][i]['replies']['comments'][j]['snippet']['textDisplay'],
                                    likesCount = commentInfoRes['items'][i]['replies']['comments'][j]['snippet']['likeCount'])

        commentDetails = dict(commentSNo = commentNo,
                            authorName = commentInfoRes['items'][i]['snippet']['topLevelComment']['snippet']['authorDisplayName'],
                            date = commentInfoRes['items'][i]['snippet']['topLevelComment']['snippet']['publishedAt'],
                            commentText = commentInfoRes['items'][i]['snippet']['topLevelComment']['snippet']['textDisplay'],
                            likesCount = commentInfoRes['items'][i]['snippet']['topLevelComment']['snippet']['likeCount'],
                            replies = repliesDetails)
        
        commentNo+=1

        commentData.append(commentDetails)

    # For comments spread across multiple pages

    nextPageToken = commentInfoRes.get('nextPageToken')
    morePagesExist = True

    while morePagesExist:
        if nextPageToken is None:
            morePagesExist = False
        else:
            commentInfoReq = youtube.commentThreads().list(
                part="snippet,replies",
                maxResults=50,
                videoId=video,
                pageToken=nextPageToken
            )
            commentInfoRes = commentInfoReq.execute()

            for i in range(len(commentInfoRes['items'])):
                commentDetails = dict(commentSNo = commentNo,
                            authorName = commentInfoRes['items'][i]['snippet']['topLevelComment']['snippet']['authorDisplayName'],
                            date = commentInfoRes['items'][i]['snippet']['topLevelComment']['snippet']['publishedAt'],
                            commentText = commentInfoRes['items'][i]['snippet']['topLevelComment']['snippet']['textDisplay'],
                            likesCount = commentInfoRes['items'][i]['snippet']['topLevelComment']['snippet']['likeCount'])
        
                if 'replies' in commentInfoRes['items'][i]:
                    for j in range(len(commentInfoRes['items'][i]['replies']['comments'])):
                        repliesDetails = dict(replierName = commentInfoRes['items'][i]['replies']['comments'][j]['snippet']['authorDisplayName'],
                                    date = commentInfoRes['items'][i]['replies']['comments'][j]['snippet']['publishedAt'],
                                    commentText = commentInfoRes['items'][i]['replies']['comments'][j]['snippet']['textDisplay'],
                                    likesCount = commentInfoRes['items'][i]['replies']['comments'][j]['snippet']['likeCount'])
                commentNo+=1

                commentData.append(commentDetails)

            nextPageToken = commentInfoRes.get('nextPageToken')


    return(commentData)