import os
from openai import OpenAI

# Define token rates
input_token_rate = 0.50  # $0.50 per 1 million tokens
output_token_rate = 1.50  # $1.50 per 1 million tokens

client = OpenAI(api_key=)

prompt = "Tell me how to make an AI event classifier, answer in 40 words maximum."

# Calculate input token count (assuming each word is a token)
input_token_count = len(prompt.split())

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": prompt,
        }
    ],
    model="gpt-3.5-turbo",
)

# Extract completed message
completed_message = chat_completion.choices[0].message.content

# Calculate output token count
output_token_count = len(completed_message.split())

# Calculate total cost
total_cost = (input_token_count * input_token_rate + output_token_count * output_token_rate) / 10**6

print("Completed Message:", completed_message)
print("Cost of Prompt: $", total_cost)
