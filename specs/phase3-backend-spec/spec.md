# Backend Specification: Todo AI Chatbot (Phase III)

**Version:** 1.0.0
**Date:** 2026-01-22
**Status:** Draft

---

## 1. Overview

This document specifies the backend architecture and implementation details for the Phase III Todo AI Chatbot. The backend will be a stateless FastAPI application that serves a conversational AI agent, handles user authentication, and persists data to a PostgreSQL database. All business logic will be executed through a set of strongly-typed MCP (Model Context Protocol) tools.

## 2. Core Technologies

- **Framework:** FastAPI
- **Database ORM:** SQLModel
- **Database:** PostgreSQL (Neon Serverless)
- **Authentication:** `fastapi-better-auth` (Email/Password), JWT
- **AI SDK:** OpenAI Agents SDK

## 3. Architecture & Data Flow

The backend operates on a stateless request-response cycle, governed by the SP Constitution.

1.  A user sends a message via the Frontend to the `/chat` endpoint with a JWT.
2.  The FastAPI server authenticates the user via the JWT.
3.  The server retrieves the `conversation_id` from the request (or creates a new one).
4.  It loads the entire message history for that conversation from the database.
5.  The message history is passed to the OpenAI Agent.
6.  The Agent processes the new message, decides if a tool needs to be called, and invokes the relevant MCP tool.
7.  The MCP tool executes the business logic (e.g., creates a todo in the database), ensuring user ownership and validation.
8.  The tool returns a result to the Agent.
9.  The Agent formulates a natural language response.
10. The new messages (user's prompt and assistant's response) are saved to the database, linked to the conversation.
11. The assistant's response is sent back to the frontend.

## 4. Folder Structure (Proposed)

```
backend/
├── .env
├── main.py           # FastAPI app entrypoint, middleware
├── requirements.txt
├── auth.py           # Auth routes (/signup, /login) & JWT logic
├── chat.py           # Chat logic (/chat endpoint)
├── agent.py          # AI Agent definition & system prompt
├── mcp_server.py     # MCP tool definitions
├── db.py             # Database session management & engine setup
├── models.py         # SQLModel table definitions (User, TodoItem, etc.)
└── schemas.py        # Pydantic schemas for API requests/responses
```

## 5. Database Schema (SQLModel)

File: `models.py`

```python
import uuid
from typing import List, Optional
from sqlmodel import Field, Relationship, SQLModel
from datetime import datetime

class User(SQLModel, table=True):
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    email: str = Field(unique=True, index=True)
    hashed_password: str
    
    todos: List["TodoItem"] = Relationship(back_populates="owner")
    conversations: List["Conversation"] = Relationship(back_populates="owner")

class TodoItem(SQLModel, table=True):
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    content: str
    completed: bool = Field(default=False)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    
    owner_id: uuid.UUID = Field(foreign_key="user.id")
    owner: User = Relationship(back_populates="todos")

class Conversation(SQLModel, table=True):
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    
    owner_id: uuid.UUID = Field(foreign_key="user.id")
    owner: User = Relationship(back_populates="conversations")
    messages: List["Message"] = Relationship(back_populates="conversation")

class Message(SQLModel, table=True):
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    role: str  # "user" or "assistant"
    content: str
    created_at: datetime = Field(default_factory=datetime.utcnow)
    
    conversation_id: uuid.UUID = Field(foreign_key="conversation.id")
    conversation: Conversation = Relationship(back_populates="messages")
```

## 6. API Contract

File: `auth.py`, `chat.py`

### Auth Endpoints

- **`POST /signup`**
  - **Request Body:** `{ "email": "user@example.com", "password": "strongpassword" }`
  - **Response (Success):** `201 OK` `{ "id": "...", "email": "..." }`
  - **Response (Failure):** `400 Bad Request` (user exists)

- **`POST /login`**
  - **Request Body:** `{ "username": "user@example.com", "password": "strongpassword" }` (Uses form data)
  - **Response (Success):** `200 OK` `{ "access_token": "...", "token_type": "bearer" }`
  - **Response (Failure):** `401 Unauthorized`

### Chat Endpoint

- **`POST /chat`** (Protected by JWT)
  - **Request Header:** `Authorization: Bearer <JWT>`
  - **Request Body:** `schemas.py:ChatMessage`
    ```python
    class ChatMessage(BaseModel):
        conversation_id: Optional[uuid.UUID] = None
        message: str
    ```
  - **Response (Success):** `200 OK` `schemas.py:ChatResponse`
    ```python
    class ChatResponse(BaseModel):
        conversation_id: uuid.UUID
        response: str
    ```
  - **Response (Failure):** `401 Unauthorized`, `500 Internal Server Error`

## 7. MCP (Model Context Protocol) Tools

File: `mcp_server.py`

Each tool will be a function that accepts user ID as the first argument to enforce data isolation.

- **`create_todo(user_id: UUID, content: str) -> dict`**
  - Creates a new `TodoItem` for the given user.
  - Returns the created todo item as a dictionary.

- **`list_todos(user_id: UUID, completed: Optional[bool] = None) -> List[dict]`**
  - Lists all `TodoItem` objects for the user.
  - Can filter by completion status.
  - Returns a list of todo items.

- **`update_todo(user_id: UUID, todo_id: UUID, new_content: str) -> dict`**
  - Finds a todo by its ID and updates its content.
  - Verifies the todo belongs to the `user_id`.
  - Returns the updated todo item.

- **`mark_complete(user_id: UUID, todo_id: UUID, is_complete: bool = True) -> dict`**
  - Marks a todo as complete or incomplete.
  - Verifies ownership.
  - Returns the updated todo item.

- **`delete_todo(user_id: UUID, todo_id: UUID) -> dict`**
  - Deletes a todo item by its ID.
  - Verifies ownership.
  - Returns a confirmation message.

## 8. AI Agent System Prompt

File: `agent.py`

```
You are a world-class Todo Manager assistant.
Your name is 'TaskBot'.
You are operating within a strict, tool-based environment (MCP).
You MUST NOT perform any action outside of the provided tools.
You are conversational, friendly, and helpful, but always precise.

Your available tools are:
- `create_todo`: Use when a user wants to add a new todo.
- `list_todos`: Use when a user asks to see their todos.
- `update_todo`: Use when a user wants to change the text of an existing todo.
- `mark_complete`: Use when a user wants to mark a todo as done or not done.
- `delete_todo`: Use when a user wants to remove a todo.

When you perform an action, confirm it clearly. For example: "Okay, I've added 'Buy milk' to your list." or "Done! I've marked 'Finish report' as complete."

If a user asks for something you cannot do, politely decline and state your purpose. For example: "I can only help you manage your todos. I can't set reminders or browse the web."

Always be aware of the user you are talking to and ensure all actions are for them.
```

## 9. Environment Variables

File: `.env`

```
DATABASE_URL="postgresql://user:password@host:port/dbname"
JWT_SECRET_KEY="a_very_strong_and_long_secret_key"
OPENAI_API_KEY="sk-..."
```
