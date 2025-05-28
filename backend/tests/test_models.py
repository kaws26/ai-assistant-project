import pytest
from models import generate_responses
from unittest.mock import patch

def test_generate_responses():
    with patch('langchain_groq.ChatGroq') as mock_chat:
        # Mock the chat model's response
        mock_chat.return_value.invoke.return_value = "Test response"
        
        casual, formal = generate_responses("test query")
        
        assert isinstance(casual, str)
        assert isinstance(formal, str)
        assert len(casual) > 0
        assert len(formal) > 0

def test_prompt_templates():
    with patch('langchain_groq.ChatGroq') as mock_chat:
        mock_chat.return_value.invoke.return_value = "Test response"
        
        # Test with different query types
        queries = [
            "What is Python?",
            "Explain quantum computing",
            "Tell me about AI"
        ]
        
        for query in queries:
            casual, formal = generate_responses(query)
            assert isinstance(casual, str)
            assert isinstance(formal, str)
            assert len(casual) > 0
            assert len(formal) > 0 