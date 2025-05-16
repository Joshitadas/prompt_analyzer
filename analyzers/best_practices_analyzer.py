import json
import os
from .base_analyzer import BaseAnalyzer

class BestPracticesAnalyzer(BaseAnalyzer):
    def __init__(self):
        super().__init__()
        # Load best practices from system_prompt_analysis.json
        with open(os.path.join(os.path.dirname(__file__), '..', 'system_prompt_analysis.json'), 'r', encoding='utf-8') as f:
            self.best_practices = json.load(f)

    def get_analysis_prompt(self, prompt: str) -> str:
        return f'''
        Analyze the following prompt for the presence of best practices and patterns found in system prompts. 
        Use the following as a checklist:
        - Role definition: {self.best_practices['role_definitions'][:3]} ...
        - Constraints: {self.best_practices['constraints'][:3]} ...
        - Capabilities: {self.best_practices['capabilities'][:3]} ...
        - Output formatting and interaction style (e.g., markdown, language, conciseness, etc.)
        - Common pitfalls: missing role, missing constraints, unclear output format, etc.

        Return a JSON object with:
        {{
            "verdict": "Pass/Weak/Missing",
            "explanation": "Detailed explanation of which best practices are present or missing.",
            "suggestion": "Specific suggestions for improvement."
        }}

        Prompt to analyze:
        {prompt}

        Return only the JSON object, no additional text.
        ''' 