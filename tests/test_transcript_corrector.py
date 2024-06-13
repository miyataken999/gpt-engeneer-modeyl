import unittest
from transcript_corrector import TranscriptCorrector

class TestTranscriptCorrector(unittest.TestCase):
    def test_correct_transcript(self):
        corrector = TranscriptCorrector()
        transcript = 'Hello,\nWorld!'
        corrected_transcript = corrector.correct_transcript(transcript)
        self.assertEqual(corrected_transcript, 'Hello World')

if __name__ == '__main__':
    unittest.main()