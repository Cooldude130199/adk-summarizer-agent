from google.adk import Agent

root_agent = Agent(
    name="summarizer",
    model="publishers/google/models/gemini-2.5-pro",
    description="Text summarization agent",
    instruction="You summarize text concisely in 1-3 sentences.",
    output_key="summary"
)
