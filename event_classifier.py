import json
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from openai import OpenAI
from collections import Counter

nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

client = OpenAI(api_key='sk-')
input_token_rate = 0.50  # $0.50 per 1 million tokens
output_token_rate = 1.50  # $1.50 per 1 million tokens

prompt = "Only generate 5 unique one-word labels with no other context like numbers or new line just separated by commas in pascalcase, based on following title & description: "

def custom_tokenize(text):
    tokens = word_tokenize(text.lower())
    stop_words = set(stopwords.words('english'))
    filtered_tokens = [token for token in tokens if token.isalnum() and token not in stop_words]
    lemmatizer = WordNetLemmatizer()
    lemmatized_tokens = [lemmatizer.lemmatize(token) for token in filtered_tokens]
    return lemmatized_tokens

def generate_tags(events):
    tags_dict = {}
    count = 0
    for event in events:
        input_token_count = len(prompt + event['title'] + event['description'])
        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": prompt + event['title'] + event['description'],
                }
            ],
            model="gpt-3.5-turbo",
        ) 

        tags_dict[event['title']] = chat_completion.choices[0].message.content 
        count += 1
        output_token_count = len(chat_completion.choices[0].message.content)
        
        if(count == 100):
            total_cost = (input_token_count * input_token_rate + output_token_count * output_token_rate) / 10**6
            print("Completed Message:", chat_completion)
            print("Cost of Prompt: $", total_cost)
            return tags_dict
    return tags_dict

# Load events from JSON file
with open('events.json', 'r', encoding='utf-8') as f:
    events = json.load(f)

# Generate tags for each event
tags_dict = generate_tags(events)

# Write tags to another JSON file
with open('tags.json', 'w', encoding='utf-8') as f:
    json.dump(tags_dict, f, indent=4)

print("Tags saved to 'tags.json'")
