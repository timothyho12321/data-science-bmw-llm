"""
LLM Provider Abstraction Layer
Supports both OpenAI and Google Gemini APIs
"""

import os
from dotenv import load_dotenv
from typing import Optional

# Load environment variables
load_dotenv()


class LLMProvider:
    """Unified interface for multiple LLM providers"""

    def __init__(self):
        """Initialize the appropriate LLM provider based on environment configuration"""
        self.provider = os.getenv("LLM_PROVIDER", "openai").lower()
        self.temperature = float(os.getenv("LLM_TEMPERATURE", "0.7"))

        if self.provider == "gemini":
            self._init_gemini()
        elif self.provider == "openai":
            self._init_openai()
        else:
            raise ValueError(
                f"Unsupported LLM_PROVIDER: {self.provider}. Use 'openai' or 'gemini'."
            )

    def _init_openai(self):
        """Initialize OpenAI client"""
        try:
            from openai import OpenAI
        except ImportError:
            raise ImportError("openai package not installed. Run: pip install openai")

        self.api_key = os.getenv("OPENAI_API_KEY")
        if not self.api_key:
            raise ValueError("OPENAI_API_KEY not found in environment variables.")

        self.client = OpenAI(api_key=self.api_key)
        self.model = os.getenv("OPENAI_MODEL", "gpt-4")

        print(f"✓ Using OpenAI: {self.model}")
        if "gpt-3.5" in self.model.lower():
            print("  → GPT-3.5-turbo (faster, cost-effective)")
        elif "gpt-4" in self.model.lower():
            print("  → GPT-4 (higher quality insights)")

    def _init_gemini(self):
        """Initialize Google Gemini client"""
        try:
            import google.generativeai as genai
        except ImportError:
            raise ImportError(
                "google-generativeai package not installed. Run: pip install google-generativeai"
            )

        self.api_key = os.getenv("GEMINI_API_KEY")
        if not self.api_key:
            raise ValueError("GEMINI_API_KEY not found in environment variables.")

        genai.configure(api_key=self.api_key)
        # Use correct model names - gemini 2.0+ models are available
        model_input = os.getenv("GEMINI_MODEL", "gemini-2.5-flash")

        # Map user-friendly names to actual model names
        model_mapping = {
            "gemini-1.5-flash": "gemini-2.5-flash",
            "gemini-1.5-pro": "gemini-2.5-pro",
            "gemini-flash": "gemini-2.5-flash",
            "gemini-pro": "gemini-2.5-pro",
            "gemini-2.5-flash": "gemini-2.5-flash",
            "gemini-2.5-pro": "gemini-2.5-pro",
            "gemini-2.0-flash": "gemini-2.0-flash",
        }

        self.model_name = model_mapping.get(model_input.lower(), "gemini-2.5-flash")

        # Create model with safety settings
        generation_config = {
            "temperature": self.temperature,
            "top_p": 0.95,
            "top_k": 40,
            "max_output_tokens": 8192,
        }

        self.client = genai.GenerativeModel(
            model_name=self.model_name, generation_config=generation_config
        )

        print(f"✓ Using Google Gemini: {self.model_name}")
        if "flash" in self.model_name.lower():
            print("  → Gemini Flash (fast, cost-effective)")
        elif "pro" in self.model_name.lower():
            print("  → Gemini Pro (best quality)")

    def generate_completion(
        self, prompt: str, system_prompt: Optional[str] = None
    ) -> str:
        """
        Generate completion using the configured LLM provider

        Parameters:
        -----------
        prompt : str
            User prompt/question
        system_prompt : str, optional
            System prompt for context (OpenAI only)

        Returns:
        --------
        str : Generated text response
        """
        if self.provider == "openai":
            return self._generate_openai(prompt, system_prompt)
        elif self.provider == "gemini":
            return self._generate_gemini(prompt, system_prompt)

    def _generate_openai(self, prompt: str, system_prompt: Optional[str] = None) -> str:
        """Generate completion using OpenAI API"""
        messages = []

        if system_prompt:
            messages.append({"role": "system", "content": system_prompt})

        messages.append({"role": "user", "content": prompt})

        response = self.client.chat.completions.create(
            model=self.model,
            messages=messages,
            temperature=self.temperature,
            max_tokens=2000,
        )

        return response.choices[0].message.content

    def _generate_gemini(self, prompt: str, system_prompt: Optional[str] = None) -> str:
        """Generate completion using Google Gemini API"""
        # Gemini doesn't have separate system prompts, so combine them
        full_prompt = prompt
        if system_prompt:
            full_prompt = f"{system_prompt}\n\n{prompt}"

        response = self.client.generate_content(full_prompt)

        return response.text

    def get_provider_info(self) -> dict:
        """Return information about the current provider configuration"""
        info = {"provider": self.provider, "temperature": self.temperature}

        if self.provider == "openai":
            info["model"] = self.model
        elif self.provider == "gemini":
            info["model"] = self.model_name

        return info
