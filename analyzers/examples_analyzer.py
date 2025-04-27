from .base_analyzer import BaseAnalyzer

class ExamplesAnalyzer(BaseAnalyzer):
    def get_analysis_prompt(self, prompt: str) -> str:
        return f"""
        Analyze the following prompt for its use of examples.
        Return a JSON object with the following structure:
        {{
            "verdict": "Pass/Weak/Missing",
            "explanation": "Detailed explanation of the examples analysis",
            "suggestion": "Specific suggestions for improvement"
        }}

        Consider these aspects:
        1. Are there example inputs provided?
        2. Are there example outputs provided?
        3. Do the examples cover different scenarios or edge cases?
        4. Are the examples clear and relevant to the task?

        Prompt to analyze:
        {prompt}

        Return only the JSON object, no additional text.
        """ 