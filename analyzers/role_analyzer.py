from .base_analyzer import BaseAnalyzer

class RoleAnalyzer(BaseAnalyzer):
    def get_analysis_prompt(self, prompt: str) -> str:
        return f"""
        Analyze the following prompt for its role assignment to the LLM.
        Return a JSON object with the following structure:
        {{
            "verdict": "Pass/Weak/Missing",
            "explanation": "Detailed explanation of the role analysis",
            "suggestion": "Specific suggestions for improvement"
        }}

        Consider these aspects:
        1. Is a specific role or persona assigned to the LLM?
        2. Is the role clearly defined and appropriate for the task?
        3. Are there any role-specific instructions or expectations?
        4. Does the role help guide the LLM's behavior?

        Prompt to analyze:
        {prompt}

        Return only the JSON object, no additional text.
        """ 