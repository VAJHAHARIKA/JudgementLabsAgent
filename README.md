project:
  title: Context-Aware Q&A Agent
  submission_for: Judgment Labs AI Engineer Assessment
  author:
    name: Harika Vajha
    github: https://github.com/vajhaharika
    portfolio: https://vajhaharika.github.io/harika7
  description: >
    A lightweight agent that answers user questions based solely on a provided context using OpenAI,
    and evaluates the output using the `judgeval` SDK with FaithfulnessScorer.
  features:
    - Context-aware Q&A using OpenAI's GPT-3.5/4o
    - Judgeval SDK evaluation with FaithfulnessScorer
    - Structured and extensible pipeline
  folder_structure:
    - agent.py: "Core context-aware Q&A logic"
    - run.py: "Command-line interface for agent interaction"
    - context.txt: "Sample knowledge base"
    - evaluate.py: "Judgeval evaluation script using FaithfulnessScorer"
    - requirements.txt: "Python dependencies"
    - .env.example: "Environment variable template"
    - README.md: "Project documentation"
  setup:
    instructions:
      - step: Clone the repository
        command: git clone https://github.com/YOUR_USERNAME/judgment-agent-harika.git
      - step: Navigate to the project folder
        command: cd judgment-agent-harika
      - step: Install dependencies
        command: pip install -r requirements.txt
      - step: Set environment variables
        command: |
          export OPENAI_API_KEY=your-openai-key
          export JUDGVAL_API_KEY=your-judgeval-key
          export JUDGVAL_ORG_ID=your-org-id
  run_agent:
    command: python run.py
    description: "Interactively asks a question and returns an answer based on the provided context."
  run_evaluation:
    command: python evaluate.py
    description: "Runs FaithfulnessScorer evaluation on a predefined input-output example."
  judgeval_notes: >
    Encountered undocumented import issues with trace() and record_eval().
    GitHub issue raised to clarify usage paths. Otherwise, JudgmentClient with FaithfulnessScorer works as expected.
  improvements:
    - Add HelpfulnessScorer and ConcisenessScorer
    - Batch evaluation support
    - Add back trace() once officially supported
  submission_checklist:
    - Agent code functional
    - judgeval evaluation included
    - Secure API handling
    - GitHub issue submitted for SDK gaps
    - Documentation complete
