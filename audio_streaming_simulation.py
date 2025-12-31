import time

audio_chunks = ["audio_chunk_1", "audio_chunk_2", "audio_chunk_3"]

def audio_stream(chunks):
    for chunk in chunks:
        yield chunk
        time.sleep(0.3)


for audio in audio_stream(audio_chunks):
    print("Sending:", audio)
