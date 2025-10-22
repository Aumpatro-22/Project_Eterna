# Quick Start Guide - DOGSNIFF Phase 1

This guide will help you get started with DOGSNIFF Phase 1 in just a few minutes.

## Prerequisites

- Python 3.8 or higher installed
- A Google Gemini API key ([Get one free here](https://makersuite.google.com/app/apikey))

## Installation (5 minutes)

### Step 1: Clone the Repository

```bash
git clone https://github.com/Aumpatro-22/Project_Eterna.git
cd Project_Eterna
```

### Step 2: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 3: Set Up Your API Key

1. Copy the example environment file:
   ```bash
   cp .env.example .env
   ```

2. Edit `.env` and add your Gemini API key:
   ```
   GEMINI_API_KEY=your_actual_api_key_here
   ```

## Usage

### Run the Demo

```bash
python main.py
```

This will run three demonstrations:
1. Text generation about memory preservation
2. Sentiment analysis of Project_Eterna's mission
3. Key point extraction from the project description

### View Code Examples

```bash
python examples.py
```

This shows various usage patterns without needing an API key.

### Use in Your Own Code

Create a new Python file:

```python
from gemini_client import initialize_gemini

# Initialize the client
client = initialize_gemini()

# Generate text
response = client.generate_text("Your prompt here")
print(response)
```

## Common Use Cases

### 1. Analyze a Memory

```python
memory = "Today I visited grandma's house. The smell of fresh cookies..."
analysis = client.analyze_text(memory, analysis_type="sentiment")
print(analysis)
```

### 2. Summarize a Story

```python
long_story = "Once upon a time, in a small village..."
summary = client.analyze_text(long_story, analysis_type="summary")
print(summary)
```

### 3. Extract Key Themes

```python
text = "The family gathering was filled with laughter, stories, and love..."
themes = client.analyze_text(text, analysis_type="key_points")
print(themes)
```

### 4. Have a Conversation

```python
result = client.chat("How can I preserve memories?")
print(result["response"])

# Continue the conversation
result = client.chat(
    "What about digital formats?",
    conversation_history=result["history"]
)
print(result["response"])
```

## Troubleshooting

**Problem**: "Gemini API key not found"
**Solution**: Make sure you created `.env` file and added your API key

**Problem**: "No module named 'google'"
**Solution**: Run `pip install -r requirements.txt`

**Problem**: API rate limit errors
**Solution**: Wait a few moments between requests

## Next Steps

- Read the full documentation: [DOGSNIFF.md](DOGSNIFF.md)
- Explore example code: `python examples.py`
- Run tests: `python -m unittest test_gemini_client.py`
- Build your own memory preservation features!

## Support

For questions or issues:
- Check [DOGSNIFF.md](DOGSNIFF.md) for detailed documentation
- Review code comments in `gemini_client.py`
- See the [Gemini API documentation](https://ai.google.dev/docs)

---

**Ready to preserve memories? Let's get started!** 🚀
