"""
DOGSNIFF - Main Application Entry Point

This is the main entry point for the DOGSNIFF application in Phase 1.
It demonstrates how to use the Gemini API integration for text analysis
and generation capabilities.
"""

import sys
from gemini_client import initialize_gemini


def main():
    """Main application function."""
    print("=" * 60)
    print("DOGSNIFF - Phase 1: Gemini API Integration")
    print("Project_Eterna Memory Preservation System")
    print("=" * 60)
    print()
    
    try:
        # Initialize the Gemini client
        print("Initializing Gemini API client...")
        client = initialize_gemini()
        print("✓ Gemini client initialized successfully!")
        print()
        
        # Example 1: Simple text generation
        print("-" * 60)
        print("Example 1: Text Generation")
        print("-" * 60)
        prompt = "What is the importance of preserving memories and honoring loved ones?"
        print(f"Prompt: {prompt}")
        print()
        response = client.generate_text(prompt)
        print(f"Response:\n{response}")
        print()
        
        # Example 2: Text analysis
        print("-" * 60)
        print("Example 2: Text Analysis")
        print("-" * 60)
        sample_text = """
        This project was born from a desire to preserve memories beyond loss. 
        It offers a digital space where stories, emotions, and legacies live on—
        allowing loved ones to be remembered, honored, and felt. A tribute to 
        connection, healing, and the timeless power of remembrance.
        """
        print(f"Text to analyze: {sample_text.strip()}")
        print()
        analysis = client.analyze_text(sample_text, analysis_type="sentiment")
        print(f"Sentiment Analysis:\n{analysis}")
        print()
        
        # Example 3: Key points extraction
        print("-" * 60)
        print("Example 3: Key Points Extraction")
        print("-" * 60)
        key_points = client.analyze_text(sample_text, analysis_type="key_points")
        print(f"Key Points:\n{key_points}")
        print()
        
        print("=" * 60)
        print("DOGSNIFF Phase 1 completed successfully!")
        print("=" * 60)
        
    except ValueError as e:
        print(f"Configuration Error: {e}")
        print()
        print("Please ensure you have:")
        print("1. Created a .env file based on .env.example")
        print("2. Added your Gemini API key to the .env file")
        print("3. Get your API key from: https://makersuite.google.com/app/apikey")
        sys.exit(1)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
