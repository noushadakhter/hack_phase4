# Implementation Plan: Phase III - Todo AI Chatbot

This document outlines the architectural approach and step-by-step plan to implement the Todo AI Chatbot based on the provided specifications.

## 1. Backend Implementation (`/backend`)

The backend will be built using FastAPI, following the structure specified in the prompt.

### 1.1. Core Setup (`settings.py`, `db.py`, `models.py`)
- **`settings.py`:** Will use Pydantic's `BaseSettings` to manage environment variables (Database URL, OpenAI keys, etc.).
- **`models.py`:** SQLModel classes for `User`, `Task`, `Conversation`, and `Message` will be created exactly as defined in `database-spec.md`. Relationships between models will be explicitly defined.
- **`db.py`:** Will contain the database engine creation logic and a dependency `get_session` to provide SQLAlchemy sessions to repository functions. It will also include a `create_db_and_tables` function.

### 1.2. Authentication (`auth.py`)
- An implementation of "Better Auth" will be created. This implies a robust, secure, and possibly social-auth-ready module. For the initial phase, it will provide secure password hashing (using passlib) and JWT token generation/validation for API security. It will expose a router with `/login` and `/register` endpoints.

### 1.3. MCP Tooling (`mcp_server.py`)
- This file will implement the five required MCP tools (`add_task`, `list_tasks`, etc.) as defined in `mcp-tools-spec.md`.
- Each tool will be a stateless Python function that accepts a database session and the required parameters.
- These functions will contain the core business logic (database queries using SQLModel) for interacting with the `Task` table.
- The file will also set up and run the MCP server, registering these functions as callable tools.

### 1.4. AI Agent (`agent.py`)
- This file will use the `OpenAI Agents SDK`.
- It will define the agent's instructions, personality, and available tools (pointing to the tools served by the `mcp_server.py`).
- The main function here will take a `user_id`, `conversation_id`, and a `message`, load the conversation history from the DB, run the agent with the new message, and return the agent's response and any tool calls.

### 1.5. API Endpoint (`chat_endpoint.py`, `main.py`)
- **`chat_endpoint.py`:** Will define the FastAPI router for the `POST /api/{user_id}/chat` endpoint.
  - This endpoint will handle the request validation.
  - It will get or create a `conversation_id`.
  - It will save the user's incoming message to the `Message` table.
  - It will call the main logic in `agent.py`.
  - It will save the agent's response to the `Message` table.
  - It will return the final response object as defined in `api-spec.md`.
- **`main.py`:** The main FastAPI application file. It will initialize the app, include the routers from `chat_endpoint.py` and `auth.py`, and handle application startup events (like `create_db_and_tables`).

### 1.6. Database Migrations (`migrations/`)
- Alembic will be configured to manage database schema migrations. The initial migration script will be generated based on the SQLModel definitions in `models.py`.

## 2. Frontend Implementation (`/frontend`)

The frontend will be built using Next.js and OpenAI's ChatKit, following the specified structure.

### 2.1. Authentication (`components/Auth.tsx`)
- This component will provide the UI for user login and registration.
- It will interact with the backend's `/auth/login` and `/auth/register` endpoints.
- Upon successful login, it will store the JWT token securely (e.g., in a state management store like Zustand and `localStorage`).

### 2.2. Chat UI (`components/ChatUI.tsx` and `app/page.tsx`)
- **`ChatUI.tsx`:** This will be the core component for the chat interface, built using OpenAI's ChatKit. It will be responsible for:
  - Displaying the conversation history (user and assistant messages).
  - Providing a text input for the user.
  - Handling message submission.
- **`app/page.tsx`:** This will be the main page of the application. It will conditionally render either the `Auth.tsx` component (if the user is not authenticated) or the `ChatUI.tsx` component (if the user is authenticated).

### 2.3. API Interaction (`lib/chat.ts`)
- This file will contain the client-side logic for communicating with the backend.
- It will export a function, e.g., `sendMessage(userId, conversationId, message)`, which makes a `POST` request to the `/api/{user_id}/chat` endpoint.
- It will handle attaching the JWT token to the request headers for authentication.

## 3. Order of Operations

1.  **Backend First:**
    1.  Set up `settings.py`, `models.py`, and `db.py`.
    2.  Implement `auth.py` for user registration and login.
    3.  Implement the MCP tools in `mcp_server.py`.
    4.  Implement the agent logic in `agent.py`.
    5.  Implement the chat endpoint in `chat_endpoint.py` and tie everything together in `main.py`.
    6.  Set up and run the initial database migration.
2.  **Frontend Second:**
    1.  Set up the basic Next.js project.
    2.  Build the `Auth.tsx` component.
    3.  Implement the `chat.ts` library for API calls.
    4.  Build the `ChatUI.tsx` component using ChatKit.
    5.  Implement the main logic in `app/page.tsx` to switch between `Auth` and `ChatUI`.
3.  **Finalization:**
    1.  Create `.env.example` files for both frontend and backend.
    2.  Write the `README.md`.
    3.  Create the `validation-checklist.md`.
