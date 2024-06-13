// Import the OpenAI library
const OpenAI = require("openai");

// Initialize OpenAI with the API key
const openai = new OpenAI({ apiKey: '' });

// Load the events and users data from JSON files
const events = require('./example_events_with_tags.json');
const users = require('./example_users.json');

// Function to generate related tags using OpenAI
async function generateRelatedTags(searchQuery) {
    const systemPrompt = "You generate tags for search queries. Tags are related topics that will be used for keyword matching. You may only answer with tags separated by commas and spaces. There will be no extraneous characters like newlines or numbers. Some of your tags will be multiple words. But try to do only single word ones. These will not be separated by a space, since everything should be in camelCase. Try to generate 20 tags. And remember, these can be related topics. So if some search is 'book club', not only will a tag be 'reading', but another one might be 'harryPotter'";

    // console.log(`Generating related tags for search query: "${searchQuery}"`);

    const response = await openai.chat.completions.create({
        model: "gpt-4o",
        messages: [
            { role: "system", content: systemPrompt },
            { role: "user", content: searchQuery }
        ]
    });

    // console.log('Raw response from OpenAI:', response);

    const tags = response.choices[0].message.content.split(',').map(tag => tag.trim());

    // console.log('Generated tags:', tags);

    return tags;
}

// Function to search for relevant events
async function searchEvents(userId, searchQuery) {
    // console.log(`Searching events for user: ${userId} with query: "${searchQuery}"`);

    const user = users[userId];
    if (!user) {
        throw new Error('User not found');
    }

    // console.log('User details:', user);

    // Remove any commas from the search query terms and split into an array
    const cleanedSearchTerms = searchQuery.split(',').map(term => term.trim()).join(' ').split(' ');

    // Generate related tags
    const relatedTags = await generateRelatedTags(searchQuery);

    // Combine the original search query terms (cleaned) and the related tags
    const searchTerms = [...cleanedSearchTerms, ...relatedTags];

    // console.log('Search terms:', searchTerms);

    // Search through the events
    const relevantEventIds = Object.keys(events).filter(eventId => {
        const event = events[eventId];
        const contentToSearch = `${event.title} ${event.description} ${event.tags.join(' ')}`.toLowerCase();

        // Check if any of the search terms are in the event's content
        const matches = searchTerms.some(term => contentToSearch.includes(term.toLowerCase()));

        // console.log(`Event ID: ${eventId}, matches: ${matches}`);

        return matches;
    });

    // console.log('Relevant event IDs:', relevantEventIds);

    return relevantEventIds;
}

// // TESTING

// const userId = 'UhQU8MaBwJhwNvFNkHCGR7IKpDO2';
// const searchQuery = 'graduation';

// (async () => {
//     try {
//         // Fetch relevant event IDs
//         const eventIds = await searchEvents(userId, searchQuery);

//         // Log the fetched event IDs
//         console.log('Fetched event IDs:', eventIds);

//         // Function to print event details
//         function printEventDetails(eventId) {
//             const event = events[eventId];
//             if (event) {
//                 console.log(`\nTitle: ${event.title}`);
//                 console.log(`Description: ${event.description}`);
//             } else {
//                 console.error('Event not found');
//             }
//         }

//         // Print details for each relevant event
//         eventIds.forEach(printEventDetails);
//     } catch (error) {
//         console.error('Error:', error.message);
//     }
// })();

module.exports = { searchEvents };
