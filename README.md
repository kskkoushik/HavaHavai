Chatbot Application Documentation
────────────────────────────────────────────

Overview
────────
This is a Flask-based chatbot application that processes user messages, enriches them with additional context from a RAG (Retrieval Augmented Generation) query, and generates an AI-driven response. The application uses external modules (ai_engine and ragdata) to handle AI response generation and data retrieval, and converts markdown responses into HTML using the markdown2 library.

Key Features
────────────
• Chat functionality with dynamically generated contexts.
• Integration with a RAG system to fetch supplementary data based on user input.
• AI-driven responses processed through a dedicated engine.
• Markdown-to-HTML conversion for well-formatted responses.
• Initial support for multiple users, with a single-user configuration used by default.

Installation and Setup
────────────────────────
1. Prerequisites:
   - Python 3.x installed on your system.
   - Required Python libraries: Flask, markdown2.
   - Ensure the custom modules ai_engine and ragdata are present in your project directory.

2. Installing Dependencies:
   Use pip to install required packages:
     pip install Flask markdown2

3. Configuration:
   - The application uses a secret key for session management. By default, the key is set as "Radheradhe". For production, update this with a secure key.
   - The multi-user functionality is conceptual; currently, the application is configured to handle a single user.

Running the Application
─────────────────────────
Execute the application by running:
   python app.py

The Flask development server will start in debug mode, allowing you to test and develop the chatbot functionality.

Endpoints
─────────
1. GET /
   - Description: Renders the homepage.
   - Functionality: Returns the index.html template which serves as the front-end for the chatbot.

2. POST /chat
   - Description: Processes the user’s chat message.
   - Expected Request: A JSON payload containing the key "message" (e.g., { "message": "Your input here" }).
   - Processing Steps:
       a. Retrieves the user's message from the JSON data.
       b. Calls the rag_query function from the ragdata module with the user message and a constant identifier ("RadheKrishna") to fetch additional data.
       c. Enhances the original message by appending a formatted section that includes the retrieved RAG data.
       d. Constructs a conversation history list including the enhanced user message.
       e. Passes the enhanced message and history to the ai_response function from the ai_engine module to generate an AI response.
       f. Converts the AI response from markdown to HTML using markdown2.markdown.
       g. Appends the AI response to the conversation history and returns the HTML formatted reply as a JSON response.
   - Response: A JSON object containing the key "reply" with the HTML formatted AI response.

Customization and Extensions
────────────────────────────
• Message Formatting:
   The user message is modified to include a clear delineation of the RAG data. This ensures both clarity for debug output and structured processing of the context.

• External Module Integration:
   Editing or extending the behavior of the AI response (ai_engine) or data query (ragdata) can tailor the chatbot to specific application requirements.

• Multi-user Support:
   While the application is designed with a concept for multiple users, the current implementation operates in a single user mode for simplicity. To support multiple users, further management of session or user-specific conversation histories would be needed.

Additional Notes
────────────────
• Debug Mode:
   The application is run in debug mode during development. Remember to disable debug mode and configure appropriate production settings before deployment.

• Security Considerations:
   Update the secret_key with a secure, unpredictable value in production environments to ensure safe session management.

This documentation provides an overview of the application’s architecture and functionality as derived from the current source code. For further details regarding the AI response generation and RAG querying logic, refer to the respective modules: ai_engine and ragdata.