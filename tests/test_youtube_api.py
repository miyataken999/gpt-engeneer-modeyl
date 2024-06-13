import unittest
from youtube_api import YouTubeAPI

class TestYouTubeAPI(unittest.TestCase):
    def test_get_video_id(self):
        api_key = 'YOUR_API_KEY'
        youtube_api = YouTubeAPI(api_key)
        url = 'https://www.youtube.com/watch?v=dQw4w9WgXcQ'
        video_id = youtube_api.get_video_id(url)
        self.assertEqual(video_id, 'dQw4w9WgXcQ')

    def test_get_video_transcript(self):
        api_key = 'YOUR_API_KEY'
        youtube_api = YouTubeAPI(api_key)
        video_id = 'dQw4w9WgXcQ'
        transcript = youtube_api.get_video_transcript(video_id)
        self.assertIsNotNone(transcript)

if __name__ == '__main__':
    unittest.main()