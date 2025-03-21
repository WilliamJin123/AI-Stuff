import OpenAI from "openai";



const apiKey = process.env.OPENAI_API_KEY;


const client = new OpenAI();

const completion = await client.chat.completions.create({
    model: "gpt-4o-mini",
    messages: [{
        role: "user",
        content: "Write a one-sentence bedtime story about a unicorn.",
    }],
});

console.log(completion.choices[0].message.content);
