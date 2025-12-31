class ContextStreamingAgent:
    def __init__(self):
        self.context = []

    def stream(self, input_text):
        self.context.append(input_text)
        for item in self.context:
            yield f"Context: {item}"


agent = ContextStreamingAgent()

for msg in agent.stream("User asks for advice"):
    print(msg)
