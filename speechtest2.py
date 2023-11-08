from google.cloud import texttospeech

# Set up the client
client = texttospeech.TextToSpeechClient()

# Set the voice and text input
voice = texttospeech.VoiceSelectionParams(
    language_code="en-US",
    name="en-US-Wavenet-A",
)

synthesis_input = texttospeech.SynthesisInput(text="Hello, world!")

# Generate the speech and write it to an audio file
response = client.synthesize_speech(input=synthesis_input, voice=voice)
with open("output.mp3", "wb") as output:
    output.write(response.audio_content)