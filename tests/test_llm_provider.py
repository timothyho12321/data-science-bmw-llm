"""
Unit tests for llm_provider module
"""

import unittest
from unittest.mock import Mock, patch, MagicMock
import sys
import os

# Add parent directory to path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


class TestLLMProvider(unittest.TestCase):
    """Test cases for LLMProvider class"""

    @patch.dict(
        os.environ,
        {
            "LLM_PROVIDER": "openai",
            "OPENAI_API_KEY": "test-key",
            "OPENAI_MODEL": "gpt-4",
        },
    )
    @patch("llm_provider.OpenAI")
    def test_openai_initialization(self, mock_openai):
        """Test OpenAI provider initialization"""
        from llm_provider import LLMProvider

        provider = LLMProvider()

        self.assertEqual(provider.provider, "openai")
        self.assertEqual(provider.model, "gpt-4")
        mock_openai.assert_called_once()

    @patch.dict(
        os.environ,
        {
            "LLM_PROVIDER": "gemini",
            "GEMINI_API_KEY": "test-key",
            "GEMINI_MODEL": "gemini-2.5-flash",
        },
    )
    @patch("llm_provider.genai")
    def test_gemini_initialization(self, mock_genai):
        """Test Gemini provider initialization"""
        from llm_provider import LLMProvider

        # Mock the GenerativeModel
        mock_genai.GenerativeModel = MagicMock()

        provider = LLMProvider()

        self.assertEqual(provider.provider, "gemini")
        self.assertEqual(provider.model_name, "gemini-2.5-flash")
        mock_genai.configure.assert_called_once()

    @patch.dict(os.environ, {"LLM_PROVIDER": "invalid"})
    def test_invalid_provider(self):
        """Test handling of invalid provider"""
        from llm_provider import LLMProvider

        with self.assertRaises(ValueError) as context:
            LLMProvider()

        self.assertIn("Unsupported LLM_PROVIDER", str(context.exception))

    @patch.dict(os.environ, {"LLM_PROVIDER": "openai"})
    def test_missing_api_key(self):
        """Test handling of missing API key"""
        from llm_provider import LLMProvider

        with self.assertRaises(ValueError) as context:
            LLMProvider()

        self.assertIn("API_KEY not found", str(context.exception))

    @patch.dict(
        os.environ,
        {
            "LLM_PROVIDER": "openai",
            "OPENAI_API_KEY": "test-key",
            "OPENAI_MODEL": "gpt-4",
            "LLM_TEMPERATURE": "0.5",
        },
    )
    @patch("llm_provider.OpenAI")
    def test_custom_temperature(self, mock_openai):
        """Test custom temperature setting"""
        from llm_provider import LLMProvider

        provider = LLMProvider()

        self.assertEqual(provider.temperature, 0.5)

    @patch.dict(
        os.environ,
        {
            "LLM_PROVIDER": "gemini",
            "GEMINI_API_KEY": "test-key",
            "GEMINI_MODEL": "gemini-1.5-flash",
        },
    )
    @patch("llm_provider.genai")
    def test_model_name_mapping(self, mock_genai):
        """Test model name mapping (1.5 to 2.5)"""
        from llm_provider import LLMProvider

        # Mock the GenerativeModel
        mock_genai.GenerativeModel = MagicMock()

        provider = LLMProvider()

        # Should map gemini-1.5-flash to gemini-2.5-flash
        self.assertEqual(provider.model_name, "gemini-2.5-flash")

    @patch.dict(
        os.environ,
        {
            "LLM_PROVIDER": "openai",
            "OPENAI_API_KEY": "test-key",
            "OPENAI_MODEL": "gpt-4",
        },
    )
    @patch("llm_provider.OpenAI")
    def test_get_provider_info(self, mock_openai):
        """Test provider info retrieval"""
        from llm_provider import LLMProvider

        provider = LLMProvider()
        info = provider.get_provider_info()

        self.assertEqual(info["provider"], "openai")
        self.assertEqual(info["model"], "gpt-4")
        self.assertIn("temperature", info)


if __name__ == "__main__":
    unittest.main()
