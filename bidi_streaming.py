class StreamingAgent:
    def receive(self, user_input):
        return f"Processing: {user_input}"

    def stream(self, user_input):
        response = self.receive(user_input)
        for word in response.split():
            yield word


agent = StreamingAgent()

for chunk in agent.stream("Live user input"):
    print(chunk)
