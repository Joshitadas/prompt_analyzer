import os
from dotenv import load_dotenv
from analyzers import (
    ContextAnalyzer,
    MachineTreatmentAnalyzer,
    ConstraintsAnalyzer,
    FormatAnalyzer,
    ExamplesAnalyzer,
    RoleAnalyzer,
    BestPracticesAnalyzer
)

def analyze_prompt(prompt: str) -> str:
    # Initialize analyzers
    analyzers = [
        ContextAnalyzer(),
        MachineTreatmentAnalyzer(),
        ConstraintsAnalyzer(),
        FormatAnalyzer(),
        ExamplesAnalyzer(),
        RoleAnalyzer(),
        BestPracticesAnalyzer()
    ]
    
    # Get analysis from each analyzer
    results = []
    for analyzer in analyzers:
        result = analyzer.analyze(prompt)
        results.append({
            'principle': analyzer.__class__.__name__.replace('Analyzer', ''),
            'verdict': result['verdict'],
            'explanation': result['explanation'],
            'suggestion': result['suggestion']
        })
    
    # Format results
    output = "Prompt Analysis Results\n"
    output += "=====================\n\n"
    output += f"Prompt: {prompt}\n\n"
    
    for result in results:
        output += f"Principle: {result['principle']}\n"
        output += f"Verdict: {result['verdict']}\n"
        output += f"Explanation: {result['explanation']}\n"
        output += f"Suggestion: {result['suggestion']}\n"
        output += "-" * 50 + "\n\n"
    
    return output

def main():
    # Load environment variables
    load_dotenv()
    
    # Check for API key
    if not os.getenv("OPENAI_API_KEY"):
        print("Error: OPENAI_API_KEY not found in environment variables.")
        print("Please create a .env file with your OpenAI API key.")
        return
    
    # Get prompt from user
    print("Enter your prompt (press Enter twice to finish):")
    lines = []
    while True:
        line = input()
        if not line:
            break
        lines.append(line)
    prompt = "\n".join(lines)
    
    if not prompt:
        print("Error: No prompt provided.")
        return
    
    # Analyze prompt
    print("\nAnalyzing prompt...")
    results = analyze_prompt(prompt)
    
    # Save results to file
    output_file = "prompt_analysis.txt"
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(results)
    
    print(f"\nAnalysis complete! Results saved to {output_file}")

if __name__ == "__main__":
    main() 