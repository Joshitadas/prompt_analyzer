from .base_analyzer import BaseAnalyzer

class FormatAnalyzer(BaseAnalyzer):
    def get_analysis_prompt(self, prompt: str) -> str:
        return f"""
        Analyze the following prompt for its input/output format specifications.
        Return a JSON object with the following structure:
        {{
            "verdict": "Pass/Weak/Missing",
            "explanation": "Detailed explanation of the format analysis",
            "suggestion": "Specific suggestions for improvement"
        }}

        Consider these aspects:
        1. Is the expected input format clearly specified?
        2. Is the expected output format clearly specified?
        3. Are there any formatting requirements (JSON, XML, markdown, etc.)?
        4. Are there any structural requirements (sections, headings, lists)?

        Prompt to analyze:
        {prompt}

        Return only the JSON object, no additional text.
        """ 