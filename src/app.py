from flask import Flask, render_template, request, jsonify
import json
import requests
import chatbot  # Make sure this line is at the top of your app.py

app = Flask(__name__, template_folder="templates", static_folder="static")

def load_scraped_data():
    """Load scraped content."""
    try:
        with open("scraped_data.json", "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        return {"error": "Scraped data not found. Please scrape first."}

@app.route("/")
def home():
    return render_template("index.html")  # This should be inside the templates/ folder

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json['message']
    response = chatbot.get_bot_response(user_message)  # Assuming chatbot.py has this function
    return jsonify({"response": response})

@app.route("/scrape", methods=["POST"])
def scrape():
    """Scrape a given URL."""
    url = request.json.get("url")
    if not url:
        return jsonify({"error": "URL required!"}), 400

    from scraper import scrape_website
    data = scrape_website(url)
    
    # Save scraped data to a file (optional, if you need to persist data)
    with open("scraped_data.json", "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

    return jsonify(data)

@app.route("/ask", methods=["POST"])
def ask():
    """Chatbot API"""
    query = request.json.get("query")
    data = load_scraped_data()

    if "error" in data:
        return jsonify(data), 400
    
    from chatbot import chatbot_response
    response = chatbot_response(query, data)
    return jsonify({"response": response})

if __name__ == '__main__':
    app.run(debug=True)
