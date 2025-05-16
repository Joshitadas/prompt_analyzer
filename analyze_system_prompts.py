import os
import re
from pathlib import Path
import json
from collections import defaultdict
import openai

def extract_system_prompt(content):
    # Common patterns for system prompt sections
    patterns = [
        r'## System Prompt\n\n(.*?)(?=\n\n|$)',  # Markdown style
        r'<claude_info>(.*?)</claude_info>',    # XML style
        r'You are.*?(?=\n\n|$)',                # Direct style
        r'## Prompt\n\n(.*?)(?=\n\n|$)',        # Alternative markdown style
        r'# System Prompt\n\n(.*?)(?=\n\n|$)',  # Another markdown style
    ]
    
    for pattern in patterns:
        try:
            match = re.search(pattern, content, re.DOTALL)
            if match:
                return match.group(1).strip()
        except Exception:
            continue
            
    # If no pattern matches, try to find the first section that starts with "You are"
    try:
        match = re.search(r'You are.*?(?=\n\n|$)', content, re.DOTALL)
        if match:
            return match.group(0).strip()
    except Exception:
        pass
        
    return None

def analyze_prompts(directory):
    prompt_patterns = defaultdict(int)
    common_phrases = defaultdict(int)
    role_definitions = []
    constraints = []
    capabilities = []
    
    # Walk through all markdown files
    for file_path in Path(directory).glob('*.md'):
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
                
            system_prompt = extract_system_prompt(content)
            if not system_prompt:
                print(f"Could not extract system prompt from {file_path}")
                continue
                
            # Extract role definitions
            role_matches = re.finditer(r'You are (.*?)(?=\.|\n)', system_prompt)
            for match in role_matches:
                role_definitions.append(match.group(1))
                
            # Extract constraints
            constraint_matches = re.finditer(r'(?:must|should|will|cannot|never|always) (.*?)(?=\.|\n)', system_prompt, re.IGNORECASE)
            for match in constraint_matches:
                constraints.append(match.group(1))
                
            # Extract capabilities
            capability_matches = re.finditer(r'(?:can|able to|capable of) (.*?)(?=\.|\n)', system_prompt, re.IGNORECASE)
            for match in capability_matches:
                capabilities.append(match.group(1))
                
            # Count common phrases
            words = re.findall(r'\b\w+\b', system_prompt.lower())
            for word in words:
                if len(word) > 3:  # Only count words longer than 3 characters
                    common_phrases[word] += 1
                    
        except Exception as e:
            print(f"Error processing {file_path}: {str(e)}")
            
    return {
        'role_definitions': list(set(role_definitions)),
        'constraints': list(set(constraints)),
        'capabilities': list(set(capabilities)),
        'common_phrases': dict(sorted(common_phrases.items(), key=lambda x: x[1], reverse=True)[:50])
    }

def generate_analysis_report(analysis_results):
    # Create a prompt for GPT-4 to analyze the results
    prompt = f"""
    Based on the analysis of multiple system prompts, here are the key findings:
    
    Role Definitions:
    {json.dumps(analysis_results['role_definitions'], indent=2)}
    
    Common Constraints:
    {json.dumps(analysis_results['constraints'], indent=2)}
    
    Capabilities:
    {json.dumps(analysis_results['capabilities'], indent=2)}
    
    Most Common Phrases:
    {json.dumps(analysis_results['common_phrases'], indent=2)}
    
    Please provide a detailed analysis of these findings and create a comprehensive guide on how to write effective system prompts. Include:
    1. Common patterns and best practices
    2. Key components that should be included
    3. Common pitfalls to avoid
    4. Examples of well-structured system prompts
    5. Tips for different use cases
    """
    
    # You would need to set up your OpenAI API key
    # response = openai.ChatCompletion.create(
    #     model="gpt-4",
    #     messages=[{"role": "user", "content": prompt}]
    # )
    # return response.choices[0].message.content
    
    # For now, we'll just save the analysis results
    with open('system_prompt_analysis.json', 'w', encoding='utf-8') as f:
        json.dump(analysis_results, f, indent=2)
    
    return "Analysis complete. Results saved to system_prompt_analysis.json"

if __name__ == "__main__":
    directory = "leaked-system-prompts"
    analysis_results = analyze_prompts(directory)
    report = generate_analysis_report(analysis_results)
    print(report) 