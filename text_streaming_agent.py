import time

def stream_response(text):
    for token in text.split():
        yield token
        time.sleep(0.2)


for token in stream_response("This is a streaming agent response"):
    print(token)
