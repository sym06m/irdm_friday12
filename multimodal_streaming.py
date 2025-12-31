def multimodal_stream(text, audio):
    for t, a in zip(text, audio):
        yield {"text": t, "audio": a}


text_stream = ["Hello", "this", "is", "live"]
audio_stream = ["a1", "a2", "a3", "a4"]

for data in multimodal_stream(text_stream, audio_stream):
    print(data)
