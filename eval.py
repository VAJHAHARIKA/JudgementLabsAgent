import os
from judgeval import JudgmentClient
from judgeval.data import Example
from judgeval.scorers import FaithfulnessScorer

# Load Judgeval credentials
client = JudgmentClient(
    api_key=os.getenv("JUDGVAL_API_KEY"),
    org_id=os.getenv("JUDGVAL_ORG_ID")
)

# Define an example for evaluation
example = Example(
    input="What if these shoes don't fit?",
    actual_output="We offer a 30-day full refund at no extra cost.",
    retrieval_context=[
        "All customers are eligible for a 30-day full refund at no extra cost."
    ]
)

scorer = FaithfulnessScorer(threshold=0.5)

# Run evaluation
results = client.run_evaluation(
    examples=[example],
    scorers=[scorer],
    model="gpt-4o",
    project_name="judgeval-faithfulness-demo"
)

print("Evaluation Results:")
print(results)
