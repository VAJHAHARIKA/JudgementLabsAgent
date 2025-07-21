from agent import context_qa

# Load context
with open("context.txt", "r") as f:
    context = f.read()

# Get question from user
question = input("Enter your question: ")

# Call agent
response = context_qa(context, question)

print("\nAnswer:", response)
