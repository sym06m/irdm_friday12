class StreamController:
    def start(self):
        print("Stream started")

    def stop(self):
        print("Stream stopped")


controller = StreamController()
controller.start()
print("Streaming data...")
controller.stop()
