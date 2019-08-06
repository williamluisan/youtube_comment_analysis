# -*- coding: utf-8 -*-

'''
Kode testing 1

Tes mengambil data komentar di youtube
pada video terkait. Tetapi pengambilan data ini
tidak live stream
'''

# Sample Python code for youtube.commentThreads.list
# See instructions for running these code samples locally:
# https://developers.google.com/explorer-help/guides/code_samples#python

import os, json

import googleapiclient.discovery

def main():
    # Disable OAuthlib's HTTPS verification when running locally.
    # *DO NOT* leave this option enabled in production.
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    api_service_name = "youtube"
    api_version = "v3"
    DEVELOPER_KEY = "AIzaSyBKrZsjpGpFp5CPwFFt4eEd9GjBM5EUA0g"

    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, developerKey = DEVELOPER_KEY)

    request = youtube.commentThreads().list(
        part="id, snippet",
        maxResults=1000,
        videoId="HLkZNGl101k"
    )
    response = request.execute()

    for v1 in response['items']:
        print(v1['snippet']['topLevelComment']['snippet']['textOriginal'], "\n")

if __name__ == "__main__":
    main()