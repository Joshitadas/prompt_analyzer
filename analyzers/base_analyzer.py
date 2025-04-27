import os
import json
from abc import ABC, abstractmethod
import openai
from typing import Dict

class BaseAnalyzer(ABC):
    def __init__(self):
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            raise ValueError("OPENAI_API_KEY not found in environment variables")
        openai.api_key = api_key
    
    @abstractmethod
    def get_analysis_prompt(self, prompt: str) -> str:
        """Generate the prompt for LLM analysis."""
        pass
    
    def analyze(self, prompt: str) -> Dict:
        """Analyze the prompt using LLM."""
        try:
            analysis_prompt = self.get_analysis_prompt(prompt)
            
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a prompt analysis expert. Analyze the given prompt and return a JSON object with verdict, explanation, and suggestion."},
                    {"role": "user", "content": analysis_prompt}
                ],
                temperature=0.7
            )
            
            result = json.loads(response.choices[0].message['content'])
            return {
                "verdict": result["verdict"],
                "explanation": result["explanation"],
                "suggestion": result["suggestion"]
            }
            
        except Exception as e:
            return {
                "verdict": "Error",
                "explanation": f"Error during analysis: {str(e)}",
                "suggestion": "Please try again or check your API key."
            }
    
    def _get_verdict(self, score: float) -> str:
        """Convert a score to a verdict."""
        if score >= 0.7:
            return "Pass"
        elif score >= 0.4:
            return "Weak"
        else:
            return "Missing" 