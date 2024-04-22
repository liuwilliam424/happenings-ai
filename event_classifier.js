const OpenAI = require("openai");

const openai = new OpenAI({ apiKey: 'sk-' });
const fs = require('fs');

async function main() {
  const completion = await openai.chat.completions.create({
    messages: [{ role: "system", content: "You are a helpful assistant." }],
    model: "gpt-3.5-turbo",
  });

  console.log(completion.choices[0]);
}
const prompt = "Only generate 5 unique one-word labels with no other context like numbers or new line just separated by commas in pascalcase, based on following title & description: ";
const numEvents = 10;
const inputTokenRate = 0.50;  // $0.50 per 1 million tokens
const outputTokenRate = 1.50;  // $1.50 per 1 million tokens

async function generateTags(events) {
    const tagsDict = {};
    let count = 0;

    for (const event of events) {
        const inputTokenCount = prompt.length + event.title.length + event.description.length;
        const chatCompletion = await openai.chat.completions.create({
            model: "gpt-3.5-turbo",
            messages: [
                { role: "user", content: prompt + event.title + event.description }
            ]
        });

        tagsDict[event.title] = chatCompletion.choices[0].message.content;
        count++;
        const outputTokenCount = chatCompletion.choices[0].message.content.length;

        if (count === numEvents) {
            const totalCost = (inputTokenCount * inputTokenRate + outputTokenCount * outputTokenRate) / 10**6;
            console.log("Completed Message:", chatCompletion);
            console.log("Cost of Prompt: $", totalCost);
            return tagsDict;
        }
    }

    return tagsDict;
}

// Load events from JSON file
const events = require('./events.json');

// Generate tags for each event
generateTags(events).then(tagsDict => {
    // Write tags to another JSON file
    fs.writeFileSync('tags.json', JSON.stringify(tagsDict, null, 4));
    console.log(`${numEvents} tags saved to 'tags.json'`);
}).catch(err => {
    console.error("Error:", err);
});
main();