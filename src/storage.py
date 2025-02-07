import json
import os

# Path to the conversation history file
CONVERSATION_FILE = "conversations.json"

def save_conversation(user_input, bot_response):
    """Saves the conversation to a file."""
    conversation = {"user_input": user_input, "bot_response": bot_response}
    
    # If the file does not exist, create it
    if not os.path.exists(CONVERSATION_FILE):
        with open(CONVERSATION_FILE, "w") as file:
            json.dump([], file)

    # Load existing conversations
    with open(CONVERSATION_FILE, "r") as file:
        conversations = json.load(file)
    
    # Add the new conversation to the list
    conversations.append(conversation)
    
    # Save the updated conversations to the file
    with open(CONVERSATION_FILE, "w") as file:
        json.dump(conversations, file, indent=4)

def load_conversations():
    """Loads the conversation history."""
    if os.path.exists(CONVERSATION_FILE):
        with open(CONVERSATION_FILE, "r") as file:
            return json.load(file)
    return []
