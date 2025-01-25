from deepgram import DeepgramClient, PrerecordedOptions

DEEPGRAM_API_KEY = "YOUR_SECRET"

AUDIO_URL = {
    "url": "https://static.deepgram.com/examples/Bueller-Life-moves-pretty-fast.wav"
}

def main():
    try:
        deepgram = DeepgramClient(DEEPGRAM_API_KEY)

        options = PrerecordedOptions(
            model="nova-2",
            language="en",
            smart_format=True,
            punctuate=True,
            paragraphs=True,
            utterances=True,
        )

        response = deepgram.listen.prerecorded.v("1").transcribe_url(AUDIO_URL, options)
        print(response.to_json(indent=4))

    except Exception as e:
        print(f"Exception: {e}")

if __name__ == "__main__":
    main()