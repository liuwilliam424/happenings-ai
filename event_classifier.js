const OpenAI = require("openai");


const openai = new OpenAI({ apiKey: '' });


async function generateTags(events) {


const systemPrompt = "You are an event classifier. You generate tags for events. Tags are related topics that will be used for search queries. You may only answer with tags separated by commas and spaces. There will be no extraneous characters like newlines or numbers. Some of your tags will be multiple words. These will not be separated by a space, since everything should be in camelCase. Try to generate 20 tags. And remember, these can be related topics. So if some event is a book club, not only will a tag be 'Reading', but another one might be 'harryPotter'";


const tagsDict = {};


for (const eventId in events) {
const event = events[eventId];
const chatCompletion = await openai.chat.completions.create({
model: "gpt-4o",
messages: [
{ role: "system", content: systemPrompt },
{ role: "user", content: event.title + event.description }
]
});


tagsDict[event.title] = chatCompletion.choices[0].message.content;
}


return tagsDict;
}


//TESTING


// // Load events from JSON file
// const events = require('./example_events.json');
// const fs = require('fs');
// // Generate tags for each event
// generateTags(events).then(tagsDict => {
// // Write tags to another JSON file
// fs.writeFileSync('tags.json', JSON.stringify(tagsDict, null, 4));
// console.log("Tags saved to 'tags.json'");
// }).catch(err => {
// console.error("Error:", err);
// });
