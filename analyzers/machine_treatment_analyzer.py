from .base_analyzer import BaseAnalyzer

class MachineTreatmentAnalyzer(BaseAnalyzer):
    def get_analysis_prompt(self, prompt: str) -> str:
        return f"""
        Analyze the following prompt for how it treats the LLM.
        Return a JSON object with the following structure:
        {{
            "verdict": "Pass/Weak/Missing",
            "explanation": "Detailed explanation of the machine treatment analysis",
            "suggestion": "Specific suggestions for improvement"
        }}

        Consider these aspects:
        1. Does the prompt treat the LLM appropriately as a machine?
        2. Is there any human-like flattery or emotional language?
        3. Are the instructions clear and direct?
        4. Is there any vague or ambiguous language?

        Prompt to analyze:
        {prompt}

        Return only the JSON object, no additional text.
        """ 