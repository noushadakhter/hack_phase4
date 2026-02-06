# API Specification

This document specifies the contract for the main API endpoint used for user interaction with the chatbot.

---

## 1. Chat Endpoint

- **Path:** `/api/{user_id}/chat`
- **Method:** `POST`
- **Description:** This is the primary endpoint for all chat-based interactions. It handles receiving a user's message, processing it through the AI agent, and returning the agent's response. The `user_id` in the path identifies the user context for the conversation.

---

## 2. Request Body

- **Content-Type:** `application/json`
- **Structure:**
  ```json
  {
    "conversation_id": 12345,
    "message": "Hello, can you show me my tasks?"
  }
  ```
- **Fields:**
  - `conversation_id` (int, optional): The ID of an existing conversation. If provided, the new message will be appended to this conversation. If omitted, a new conversation will be created.
  - `message` (str, required): The text content of the user's message.

---

## 3. Response Body

- **Content-Type:** `application/json`
- **Success (Status Code `200 OK`) Structure:**
  ```json
  {
    "conversation_id": 12345,
    "response": "Of course! Here are your current tasks: \n1. Buy groceries",
    "tool_calls": [
      {
        "tool_name": "list_tasks",
        "parameters": {
          "user_id": 1,
          "status": "all"
        },
        "result": [
          { "id": 101, "title": "Buy groceries", "completed": false }
        ]
      }
    ]
  }
  ```
- **Fields:**
  - `conversation_id` (int): The ID of the conversation (either the one provided in the request or the newly created one).
  - `response` (str): The natural language response from the AI agent, intended to be displayed to the user.
  - `tool_calls` (array): An array of objects, where each object represents a tool that the agent called during its execution. This is for logging, debugging, and potential frontend use.
    - `tool_name` (str): The name of the called tool (e.g., `list_tasks`).
    - `parameters` (dict): The parameters passed to the tool.
    - `result` (any): The data returned by the tool.

- **Error (Status Code `4xx`/`5xx`) Structure:**
  ```json
  {
    "detail": "A descriptive error message."
  }
  ```
- **Fields:**
  - `detail` (str): A message describing the error (e.g., "User not found", "Invalid request body").

