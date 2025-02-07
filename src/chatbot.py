import json
import re
import requests  # For LLM API calls

def load_scraped_data():
    """Load the scraped data from the JSON file."""
    try:
        with open("scraped_data.json", "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        return {"error": "No scraped data found. Please scrape a website first."}

def chatbot_response(query, data):
    """Generate chatbot response based on user query and scraped data."""
    query = query.lower()

    # Basic keyword matching
    if "name" in query or "company" in query:
        return f"The company name is: {data.get('title', 'Unknown')}."
    
    if "details" in query or "about" in query:
        return f"This is about: {data.get('headings', ['No description found'])[0]}"
    
    if "summary" in query or "summarize" in query:
        return llm_summarize(data.get("content", "No content found."))  # Call LLM API
    
    return "I'm sorry, I don't have an answer to that question. Try asking something else!"

# LLM API (Groq or OpenAI)
def llm_summarize(text):
    """Use an LLM API to summarize scraped content."""
    api_url = "https://api.groq.com/v1/completions"  # Replace with the correct API
    headers = {"Authorization": "Bearer YOUR_API_KEY", "Content-Type": "application/json"}
    payload = {
        "model": "llama3",  # Use any free LLM model
        "messages": [{"role": "system", "content": "Summarize this:" + text}]
    }

    response = requests.post(api_url, headers=headers, json=payload)
    return response.json().get("choices", [{}])[0].get("message", {}).get("content", "LLM API failed.")

# Run chatbot
if __name__ == "__main__":
    data = load_scraped_data()
    if "error" in data:
        print(data["error"])
    else:
        print("🤖 Chatbot is ready! Type 'exit' to quit.")
        while True:
            query = input("You: ")
            if query.lower() in ["exit", "quit"]:
                print("👋 Goodbye!")
                break
            print(f"Bot: {chatbot_response(query, data)}")
