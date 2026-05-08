import anthropic
import json

def run_optimization_agent(api_key, prompt, backend):
    client = anthropic.Anthropic(api_key=api_key)
    # This is a simplified version for easy uploading
    response = client.messages.create(
        model="claude-3-5-sonnet-20241022",
        max_tokens=1000,
        system="You are a financial agent. Output only JSON.",
        messages=[{"role": "user", "content": prompt}]
    )
    return json.loads(response.content[0].text)