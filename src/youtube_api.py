import os
import json
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

class YouTubeAPI:
    def __init__(self, api_key):
        self.api_key = api_key
        self.youtube = build('youtube', 'v3', developerKey=self.api_key)

    def get_video_id(self, url):
        # Extract video ID from URL
        video_id = url.split('?v=')[-1]
        return video_id

    def get_video_transcript(self, video_id):
        request = self.youtube.captions().list(
            part="id,snippet",
            videoId=video_id
        )
        response = request.execute()
        captions = response['items']
        for caption in captions:
            if caption['snippet']['languageCode'] == 'ja':
                caption_id = caption['id']
                break
        request = self.youtube.captions().get(
            id=caption_id
        )
        response = request.execute()
        transcript = response['snippet']['textBody']
        return transcript