import json
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from collections import Counter

nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

def custom_tokenize(text):
    tokens = word_tokenize(text.lower())
    stop_words = set(stopwords.words('english'))
    filtered_tokens = [token for token in tokens if token.isalnum() and token not in stop_words]
    lemmatizer = WordNetLemmatizer()
    lemmatized_tokens = [lemmatizer.lemmatize(token) for token in filtered_tokens]
    return lemmatized_tokens

def generate_tags(events):
    tags_dict = {}
    for event in events:
        title_tokens = custom_tokenize(event['title'])
        description_tokens = custom_tokenize(event['description'])
        all_tokens = title_tokens + description_tokens
        tag_count = Counter(all_tokens)
        sorted_tags = sorted(tag_count.items(), key=lambda x: x[1], reverse=True)
        tags_dict[event['title']] = [tag[0] for tag in sorted_tags[:3]]  # Extract top 3 tags
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
