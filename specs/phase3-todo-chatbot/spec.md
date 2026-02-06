# Phase III: Todo AI Chatbot - Specification

## 1. Introduction
This document outlines the specifications for "Phase III: Todo AI Chatbot," an AI-powered chatbot designed to manage todo tasks through natural language interactions. The project will adhere strictly to Spec-Driven Development and the Agentic Dev Stack workflow.

## 2. Objective
To build an AI-powered chatbot that manages todos through natural language.

## 3. Architecture Overview
### High-Level Architecture
- **ChatKit UI**: Frontend for user interaction.
- **FastAPI Backend**: Stateless API serving the chatbot.
- **OpenAI Agent (Runner)**: Handles natural language reasoning and task execution.
- **MCP Server (Tools)**: Provides tools for task operations to the OpenAI Agent.
- **Neon PostgreSQL**: Database for persistent storage of tasks and conversation history.

### Backend State
The backend will be stateless. All conversation and task state will be stored in the database.

## 4. Mandatory Tech Stack
- **Frontend**: OpenAI ChatKit
- **Backend**: Python FastAPI
- **AI Framework**: OpenAI Agents SDK
- **MCP Server**: Official MCP SDK
- **ORM**: SQLModel
- **Database**: Neon Serverless PostgreSQL
- **Authentication**: Better Auth

## 5. Database Models

### Task Model
- `id`: `int` (Primary Key)
- `user_id`: `string`
- `title`: `string`
- `description`: `string` (nullable)
- `completed`: `bool`
- `created_at`: `datetime`
- `updated_at`: `datetime`

### Conversation Model
- `id`: `int` (Primary Key)
- `user_id`: `string`
- `created_at`: `datetime`
- `updated_at`: `datetime`

### Message Model
- `id`: `int` (Primary Key)
- `user_id`: `string`
- `conversation_id`: `int` (Foreign Key to Conversation.id)
- `role`: `enum("user", "assistant")`
- `content`: `text`
- `created_at`: `datetime`

## 6. Chat API

### Endpoint: `POST /api/{user_id}/chat`

#### Request
```json
{
  "conversation_id": number, // Optional, for continuing conversations
  "message": string
}
```

#### Response
```json
{
  "conversation_id": number,
  "response": string,
  "tool_calls": array // Details of tools called by the agent
}
```

## 7. MCP Tools (Must Implement)

All task operations MUST be performed only through MCP tools.

### `add_task`
- **Description**: Adds a new todo task.
- **Parameters**:
  - `user_id`: `string`
  - `title`: `string`
  - `description`: `string` (optional)
- **Returns**: `{ task_id: int, status: string, title: string }`

### `list_tasks`
- **Description**: Lists todo tasks based on status.
- **Parameters**:
  - `user_id`: `string`
  - `status`: `enum("all", "pending", "completed")` (optional, default "all")
- **Returns**: `[{id: int, title: string, completed: bool}]`

### `complete_task`
- **Description**: Marks a specific task as completed.
- **Parameters**:
  - `user_id`: `string`
  - `task_id`: `int`
- **Returns**: `{ task_id: int, status: string, title: string }`

### `delete_task`
- **Description**: Deletes a specific todo task.
- **Parameters**:
  - `user_id`: `string`
  - `task_id`: `int`
- **Returns**: `{ task_id: int, status: string, title: string }`

### `update_task`
- **Description**: Updates the title or description of a specific task.
- **Parameters**:
  - `user_id`: `string`
  - `task_id`: `int`
  - `title`: `string` (optional)
  - `description`: `string` (optional)
- **Returns**: `{ task_id: int, status: string, title: string }`

## 8. Agent Design

### Agent Type
One Main Agent.

### Internal Roles
- `IntentClassifier`
- `ToolSelector`
- `ToolExecutor`
- `ResponseFormatter`

### Agent Behavior
- **Intent Mapping**:
  - `add`/`create`/`remember` → `add_task`
  - `show`/`list` → `list_tasks`
  - `done`/`complete` → `complete_task`
  - `delete`/`remove` → `delete_task`
  - `change`/`update`/`rename` → `update_task`
- **Confirmation**: Always confirm actions with the user.
- **Error Handling**: Handle errors gracefully.

## 9. Stateless Request Flow
1. Receive request (`POST /api/{user_id}/chat`).
2. Fetch conversation history from DB (using `conversation_id` from request, or create new if not provided).
3. Append new user message to history.
4. Save user message to DB.
5. Run agent with MCP tools, providing full conversation history as context.
6. Capture tool calls made by the agent.
7. Save assistant's response message and tool calls to DB.
8. Return response.

## 10. Frontend

### Technology
OpenAI ChatKit.

### Features
- Chat UI
- Conversation continuity
- Loading states
- Error display

### Environment Variable
`NEXT_PUBLIC_OPENAI_DOMAIN_KEY`

## 11. Authentication
- **Technology**: Better Auth.
- **Protection**: Protect the chat endpoint (`POST /api/{user_id}/chat`).
- **User Association**: Associate `user_id` in API calls with the authenticated user.

## 12. Repository Structure
- `/frontend`
- `/backend`
- `/mcp_server`
- `/specs`
- `/migrations`
- `README.md`

## 13. Quality Bar
- Clean architecture
- Async FastAPI
- Typed Python
- Modular structure
- Logging
- Error handling
- Security best practices
- Deployment ready

## 14. Deliverables
1. System design (this document and future architecture diagram)
2. Detailed specs (this document)
3. Implementation plan
4. Backend code
5. MCP server code
6. Frontend code
7. SQLModel models
8. Alembic migrations
9. Env examples
10. README