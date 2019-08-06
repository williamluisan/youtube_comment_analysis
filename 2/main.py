import os, json, re
import googleapiclient.discovery

def main():
    # Disable OAuthlib's HTTPS verification when running locally.
    # *DO NOT* leave this option enabled in production.
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    api_service_name = "youtube"
    api_version = "v3"
    DEVELOPER_KEY = "AIzaSyBKrZsjpGpFp5CPwFFt4eEd9GjBM5EUA0g"

    # membuat google api (youtube) instance
    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, developerKey = DEVELOPER_KEY
    )

    # melakukan request
    request = youtube.commentThreads().list(
        part="id, snippet",
        maxResults=10,
        videoId="HLkZNGl101k"
    )
    response = request.execute()

    # pre-processing data
    regex = re.compile("[^a-zA-Z0-9\s]")
    for v1 in response['items']:
        comment = v1['snippet']['topLevelComment']['snippet']['textOriginal']   # mengambil komentar dari request api
        comment = regex.sub('', comment)                                        # mengganti char yang tidak diinginkan dengan ''
        comment = comment.lower()                                               # membuat semua char menjadi lowercase    
        print(comment)

if __name__ == "__main__":
    main()