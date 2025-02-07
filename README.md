# Web Scraper Chatbot

This project integrates a web scraper and a chatbot into a single application. Users can input a URL to scrape website data, which is then stored and used by a chatbot to answer questions based on the scraped content. It's a fun and interactive way to combine web scraping with conversational AI.

## Features

- **Web Scraping:** Enter any valid URL, and the application will scrape the data from the website.
- **Chatbot Integration:** Ask questions based on the scraped content, and the bot will respond with relevant answers.
- **Responsive Interface:** The UI is responsive, making it accessible on both desktop and mobile devices.
- **Attractive Design:** The user interface includes interactive buttons and colorful elements to enhance user experience.

 ## Edge Cases Handled
- **Invalid URL Input:** If the user doesn't provide a valid URL or leaves the URL field blank, the scraper won't function and will prompt the user to enter a valid URL.

- **Empty or Missing Scraped Data:** If the user tries to ask the chatbot without scraping any data first, the application will return an error message saying "Scraped data not found. Please scrape first."

- **Chatbot Query without Input:** If the user tries to ask the chatbot without entering a question, the chatbot will prompt the user to enter a query.

- **Scraping Failure:** If the scraping fails (e.g., the website is unreachable or doesn't allow scraping), an error message will notify the user.

- **Unreachable Website:** If the website cannot be reached due to connectivity issues or restrictions, the application will notify the user with an error message like "Error fetching data."

 ## Example
Scrape a Website:

Input the URL https://www.example.com in the input field and click the Scrape button.
The application will scrape the website and store its textual content.
Ask the Chatbot:

Once the website is scraped, you can ask the chatbot, for example: "What is the name of the college?"
If the scraped data contains the information about the college name, the chatbot will respond with the relevant information, such as "The name of the college is Example College."
 

## Technologies Used

- **Flask:** A lightweight web framework to build the server-side of the application.
- **HTML/CSS:** For creating the front-end layout and styling.
- **JavaScript:** Handles the front-end logic, including sending requests to the Flask API for scraping and chatbot interactions.
- **Python:** The core language used for scraping, chatbot logic, and backend operations.

## Setup

To set up this project locally, follow these steps:

### Prerequisites

- **Python 3.x**
- **pip (Python package manager)**
- **Flask** library (web framework)
- **BeautifulSoup** and **requests** libraries (for scraping)

### Step 1: Clone the Repository

```bash
git clone <repository-url>
cd web_scraper_chatbot
```

### Step 2: Install Dependencies

Install all the required Python libraries using pip:

```bash
pip install -r requirements.txt
```

### Step 3: Run the Application

Set the Flask app environment variable and run the Flask server:

**For Windows:**
```bash
set FLASK_APP=app.py
flask run
```

**For macOS/Linux:**
```bash
export FLASK_APP=app.py
flask run
```

The application will run on `http://127.0.0.1:5000`.

### Step 4: Access the Web App

Open your browser and go to `http://127.0.0.1:5000` to access the web scraper chatbot.

## How It Works

### Web Scraping:

1. Enter a URL in the input field and press the "Scrape" button.
2. The app sends the URL to the server.
3. The server scrapes the website content and stores it in a JSON file.
4. The app will display a success message once the scraping is complete.

### Chatbot Interaction:

1. Type a question into the "Ask something..." input field.
2. The question is sent to the server, which processes the query based on the scraped data.
3. The chatbot responds with relevant information extracted from the website.

## Folder Structure

```
web_scraper_chatbot/
│
├── app.py               # Main Flask app
├── scraper.py           # Web scraping logic
├── chatbot.py           # Chatbot logic
│
├── templates/
│   └── index.html       # Frontend HTML file
│
├── static/
│   ├── styles.css       # CSS styles for the UI
│   └── script.js        # JavaScript logic for the UI
│
├── scraped_data.json    # Stores the scraped website data
└── requirements.txt     # List of required Python libraries
```

## License

This project is open-source and available under the MIT License.
