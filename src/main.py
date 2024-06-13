from transcript_generator import TranscriptGenerator
from transcript_corrector import TranscriptCorrector

def main():
    api_key = 'YOUR_API_KEY'
    youtube_api = YouTubeAPI(api_key)
    generator = TranscriptGenerator(youtube_api)
    corrector = TranscriptCorrector()
    url = 'https://www.youtube.com/watch?v=dQw4w9WgXcQ'
    transcript = generator.generate_transcript(url)
    corrected_transcript = corrector.correct_transcript(transcript)
    print(corrected_transcript)

if __name__ == '__main__':
    main()