```
## AI-Powered Music Recommendation Chatbot

This AI-powered music recommendation chatbot interacts with users, analyzes the mood and sentiment of the conversation, and provides a Spotify playlist that matches the user's mood.

### Installation

Before running this module, you need to install a few libraries:

```bash
pip install openai
pip install requests
pip install json
pip install flask
```

**Note:** Ensure you have Python installed on your system.

### Spotify API Token

You will require a new Spotify API token, as it expires every hour.

To get a Spotify API token:

1. Visit the Spotify Developer Console.
2. Scroll down and click on the "Get Token" button.
3. Check all the boxes and get the token.
4. Use the token in the code at line 44 under headers -> authorization -> "Bearer {new token}".

### Instructions

#### Input and Output of the Module:

- **Start the Conversation:** The user initiates the conversation with the AI.
  
- **AI Replies:** The AI responds, and you'll get a prompt to either continue or stop.

- **Spotify Playlist:** If you choose to stop, the AI will provide a Spotify playlist link based on the mood of your conversation.

- **Handling Errors:** If the AI does not reply properly or responds with symbols like "?" or ".", use a "?" as the next input to prompt a proper response.

### Frontend Development

The frontend of this project is currently under development. Please use the module for backend verification.

Thank you for using the AI-powered Music Recommendation Chatbot!
```