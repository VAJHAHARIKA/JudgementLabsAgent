import os
import openai

# Load OpenAI API key from environment
openai.api_key = os.getenv("OPENAI_API_KEY")

def context_qa(context, question):
    prompt = f"""You are an assistant. Answer the question only if the answer is in the context. Otherwise, say you don't know.

Context: {context}

Question: {question}
Answer:"""

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )

    answer = response['choices'][0]['message']['content'].strip()
    return answer
