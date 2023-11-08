import pyaudio
import boto3

# Create a client object for the Amazon Polly service
polly_client = boto3.client('polly', region_name='us-east-1')

# Set the text to synthesize
text = "Hello, world!"

# Set the voice to use
voice_id = "Joanna"

# Synthesize the speech
response = polly_client.synthesize_speech(Text=text, VoiceId=voice_id)

# Create a PyAudio object
audio = pyaudio.PyAudio()

# Open a stream for playing the synthesized speech
stream = audio.open(format=audio.get_format_from_width(response.AudioStream.read(1)),
                   channels=1,
                   rate=response.SampleRate,
                   output=True)

# Read the synthesized speech data from the AudioStream object
data = response.AudioStream.read()

# Write the synthesized speech data to the stream
stream.write(data)

# Close the stream
stream.stop_stream()
stream.close()

# Close the PyAudio object
audio.terminate()