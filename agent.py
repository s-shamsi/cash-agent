import json
import logging
import anthropic

logger = logging.getLogger(__name__)

def run_optimization_agent(api_key: str, prompt: str, system_instruction: str) -> dict:
    """
    Executes the optimization prompt against the Claude API and returns verified JSON data.
    """
    if not api_key:
        raise ValueError("Anthropic API key is required but missing.")

    client = anthropic.Anthropic(api_key=api_key)
    
    try:
        response = client.messages.create(
            model="claude-3-5-sonnet-20241022",
            max_tokens=1200,
            temperature=0.0,  # Explicitly low for deterministic financial JSON
            system=system_instruction,
            messages=[{"role": "user", "content": prompt}]
        )
        
        raw_text = response.content[0].text.strip()
        return json.loads(raw_text)
        
    except anthropic.APIError as e:
        logger.error(f"Anthropic API exception: {e}")
        return {"error": f"API failure: {str(e)}"}
    except json.JSONDecodeError:
        logger.error(f"Failed to parse model response as JSON. Raw output: {raw_text}")
        return {"error": "Invalid payload format returned from model"}
