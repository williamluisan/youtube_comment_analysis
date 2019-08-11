import config
import sys, os, json, datetime
import googleapiclient.discovery

class Fetch:
    def main(self):
        # Disable OAuthlib's HTTPS verification when running locally.
        # *DO NOT* leave this option enabled in production.
        os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

        # variabel google API
        api_service_name = "youtube"
        api_version = "v3"
        DEVELOPER_KEY = config.DEVELOPER_KEY
        VIDEO_ID = config.YOUTUBE_VIDEO_ID

        # membuat google api (youtube) instance
        youtube = googleapiclient.discovery.build(
            api_service_name, api_version, developerKey = DEVELOPER_KEY
        )

        # melakukan request by total_page_request (1 page = 100 comments)
        file                = open('data/' + str(datetime.datetime.now().date()) + '_comment_' + VIDEO_ID + '.txt', 'a', encoding="utf8")
        total_page_request  = config.TOTAL_PAGE_REQUEST
        next_page_token     = ''
        for i in range(0, total_page_request):
            print("Mengerjakan request API #" + str(i+1) + " dari #" + str(total_page_request) + "...")

            request = youtube.commentThreads().list(
                part = "id, snippet",
                maxResults = 100,
                videoId = VIDEO_ID,
                textFormat = "plainText",
                pageToken = next_page_token
            )
            response = request.execute()

            # pre-process-1 data komentar yang diambil
            all_comments = ''
            for v in response['items']:
                comment = v['snippet']['topLevelComment']['snippet']['textOriginal']    # mengambil komentar dari request api
                comment = comment.replace("\n", ' ') + "\n\n"                           # menghilangkan newline pada komentar
                all_comments += comment

            file.write(all_comments)

            next_page_token = response['nextPageToken']

        # simpan semua komentar kedalam file
        next_page_token = "Next page token: " + next_page_token     # menyimpan next_page_token terakhir di akhir file
        file.write(next_page_token)
        file.close()
        print("Selesai !")

if __name__ == "__main__":
    Fetch().main()