def tool_stream(tool_output):
    for step in tool_output:
        yield f"Tool result: {step}"


results = ["Search done", "Data processed", "Answer ready"]

for update in tool_stream(results):
    print(update)
