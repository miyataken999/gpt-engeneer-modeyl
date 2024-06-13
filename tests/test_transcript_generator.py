import unittest
from transcript_generator import TranscriptGenerator

class TestTranscriptGenerator(unittest.TestCase):
    def test_generate_transcript(self):
        youtube_api = YouTubeAPI('YOUR_API_KEY')
        generator = TranscriptGenerator(youtube_api)
        url = 'https://www.youtube.com/watch?v=dQw4w9WgXcQ'
        transcript = generator.generate_transcript(url)
        self.assertIsNotNone(transcript)

if __name__ == '__main__':
    unittest.main()