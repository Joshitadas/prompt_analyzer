from .base_analyzer import BaseAnalyzer

class ConstraintsAnalyzer(BaseAnalyzer):
    def get_analysis_prompt(self, prompt: str) -> str:
        return f"""
        Analyze the following prompt for its constraints and boundaries.
        Return a JSON object with the following structure:
        {{
            "verdict": "Pass/Weak/Missing",
            "explanation": "Detailed explanation of the constraints analysis",
            "suggestion": "Specific suggestions for improvement"
        }}

        Consider these aspects:
        1. Are there clear boundaries or limitations specified?
        2. Are there specific requirements or restrictions?
        3. Are there any numerical constraints (word count, character limit, etc.)?
        4. Are there any content restrictions or guidelines?

        Prompt to analyze:
        {prompt}

        Return only the JSON object, no additional text.
        """ 