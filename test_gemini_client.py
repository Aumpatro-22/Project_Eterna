"""
Test suite for DOGSNIFF Phase 1 - Gemini API Integration

This file contains basic tests to verify the structure and functionality
of the Gemini client implementation.
"""

import unittest
from unittest.mock import patch, MagicMock
import os
import sys

# Add parent directory to path for imports
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from gemini_client import GeminiClient, initialize_gemini


class TestGeminiClient(unittest.TestCase):
    """Test cases for GeminiClient class."""
    
    @patch.dict(os.environ, {'GEMINI_API_KEY': 'test_api_key'})
    @patch('gemini_client.genai')
    def test_init_with_env_key(self, mock_genai):
        """Test initialization with API key from environment."""
        client = GeminiClient()
        self.assertEqual(client.api_key, 'test_api_key')
        mock_genai.configure.assert_called_once_with(api_key='test_api_key')
    
    @patch('gemini_client.genai')
    def test_init_with_provided_key(self, mock_genai):
        """Test initialization with provided API key."""
        client = GeminiClient(api_key='provided_key')
        self.assertEqual(client.api_key, 'provided_key')
        mock_genai.configure.assert_called_once_with(api_key='provided_key')
    
    @patch.dict(os.environ, {}, clear=True)
    def test_init_without_key_raises_error(self):
        """Test that initialization without API key raises ValueError."""
        with self.assertRaises(ValueError) as context:
            GeminiClient()
        self.assertIn('Gemini API key not found', str(context.exception))
    
    @patch.dict(os.environ, {'GEMINI_API_KEY': 'test_key'})
    @patch('gemini_client.genai')
    def test_generate_text(self, mock_genai):
        """Test text generation method."""
        # Setup mock
        mock_model = MagicMock()
        mock_response = MagicMock()
        mock_response.text = "Generated text response"
        mock_model.generate_content.return_value = mock_response
        mock_genai.GenerativeModel.return_value = mock_model
        
        # Test
        client = GeminiClient()
        result = client.generate_text("Test prompt")
        
        self.assertEqual(result, "Generated text response")
        mock_model.generate_content.assert_called_once_with("Test prompt")
    
    @patch.dict(os.environ, {'GEMINI_API_KEY': 'test_key'})
    @patch('gemini_client.genai')
    def test_analyze_text_sentiment(self, mock_genai):
        """Test text analysis with sentiment type."""
        # Setup mock
        mock_model = MagicMock()
        mock_response = MagicMock()
        mock_response.text = "Sentiment analysis result"
        mock_model.generate_content.return_value = mock_response
        mock_genai.GenerativeModel.return_value = mock_model
        
        # Test
        client = GeminiClient()
        result = client.analyze_text("Test text", analysis_type="sentiment")
        
        self.assertEqual(result, "Sentiment analysis result")
        # Verify the prompt contains the text
        call_args = mock_model.generate_content.call_args[0][0]
        self.assertIn("Test text", call_args)
        self.assertIn("sentiment", call_args.lower())
    
    @patch.dict(os.environ, {'GEMINI_API_KEY': 'test_key'})
    @patch('gemini_client.genai')
    def test_chat(self, mock_genai):
        """Test chat method."""
        # Setup mock
        mock_model = MagicMock()
        mock_chat = MagicMock()
        mock_response = MagicMock()
        mock_response.text = "Chat response"
        mock_chat.send_message.return_value = mock_response
        mock_chat.history = []
        mock_model.start_chat.return_value = mock_chat
        mock_genai.GenerativeModel.return_value = mock_model
        
        # Test
        client = GeminiClient()
        result = client.chat("Hello")
        
        self.assertEqual(result["response"], "Chat response")
        self.assertIn("history", result)
        mock_model.start_chat.assert_called_once()
        mock_chat.send_message.assert_called_once_with("Hello")
    
    @patch.dict(os.environ, {'GEMINI_API_KEY': 'test_key'})
    @patch('gemini_client.genai')
    def test_initialize_gemini(self, mock_genai):
        """Test initialize_gemini helper function."""
        client = initialize_gemini()
        self.assertIsInstance(client, GeminiClient)
        self.assertEqual(client.api_key, 'test_key')


class TestAnalysisTypes(unittest.TestCase):
    """Test different analysis types."""
    
    @patch.dict(os.environ, {'GEMINI_API_KEY': 'test_key'})
    @patch('gemini_client.genai')
    def test_all_analysis_types(self, mock_genai):
        """Test all supported analysis types."""
        # Setup mock
        mock_model = MagicMock()
        mock_response = MagicMock()
        mock_response.text = "Analysis result"
        mock_model.generate_content.return_value = mock_response
        mock_genai.GenerativeModel.return_value = mock_model
        
        client = GeminiClient()
        
        # Test each analysis type
        analysis_types = ["general", "sentiment", "summary", "key_points"]
        for analysis_type in analysis_types:
            result = client.analyze_text("Test text", analysis_type=analysis_type)
            self.assertEqual(result, "Analysis result")


if __name__ == '__main__':
    unittest.main()
