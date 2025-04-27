# Prompt Analyzer

A command-line tool that analyzes prompts based on six key principles of effective prompt engineering, using OpenAI's GPT model for analysis.

## What Does This Project Do?

The Prompt Analyzer evaluates prompts based on six fundamental principles:

1. **Context Analysis**: Evaluates the clarity and completeness of background information, goals, and setting.
2. **Machine Treatment**: Assesses how appropriately the prompt treats the LLM as a machine.
3. **Constraints**: Analyzes the presence and clarity of boundaries, limitations, and requirements.
4. **Format**: Evaluates the specification of input/output formats and structural requirements.
5. **Examples**: Checks for the presence and quality of example inputs and outputs.
6. **Role**: Assesses the clarity and appropriateness of role assignment to the LLM.

For each principle, the analyzer provides:
- A verdict (Pass/Weak/Missing)
- A detailed explanation
- Specific suggestions for improvement

## How To Run The Project

### Prerequisites
- Python 3.x
- OpenAI API key

### Setup Instructions

1. Clone the repository:
   ```bash
   git clone https://github.com/Joshitadas/prompt_analyzer.git
   cd prompt-analyzer
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   .\venv\Scripts\activate  # On Windows
   source venv/bin/activate # On Unix/MacOS
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Create a `.env` file in the root directory and add your OpenAI API key:
   ```
   OPENAI_API_KEY=your_api_key_here
   ```

### Running the Analyzer

1. Run the analyzer:
   ```bash
   python prompt_analyzer.py
   ```

2. Enter your prompt when prompted. Press Enter twice to finish input.

3. The analysis results will be saved in `prompt_analysis.txt`.

## Project Explanation

### Architecture

The project follows a modular architecture with the following components:

1. **Main Script** (`prompt_analyzer.py`):
   - Handles user input
   - Coordinates analysis
   - Manages output generation

2. **Analyzer Modules**:
   - `base_analyzer.py`: Abstract base class providing LLM integration
   - Individual analyzers for each principle:
     - `context_analyzer.py`
     - `machine_treatment_analyzer.py`
     - `constraints_analyzer.py`
     - `format_analyzer.py`
     - `examples_analyzer.py`
     - `role_analyzer.py`

### Analysis Process

1. **Input Collection**:
   - Takes multi-line input from the user
   - Supports complex prompts with formatting

2. **Analysis**:
   - Each analyzer uses GPT-3.5-turbo to evaluate its specific aspect
   - Provides structured JSON responses
   - Includes specific criteria for each principle

3. **Output Generation**:
   - Creates a formatted analysis report
   - Saves results to a text file
   - Includes the original prompt and detailed analysis

### Example Output

```
Prompt Analysis Results
=====================

Prompt: [Your prompt here]

Principle: Context
Verdict: [Pass/Weak/Missing]
Explanation: [Detailed analysis]
Suggestion: [Improvement suggestions]
--------------------------------------------------
[Continues for each principle...]
```

### Use Cases

1. **Prompt Development**:
   - Evaluate and improve prompts during development
   - Identify missing elements
   - Get specific improvement suggestions

2. **Learning Tool**:
   - Understand prompt engineering principles
   - Learn from concrete suggestions
   - Practice writing better prompts

3. **Quality Assurance**:
   - Verify prompts meet best practices
   - Ensure completeness and clarity
   - Maintain consistency in prompt design

