# Core Specification: Phase III - Todo AI Chatbot

## 1. Project Objective

The primary objective of this project is to build a production-grade, AI-powered chatbot that allows users to manage their to-do tasks using natural language. The system will be built upon a modern, agentic stack featuring a stateless backend architecture orchestrated via the Model Context Protocol (MCP).

## 2. High-Level Architecture Rules

- **Stateless Backend:** The FastAPI backend must be fully stateless. All conversation state must be persisted in the database.
- **Stateful Conversations:** The application must support resuming conversations across sessions by storing conversation history (`Conversation` and `Message` models) in the database.
- **Agent-Tool Interaction:** The AI Agent (built with the OpenAI Agents SDK) is strictly prohibited from interacting with the database directly. All data-related actions (e.g., creating, reading, updating tasks) MUST be performed by invoking stateless MCP tools.
- **MCP Tool Design:** All tools exposed to the agent via the MCP server must be stateless functions. They receive all necessary context (like `user_id`) via their arguments.

## 3. Functional Features

- **Natural Language Interaction:** Users will interact with the system via a chat interface, issuing commands in plain English.
- **Task Management CRUD:**
  - **Add:** Create new tasks.
  - **List:** View existing tasks, with filtering options (all, pending, completed).
  - **Update:** Modify the title or description of a task.
  - **Complete:** Mark a task as completed.
  - **Delete:** Remove a task.
- **Conversational Experience:**
  - **Session Resumption:** Users can close the chat and resume their conversation later, with full history intact.
  - **Friendly Confirmations:** The chatbot will provide clear, user-friendly confirmations after performing an action (e.g., "✅ Task 'Buy milk' has been added!").
  - **Graceful Error Handling:** The system will handle invalid commands or failed operations gracefully, providing helpful feedback to the user (e.g., "Sorry, I couldn't find a task with that ID. Please try again.").

## 4. Technology Stack

- **Frontend:** OpenAI ChatKit
- **Backend:** FastAPI (Python)
- **AI Framework:** OpenAI Agents SDK
- **MCP Server:** Official MCP SDK
- **ORM:** SQLModel
- **Database:** Neon Serverless PostgreSQL
- **Authentication:** Better Auth
