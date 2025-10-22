"""
Example demonstration of DOGSNIFF Phase 1 capabilities.

This file demonstrates how to use the Gemini API integration
without requiring an actual API key (for documentation purposes).
"""

from gemini_client import GeminiClient


def demonstrate_usage():
    """Demonstrate the usage of GeminiClient with examples."""
    
    print("=" * 70)
    print("DOGSNIFF Phase 1 - Gemini API Integration Examples")
    print("=" * 70)
    print()
    
    # Example 1: Initialization
    print("1. INITIALIZATION")
    print("-" * 70)
    print("# Initialize with API key from .env file:")
    print("client = initialize_gemini()")
    print()
    print("# Or initialize with explicit API key:")
    print("client = GeminiClient(api_key='your_api_key_here')")
    print()
    
    # Example 2: Text Generation
    print("2. TEXT GENERATION")
    print("-" * 70)
    print("# Generate meaningful text about memories:")
    print("response = client.generate_text(")
    print('    "What makes memories precious and worth preserving?"')
    print(")")
    print()
    print("Example response:")
    print("\"Memories are precious because they capture moments that define")
    print("who we are. They connect us to our past, help us understand our")
    print("present, and guide us toward our future...\"")
    print()
    
    # Example 3: Sentiment Analysis
    print("3. SENTIMENT ANALYSIS")
    print("-" * 70)
    print("# Analyze the emotional tone of a memory:")
    print("text = 'I remember the day we spent together at the beach...'")
    print("analysis = client.analyze_text(text, analysis_type='sentiment')")
    print()
    print("Example response:")
    print("\"The text conveys a positive and nostalgic sentiment,")
    print("characterized by warmth and fond remembrance...\"")
    print()
    
    # Example 4: Text Summarization
    print("4. TEXT SUMMARIZATION")
    print("-" * 70)
    print("# Summarize a long memory or story:")
    print("story = 'A long story about a meaningful life event...'")
    print("summary = client.analyze_text(story, analysis_type='summary')")
    print()
    print("Example response:")
    print("\"Key points: Family gathering, celebration of life,")
    print("shared memories, emotional connection, legacy...\"")
    print()
    
    # Example 5: Key Points Extraction
    print("5. KEY POINTS EXTRACTION")
    print("-" * 70)
    print("# Extract key themes from a narrative:")
    print("narrative = 'The project celebrates connection and healing...'")
    print("key_points = client.analyze_text(narrative, analysis_type='key_points')")
    print()
    print("Example response:")
    print("\"• Connection and healing")
    print(" • Digital preservation")
    print(" • Honoring loved ones")
    print(" • Timeless remembrance\"")
    print()
    
    # Example 6: Conversational AI
    print("6. CONVERSATIONAL AI")
    print("-" * 70)
    print("# Have a conversation about memories:")
    print("result = client.chat('How can I preserve my family stories?')")
    print("print(result['response'])")
    print()
    print("# Continue the conversation:")
    print("result = client.chat(")
    print("    'What about photos and videos?',")
    print("    conversation_history=result['history']")
    print(")")
    print()
    
    # Example 7: Advanced Usage
    print("7. ADVANCED USAGE")
    print("-" * 70)
    print("# Custom generation parameters:")
    print("response = client.generate_text(")
    print("    prompt='Tell me about preserving memories',")
    print("    temperature=0.7,  # Control creativity")
    print("    max_tokens=500    # Limit response length")
    print(")")
    print()
    
    print("=" * 70)
    print("For more information, see DOGSNIFF.md")
    print("=" * 70)


if __name__ == "__main__":
    demonstrate_usage()
