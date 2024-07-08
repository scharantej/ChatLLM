## Flask Application Design for Google Chat Chatbot Using Internal Resources

### HTML Files
1. **index.html:**
   - Main HTML page
   - Contains the chatbot interface, including a text input for user messages and a chat window for displaying responses.

2. **chat.html:**
   - Embedded in `index.html` as a template for each message
   - Defines the layout and content of individual messages, including sender, timestamp, and message text.

### Routes

1. **`/` (GET):**
   - Serves the `index.html` page, displaying the chatbot interface.

2. **`/chat` (POST):**
   - Receives a POST request from the chatbot interface when a user sends a message.
   - Processes the user's input and generates a response.
   - Returns the response in JSON format, which is rendered in the chat window.

3. **`/resources` (GET):**
   - Serves internal resources such as JavaScript or CSS files necessary for the chatbot's functionality.