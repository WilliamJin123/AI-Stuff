import dotenv from "dotenv"
import { GoogleGenerativeAI } from "@google/generative-ai"



dotenv.config()
const genAI = new GoogleGenerativeAI(process.env.API_KEY)

const model = genAI.getGenerativeModel({ model: "gemini-1.5-flash" })
const prompt = "write a one sentence fact about the human body";


export async function run(prompt) {
    try {
        const result = await model.generateContent(prompt);
        console.log(result.response.text());
        console.log('response obj', result.response)
        return result.response.text()
    } catch (err) {
        console.error(err)
        //an error returns obj with status 400, use that to check
        return err
    }
}
export function checkResponse(response) {
    if(response.status === 400 || typeof response !== 'string') {
        return false
    }
    
    return true
}


run(prompt)