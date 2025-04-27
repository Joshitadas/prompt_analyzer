from .base_analyzer import BaseAnalyzer

class ContextAnalyzer(BaseAnalyzer):
    def get_analysis_prompt(self, prompt: str) -> str:
        return f"""
        Analyze the following prompt for its context and background information.
        Return a JSON object with the following structure:
        {{
            "verdict": "Pass/Weak/Missing",
            "explanation": "Detailed explanation of the context analysis",
            "suggestion": "Specific suggestions for improvement"
        }}

        Consider these aspects:
        1. Is there sufficient background information?
        2. Is the context clear and well-defined?
        3. Are the goals and objectives clearly stated?
        4. Is the setting or environment properly explained?

        Prompt to analyze:
        {prompt}

        Return only the JSON object, no additional text.
        """ 