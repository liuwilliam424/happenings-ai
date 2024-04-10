import os
from openai import OpenAI

client = OpenAI(api_key="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")

# hard-coded data for testing
user_interests = ["engineering", "technology", "NCAA basketball", "networking", "environmental sustainability", "entrepreneurship"]
prev_events = {
    "events": [
        {"title": "Engineering Innovations in Sports", "description": "Exploring the intersection of engineering and sports."},
        {"title": "NCAA Basketball Fan Meetup", "description": "A social gathering for NCAA basketball fans to connect and discuss the game."},
        {"title": "Tech Startups Networking Event", "description": "An opportunity to meet and network with tech entrepreneurs and innovators."},
        {"title": "Sustainable Engineering Solutions", "description": "A seminar on the role of engineering in promoting environmental sustainability."},
        {"title": "Basketball Analytics Workshop", "description": "A hands-on workshop on applying data analytics in basketball."},
        {"title": "Entrepreneurship in the Tech Industry", "description": "A panel discussion on starting and growing a tech business."},
        {"title": "Engineering for Social Impact", "description": "A lecture on using engineering skills to address social issues."},
        {"title": "Sports and Technology Expo", "description": "An exhibition showcasing the latest technological advancements in sports."},
        {"title": "Green Technology Innovations", "description": "An event highlighting new technologies in environmental sustainability."},
        {"title": "Networking Skills for Engineers", "description": "A workshop on developing networking skills for career growth in engineering."},
        {"title": "Apples and oranges", "description": "i hate bananas"},
    ]
}

def search_events(tags):
    result_events = []
    return result_events


# returns list of event titles based on user interests and previous events
def recommend_engine(user_interests, prev_events):
    event_data = prev_events['events'][:10]

    event_titles = [event['title'].strip() for event in event_data]
    event_descs = [event['description'].strip() for event in event_data]

    event_titles_str = ', '.join(event_titles)
    event_descs_str = ', '.join(event_descs)
    user_interests_str = ', '.join(user_interests)

    prompt = f"Based on all of these words: {event_titles_str}, {event_descs_str}, and {user_interests_str}, give me a list of 20 relevant tags separated by commas"

    response = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
        model="gpt-3.5-turbo"
    )
    

    result = response.choices[0].message.content.split(', ')

    return result

recommend_engine(user_interests, prev_events)