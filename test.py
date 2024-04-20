import os
from openai import OpenAI


def break_up_query(user_query):
    prompt = f"Break up the following query into a comma sseparated string of discrete ideas. Ex: User input is 'baseball basketball coffee shop', we would like it to be split into 'baseball, basketball, coffee shop'. Another example is a single input 'baseball', we want to just return 'baseball'. The following query is {user_query}"
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
        model="gpt-3.5-turbo",
    )
    completed_message = chat_completion.choices[0].message.content
    return completed_message.split(", ")s



def tag_query(search_query):
    prompt = f"Based on the following query, generate a string of a dozen relevant tags in addition to the original query. Ex: Given 'baseball basketball coffee shop', generate 'baseball basketball coffee shop football tennis bakery bar restaurant'. The following query is {search_query}"
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
        model="gpt-3.5-turbo",
    )   
    completed_message = chat_completion.choices[0].message.content
    return completed_message

events = [
    {
        "title": "Los Angeles Convention Center - Ski Dazzle 2016",
        "description": "Paid parking available. Please park in South Hall parking garage.",
        "start_time": "2016-12-04T12:00:00.000",
        "location": "Los Angeles Convention Center, South Hall GH"
    },
    {
        "title": "Los Angeles Convention Center - Sikh Study Circle",
        "description": "Paid parking available. Park in West Hall parking garage. Prayer 7am-5pm. Food Function 11am-4pm. Expo 11am-4pm.  Donations accepted.",
        "start_time": "2016-12-04T07:00:00.000",
        "location": "Los Angeles Convention Center, West Hall A"
    },
    {
        "title": "Los Angeles Convention Center - Ski Dazzle 2016",
        "description": "Paid parking available. Please park in South Hall parking garage.",
        "start_time": "2016-12-03T11:00:00.000",
        "location": "Los Angeles Convention Center, South Hall GH"
    },
    {
        "title": "Los Angeles Convention Center: Yu-Gi-Oh Tournament",
        "description": "Paid parking available. Park in West Hall garage. Registration 7am-12pm. Tournament 10am-11pm",
        "start_time": "2016-12-03T07:00:00.000",
        "location": "Los Angeles Convention Center, Concourse Hall EF"
    },
    {
        "title": "Los Angeles Convention Center - Ski Dazzle 2016",
        "description": "Paid parking available. Please park in South Hall parking garage.",
        "start_time": "2016-12-02T15:00:00.000",
        "location": "Los Angeles Convention Center, South Hall GH"
    },
    {
        "title": "Los Angeles Convention Center - Stan Lee's Los Angeles Comic Con",
        "description": "Paid parking available. Park in South Hall garage. Registration opens at 8 a.m.",
        "start_time": "2016-10-30T10:00:00.000",
        "location": "Los Angeles Convention Center, South Hall GHJK"
    },
    {
        "title": "Los Angeles Convention Center - Stan Lee's Los Angeles Comic Con",
        "description": "Paid parking available. Park in South Hall garage.  Registration opens at 7a.m.",
        "start_time": "2016-10-29T09:00:00.000",
        "location": "Los Angeles Convention Center, South Hall GHJK"
    },
    {
        "title": "Los Angeles Convention Center - Stan Lee's Los Angeles Comic Con",
        "description": "Paid parking available. Park in South Hall garage. Registration opens at 9 a.m.",
        "start_time": "2016-10-28T17:00:00.000",
        "location": "Los Angeles Convention Center, South Hall GHJK"
    },
    {
        "title": "Los Angeles Convention Center - Idealist Graduate School Fair",
        "description": "Paid parking available. Please park in South Hall parking garage.",
        "start_time": "2016-10-17T17:00:00.000",
        "location": "Los Angeles Convention Center, South Hall K"
    },
    {
        "title": "Summer Whalewatch (08/21/2016)",
        "description": "Join CMA staff as they search the Catalina Channel for the largest animals in the world. Blue, fin and humpback whales spend part of their summer here to feed on huge amounts of krill. Boat leaves from San Pedro.  Pre-registration is required",
        "start_time": "2016-08-21T09:00:00.000",
        "location": "Cabrillo Marine Aquarium"
    },
    {
        "title": "See the Sea, si? Floating Oceanography Lab (08/20/2016)",
        "description": "Join us aboard a specially equipped vessel where you’ll have opportunities to study some of the near- shore animals which will be collected during the trip. Learn about plankton, animals that call mud their home and bottom fish and marine birds and be on the lookout for sea lions and dolphins. Pre-registration is required.",
        "start_time": "2016-08-20T09:00:00.000",
        "location": "Cabrillo Marine Aquarium"
    },
    {
        "title": "Meet The Grunion (07/21/2016)",
        "description": "Watch the silvery fish come up on the beach to spawn!  Learn about the interesting mating rituals and growth of this curious fish.  The Aquarium opens at 8pm and an auditorium program begins at 9, followed by guided observation at the beach.  Warm clothing and a flashlight are recommended.",
        "start_time": "2016-07-21T20:00:00.000",
        "location": "Cabrillo Marine Aquarium"
    },
    {
        "title": "36th Annual Lotus Festival (07/10/2016)",
        "description": "The Lotus Festival celebrates the people and cultures of Asia and the Pacific Islands. As we experience the diversity of cultures, this year we highlight the traditions and customs of our host country, Republic of Korea.    Explore the Festival, taste the cuisine, enjoy the traditional live entertainment and the excitement of the legendary dragon boat races. Over the years, the Lotus Festival has become a local tradition, with community booths, food court, boutiques and children’s play areas.",
        "start_time": "2016-07-10T12:00:00.000",
        "location": "Echo Park Lake"
    },
    {
        "title": "36th Annual Lotus Festival (07/09/2016)",
        "description": "The Lotus Festival celebrates the people and cultures of Asia and the Pacific Islands. As we experience the diversity of cultures, this year we highlight the traditions and customs of our host country, Republic of Korea.    Explore the Festival, taste the cuisine, enjoy the traditional live entertainment and the excitement of the legendary dragon boat races. Over the years, the Lotus Festival has become a local tradition, with community booths, food court, boutiques and children’s play areas.",
        "start_time": "2016-07-09T12:00:00.000",
        "location": "Echo Park Lake"
    },
    {
        "title": "Re-Opening Ceremony for Westwood Gardens Park (06/25/2016)",
        "description": "Join us for the Re-Opening Ceremony for Westwood Gardens Park!    Saturday, June 25, 2016  10:00 A.M.    Westwood Gardens Park  1246 Glendon Avenue  Los Angeles, CA 90024    This event is being hosted by the Department of Recreation and Parks along with Councilmember Paul Koretz, Fifth District.",
        "start_time": "2016-06-25T10:00:00.000",
        "location": "Westwood Gardens Park"
    },
    {
        "title": "\"Discover Recycling\" Open Houses",
        "description": "LA Sanitation opens its wasteshed district yards to the public in a series of free Saturday events. The Open Houses showcase LA Sanitation’s residential curbside collection programs with an emphasis on proper recycling practices and bulky item collection. The Open Houses feature trash trucks and equipment demonstrations in addition to facility tours, information booths, recycling games, and refreshments.",
        "start_time": "2016-06-25T09:00:00.000",
        "location": "West Los Angeles District Yard"
    }
]

def search_events(search_query):
    search_results = []
    for event in events:
        if any(search_query.lower() in str(event[field]).lower() for field in ["title", "description"]):
            search_results.append(event)
    return search_results

def main():
    while True:
        search_term = input("Enter search term (or 'exit' to quit): ")

        if search_term.lower() == 'exit':
            break

        string_with_tags = tag_query(search_term)
        split_up_tags = break_up_query(string_with_tags)
        print(split_up_tags)

        list_of_events = []
        for tag in split_up_tags:
            list_of_events.append(search_events(tag))

        matching_events = list_of_events
        

        if matching_events:
            for matching_event in matching_events:
                for event in matching_event:
                    print(f"\nTitle: {event['title']}")
                    print(f"Description: {event['description']}")
                    print(f"Start Time: {event['start_time']}")
                    print(f"Location: {event['location']}\n")
            else:
                print("No events found matching your search criteria.\n")

# Run the search interface
if __name__ == "__main__":
    main()