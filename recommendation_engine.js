// Import the searchEvents function from search.js
const { searchEvents } = require('./search.js');

// Load the events and users data from JSON files
const events = require('./example_events_with_tags.json');
const users = require('./example_users.json');

// Function to recommend events based on user's interests and previously attended events
async function recommendEvents(userId) {
    // Log the user ID we're working with
    // console.log(`Fetching recommendations for user: ${userId}`);

    // Find the user object by userId
    const user = users[userId];
    if (!user) {
        throw new Error('User not found');
    }

    // Log the found user details
    // console.log('User details:', user);

    // Get user's interests
    const userInterests = user.likes;
    // console.log('User interests:', userInterests);

    // Get the user's last attended events (up to 5)
    const attendedEventIds = user.events.slice(-5);
    // console.log('Last attended event IDs:', attendedEventIds);

    // Get the tags from the last attended events
    const attendedEventTags = attendedEventIds.map(eventId => {
        const event = events[eventId];
        if (event) {
            // console.log(`Tags for event ${eventId}:`, event.tags);
            return event.tags;
        } else {
            // console.warn(`Event not found for ID: ${eventId}`);
            return [];
        }
    }).flat();

    // Log the collected tags from attended events
    // console.log('Collected tags from attended events:', attendedEventTags);

    // Combine user interests and attended event tags, removing duplicates
    const combinedTags = [...new Set([...userInterests, ...attendedEventTags])];
    // console.log('Combined tags:', combinedTags);

    // Join the tags to form a search query
    const searchQuery = combinedTags.join(', ');
    // console.log('Search query:', searchQuery);

    // Use the search function to find relevant events
    const recommendedEventIds = await searchEvents(userId, searchQuery);
    // console.log('Recommended Event IDs:', recommendedEventIds);

    return recommendedEventIds;
}

// TESTING

// const userId = 'UhQU8MaBwJhwNvFNkHCGR7IKpDO2';

// (async () => {
//     try {
//         // Fetch recommended event IDs
//         const recommendedEventIds = await recommendEvents(userId);

//         console.log('Recommended Event IDs:', recommendedEventIds);

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

//         // Print details for each recommended event
//         recommendedEventIds.forEach(printEventDetails);
//     } catch (error) {
//         console.error('Error:', error.message);
//     }
// })();
