function scrapeData() {
    let url = document.getElementById("urlInput").value;
    if (!url) {
        alert("Please enter a URL!");
        return;
    }

    // Show the loading message
    document.getElementById("scrapingMessage").style.display = "block";
    document.getElementById("scrapeButton").disabled = true;

    fetch("/scrape", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ url: url })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById("scrapeStatus").innerText = "✅ Scraping successful!";
        document.getElementById("scrapingMessage").style.display = "none";
        document.getElementById("scrapeButton").disabled = false;
    })
    .catch(error => {
        console.error("Error:", error);
        document.getElementById("scrapeStatus").innerText = "❌ Error scraping data.";
        document.getElementById("scrapingMessage").style.display = "none";
        document.getElementById("scrapeButton").disabled = false;
    });
}

function askChatbot() {
    let query = document.getElementById("queryInput").value;
    if (!query) {
        alert("Please enter a question!");
        return;
    }

    fetch("/ask", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ query: query })
    })
    .then(response => response.json())
    .then(data => {
        let chatbox = document.getElementById("messages");
        chatbox.innerHTML += `<div class='user-message'>You: ${query}</div>`;
        chatbox.innerHTML += `<div class='bot-message'>Bot: ${data.response}</div>`;
        document.getElementById("queryInput").value = "";
        chatbox.scrollTop = chatbox.scrollHeight;
    })
    .catch(error => {
        console.error("Error:", error);
        alert("❌ Error communicating with chatbot.");
    });
}
