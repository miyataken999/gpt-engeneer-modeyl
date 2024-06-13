# YouTube Transcript Generator Specification

## Overview

This system generates a transcript from a YouTube video URL.

## Components

* `YouTubeAPI`: interacts with the YouTube API to retrieve video captions
* `TranscriptGenerator`: generates a transcript from a YouTube video URL
* `TranscriptCorrector`: corrects the generated transcript

## Sequence Diagram

@startuml
participant YouTubeAPI as ya
participant TranscriptGenerator as tg
participant TranscriptCorrector as tc

ya -> tg: get_video_id(url)
tg -> ya: video_id
ya -> tg: get_video_transcript(video_id)
tg -> ya: transcript
tg -> tc: correct_transcript(transcript)
tc -> tg: corrected_transcript
@enduml