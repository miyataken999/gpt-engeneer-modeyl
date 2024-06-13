from youtube_api import YouTubeAPI

class TranscriptGenerator:
    def __init__(self, youtube_api):
        self.youtube_api = youtube_api

    def generate_transcript(self, url):
        video_id = self.youtube_api.get_video_id(url)
        transcript = self.youtube_api.get_video_transcript(video_id)
        return transcript