# Chatbot Application Documentation

This project is a Flask-based chatbot web application that integrates artificial intelligence with retrieval-augmented generation (RAG). The application receives user messages, retrieves related contextual data using a RAG query, and generates a response using an AI engine. The resulting reply is formatted in Markdown and then converted to HTML for display.

---

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Endpoints](#endpoints)
- [Configuration](#configuration)
- [Code Structure](#code-structure)
- [Dependencies](#dependencies)
- [Notes](#notes)

---

## Overview

The chatbot application is designed to handle interactions with users. When a user sends a message, the application first retrieves contextual data using a RAG query. This data is appended to the user message along with delimiters for clarity. The augmented message is then processed by an AI response engine. The output from the AI engine, initially in Markdown format, is converted to HTML using the `markdown2` library and returned as a JSON response.

---

## Features

- Web-based chatbot interface using Flask.
- Retrieval-augmented generation with a dedicated RAG query.
- AI-generated responses integrated with session-based conversation history.
- Markdown-to-HTML conversion for rich text display.
- Single-user session management with future extensibility for handling multiple users.

---

## Installation

1. **Clone the Repository:**

   ```
   git clone <repository_url>
   cd <repository_directory>
   ```

2. **Create a Virtual Environment (optional but recommended):**

   ```
   python3 -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```

3. **Install Dependencies:**

   ```
   pip install flask markdown2
   ```

   Ensure that the modules `ai_engine` and `ragdata` are available in your project or are installed as needed.

---

## Usage

1. **Run the Application:**

   ```
   python app.py
   ```

2. **Access the Application:**

   Open a browser and navigate to [http://localhost:5000](http://localhost:5000).

3. **Chat Interaction:**

   - The home page (`/`) serves the main interface.
   - User messages are sent to the `/chat` endpoint via a POST request.
   - The server processes the message, augments it with RAG data, and responds with AI-generated content.

---

## Endpoints

### GET /

- **Description:** Renders the main chat interface.
- **Response:** HTML content from `index.html`.

### POST /chat

- **Description:** Receives a user message in JSON format, processes it with the RAG query and AI engine, and returns a formatted reply.
- **Request Payload Example:**
  ```json
  {
    "message": "Hello, how are you?"
  }
  ```
- **Processing Details:**
  - Uses the function `rag_query` with the parameter "RadheKrishna" to retrieve contextual data.
  - Constructs an augmented message containing the original user message and retrieved RAG data.
  - Updates a conversation history list (with roles "user" and "model").
  - Sends the enhanced message along with conversation history to the `ai_response` function.
  - Converts the AI-generated Markdown reply to HTML using `markdown2.markdown`.
- **Response Example:**
  ```json
  {
    "reply": "<p>Your AI-generated response in HTML format</p>"
  }
  ```

---

## Configuration

- **Secret Key:**  
  The Flask application uses a hardcoded secret key for session management. **Note that this key was updated from "Radheradhe" to "1234".**  
  File: `app.py`  
  ```python
  app.secret_key = "1234"
  ```

- **Comments in Code:**  
  There are inline code comments referencing "Radhakrishn" and a reminder to update the README accordingly.

---

## Code Structure

- **app.py:**  
  Main Flask application file that handles routing and integration of the AI engine and RAG data.
  
- **ai_engine.py:**  
  Contains the definition for the `ai_response` function responsible for generating AI responses (implementation details not shown here).
  
- **ragdata.py:**  
  Contains the definition for the `rag_query` function that fetches related data based on the user message.

- **templates/index.html:**  
  HTML template served as the main interface for the chatbot.

---

## Dependencies

- [Flask](https://flask.palletsprojects.com/)
- [markdown2](https://github.com/trentm/python-markdown2)
- Custom modules: `ai_engine`, `ragdata`

---

## Notes

- This application currently maintains a simple conversation history for a single user session.
- Future enhancements may include multi-user session management and improved security for session handling.
- Ensure that all custom modules (`ai_engine` and `ragdata`) are properly integrated and available in the project environment.

---

This documentation reflects the current state and functionality of the chatbot application. For any questions or contributions, please refer to the project repository.