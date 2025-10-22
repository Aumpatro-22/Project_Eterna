"""
DOGSNIFF - Phase 1: Gemini API Integration

This module provides the core functionality for integrating with Google's Gemini API
for language model capabilities in the Project_Eterna ecosystem.
"""

import os
import google.generativeai as genai
from dotenv import load_dotenv
from typing import Optional, Dict, Any


class GeminiClient:
    """Client for interacting with Google's Gemini API."""
    
    def __init__(self, api_key: Optional[str] = None):
        """
        Initialize the Gemini client.
        
        Args:
            api_key: Optional API key. If not provided, will load from .env file.
        """
        # Load environment variables from .env file
        load_dotenv()
        
        # Use provided API key or get from environment
        self.api_key = api_key or os.getenv('GEMINI_API_KEY')
        
        if not self.api_key:
            raise ValueError(
                "Gemini API key not found. Please set GEMINI_API_KEY in .env file "
                "or pass it to the constructor."
            )
        
        # Configure the Gemini API
        genai.configure(api_key=self.api_key)
        
        # Initialize the model
        self.model = genai.GenerativeModel('gemini-pro')
    
    def generate_text(self, prompt: str, **kwargs) -> str:
        """
        Generate text using the Gemini API.
        
        Args:
            prompt: The input prompt for text generation.
            **kwargs: Additional parameters for the generation (temperature, max_tokens, etc.)
        
        Returns:
            Generated text response.
        """
        try:
            response = self.model.generate_content(prompt, **kwargs)
            return response.text
        except Exception as e:
            raise RuntimeError(f"Error generating text: {str(e)}")
    
    def analyze_text(self, text: str, analysis_type: str = "general") -> str:
        """
        Analyze text using the Gemini API.
        
        Args:
            text: The text to analyze.
            analysis_type: Type of analysis to perform (general, sentiment, summary, etc.)
        
        Returns:
            Analysis results.
        """
        analysis_prompts = {
            "general": f"Analyze the following text and provide insights:\n\n{text}",
            "sentiment": f"Analyze the sentiment of the following text:\n\n{text}",
            "summary": f"Provide a concise summary of the following text:\n\n{text}",
            "key_points": f"Extract the key points from the following text:\n\n{text}",
        }
        
        prompt = analysis_prompts.get(analysis_type, analysis_prompts["general"])
        return self.generate_text(prompt)
    
    def chat(self, message: str, conversation_history: Optional[list] = None) -> Dict[str, Any]:
        """
        Have a conversational interaction with the Gemini API.
        
        Args:
            message: The user's message.
            conversation_history: Optional list of previous messages.
        
        Returns:
            Dictionary containing the response and updated conversation history.
        """
        chat = self.model.start_chat(history=conversation_history or [])
        response = chat.send_message(message)
        
        return {
            "response": response.text,
            "history": chat.history
        }


def initialize_gemini(api_key: Optional[str] = None) -> GeminiClient:
    """
    Initialize and return a Gemini client instance.
    
    Args:
        api_key: Optional API key. If not provided, will load from .env file.
    
    Returns:
        Initialized GeminiClient instance.
    """
    return GeminiClient(api_key=api_key)
