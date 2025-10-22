# DOGSNIFF - Phase 1: Gemini API Integration

## Overview

DOGSNIFF is part of the **Project_Eterna** ecosystem - a project born from a desire to preserve memories beyond loss. Phase 1 focuses on integrating Google's Gemini API for advanced language model capabilities that will help analyze, summarize, and work with memories, stories, and emotions.

## Features

- **Gemini API Integration**: Seamless integration with Google's Gemini Pro language model
- **Text Generation**: Generate meaningful content related to memories and remembrance
- **Text Analysis**: Analyze sentiment, extract key points, and summarize content
- **Conversational AI**: Interactive chat capabilities for memory exploration
- **Secure Configuration**: Environment-based API key management

## Project Structure

```
Project_Eterna/
├── README.md                 # Project overview
├── DOGSNIFF.md              # This file - Phase 1 documentation
├── requirements.txt         # Python dependencies
├── .env.example            # Example environment configuration
├── .gitignore              # Git ignore rules
├── gemini_client.py        # Gemini API client module
└── main.py                 # Main application entry point
```

## Setup Instructions

### Prerequisites

- Python 3.8 or higher
- Google Gemini API key ([Get one here](https://makersuite.google.com/app/apikey))

### Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Aumpatro-22/Project_Eterna.git
   cd Project_Eterna
   ```

2. **Create a virtual environment** (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure API key**:
   ```bash
   # Copy the example environment file
   cp .env.example .env
   
   # Edit .env and add your Gemini API key
   # GEMINI_API_KEY=your_actual_api_key_here
   ```

### Getting Your Gemini API Key

1. Visit [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Sign in with your Google account
3. Click "Create API Key"
4. Copy the generated key
5. Add it to your `.env` file

## Usage

### Running the Demo

To run the Phase 1 demonstration:

```bash
python main.py
```

This will demonstrate:
- Text generation capabilities
- Sentiment analysis
- Key point extraction

### Using the Gemini Client in Your Code

```python
from gemini_client import initialize_gemini

# Initialize the client
client = initialize_gemini()

# Generate text
response = client.generate_text("Your prompt here")
print(response)

# Analyze text
analysis = client.analyze_text("Your text here", analysis_type="sentiment")
print(analysis)

# Chat interface
chat_result = client.chat("Tell me about preserving memories")
print(chat_result["response"])
```

### Analysis Types

The `analyze_text` method supports different analysis types:
- `"general"`: General analysis and insights
- `"sentiment"`: Sentiment analysis
- `"summary"`: Text summarization
- `"key_points"`: Key point extraction

## API Reference

### GeminiClient Class

#### `__init__(api_key: Optional[str] = None)`
Initialize the Gemini client with an optional API key.

#### `generate_text(prompt: str, **kwargs) -> str`
Generate text based on a prompt.

**Parameters:**
- `prompt`: Input prompt for generation
- `**kwargs`: Additional generation parameters (temperature, max_tokens, etc.)

**Returns:** Generated text string

#### `analyze_text(text: str, analysis_type: str = "general") -> str`
Analyze text with specified analysis type.

**Parameters:**
- `text`: Text to analyze
- `analysis_type`: Type of analysis ("general", "sentiment", "summary", "key_points")

**Returns:** Analysis results as string

#### `chat(message: str, conversation_history: Optional[list] = None) -> Dict[str, Any]`
Have a conversational interaction.

**Parameters:**
- `message`: User's message
- `conversation_history`: Optional previous conversation history

**Returns:** Dictionary with "response" and "history" keys

## Security Best Practices

- **Never commit your `.env` file** - it contains your API key
- **Use `.env.example`** as a template without actual credentials
- **Keep your API key secret** - don't share it publicly
- **Rotate your API key** if you suspect it has been compromised

## Phase 1 Objectives ✓

- [x] Set up project structure
- [x] Implement Gemini API integration
- [x] Create configuration management
- [x] Develop text generation capabilities
- [x] Develop text analysis capabilities
- [x] Create example usage demonstration
- [x] Document setup and usage

## Future Phases

- **Phase 2**: Advanced memory storage and retrieval
- **Phase 3**: Multi-modal capabilities (images, audio)
- **Phase 4**: User interface development
- **Phase 5**: Integration with Project_Eterna ecosystem

## Troubleshooting

### "Gemini API key not found" Error

**Solution**: Ensure you've created a `.env` file and added your API key:
```
GEMINI_API_KEY=your_actual_key_here
```

### Import Errors

**Solution**: Make sure all dependencies are installed:
```bash
pip install -r requirements.txt
```

### API Rate Limits

**Solution**: The Gemini API has rate limits. If you encounter them:
- Wait a few moments before retrying
- Consider implementing rate limiting in your code
- Check your API quota in Google AI Studio

## Contributing

This project is part of the Project_Eterna initiative. Contributions that align with the mission of preserving memories and honoring loved ones are welcome.

## License

Part of Project_Eterna - A tribute to connection, healing, and the timeless power of remembrance.

## Support

For issues or questions about DOGSNIFF Phase 1:
- Check this documentation
- Review the code comments
- Consult the [Gemini API documentation](https://ai.google.dev/docs)

---

*"Preserving memories beyond loss, one story at a time."*
