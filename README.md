# Phase III: Todo AI Chatbot

This project implements an AI-powered chatbot that manages todo tasks through natural language, following a strict Spec-Driven Development and Agentic Dev Stack workflow.

## Project Structure

```
.
├── backend/                  # FastAPI backend and SQLModel models
│   ├── app/                  # Application logic (database, auth, API endpoints)
│   ├── migrations/           # Alembic database migrations
│   ├── .env.example          # Example environment variables for backend
│   ├── requirements.txt      # Python dependencies for backend
│   ├── main.py               # Main FastAPI application
│   └── models.py             # SQLModel database models
├── frontend/                 # Next.js frontend (basic chat UI)
│   ├── public/
│   ├── src/
│   │   ├── app/              # Next.js App Router pages
│   │   └── styles/           # Global styles (Tailwind CSS)
│   ├── .env.local.example    # Example environment variables for frontend
│   ├── package.json          # Node.js dependencies for frontend
│   └── ...                   # Other Next.js config files
├── mcp_server/               # Model Context Protocol (MCP) server with tools
│   ├── requirements.txt      # Python dependencies for MCP server
│   ├── main.py               # FastMCP application to expose tools
│   └── tools.py              # Definitions of MCP tools (add_task, list_tasks, etc.)
├── specs/                    # Project specifications, architecture, and plan
│   ├── phase3-todo-chatbot/
│   │   ├── spec.md           # Detailed project specification
│   │   ├── architecture.md   # High-level architecture diagram
│   │   └── plan.md           # Implementation plan and task breakdown
│   └── ...
└── README.md                 # Project README (this file)
```

## Mandatory Tech Stack

*   **Frontend**: Next.js (as placeholder for OpenAI ChatKit)
*   **Backend**: Python FastAPI
*   **AI Framework**: OpenAI Agents SDK
*   **MCP Server**: Official MCP SDK (via `fastmcp`)
*   **ORM**: SQLModel
*   **Database**: Neon Serverless PostgreSQL
*   **Authentication**: Better Auth (stubbed)

## Setup and Running the Project

### 1. Prerequisites

*   Python 3.11+
*   Node.js (LTS recommended) & npm
*   A Neon PostgreSQL database instance.
*   An OpenAI API Key.

### 2. Backend Setup

1.  **Navigate to the `backend` directory:**
    ```bash
    cd backend
    ```
2.  **Create a `.env` file:**
    Copy the contents of `.env.example` to a new file named `.env` and fill in your database URL and OpenAI API Key.
    ```bash
    cp .env.example .env
    ```
    Example `.env` content:
    ```
    DATABASE_URL="postgresql+psycopg2://[USER]:[PASSWORD]@[ENDPOINT_HOSTNAME]/[DATABASE_NAME]?sslmode=require"
    OPENAI_API_KEY="sk-your-openai-key"
    MCP_SERVER_URL="http://localhost:8001" # Default URL for the FastMCP server
    ```
3.  **Install Python dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
4.  **Run Alembic migrations:**
    ```bash
    alembic upgrade head
    ```
    *Note: If you encounter errors during migration, ensure your `DATABASE_URL` is correct and accessible.*
5.  **Run the FastAPI backend:**
    ```bash
    uvicorn main:app --reload --port 8000
    ```
    The backend API will be available at `http://localhost:8000`.

### 3. MCP Server Setup

1.  **Navigate to the `mcp_server` directory:**
    ```bash
    cd mcp_server
    ```
2.  **Install Python dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
3.  **Run the FastMCP server:**
    ```bash
    fastmcp run main:app --port 8001
    ```
    The MCP server will be available at `http://localhost:8001`.

### 4. Frontend Setup

1.  **Navigate to the `frontend` directory:**
    ```bash
    cd frontend
    ```
2.  **Create a `.env.local` file:**
    Copy the contents of `.env.local.example` (you might need to create this file based on backend `.env.example` for `NEXT_PUBLIC_OPENAI_DOMAIN_KEY` if ChatKit was used, but for now we'll use `NEXT_PUBLIC_API_BASE_URL`).
    ```bash
    cp .env.local.example .env.local
    ```
    Example `frontend/.env.local` content:
    ```
    NEXT_PUBLIC_API_BASE_URL="http://localhost:8000"
    ```
3.  **Install Node.js dependencies:**
    ```bash
    npm install
    ```
4.  **Run the Next.js frontend:**
    ```bash
    npm run dev
    ```
    The frontend will be available at `http://localhost:3000`.

## API Endpoints

### Backend (FastAPI)

*   `GET /health`: Health check.
*   `POST /api/{user_id}/chat`: Main chat endpoint for AI interaction.

### MCP Server (FastMCP)

*   Exposes tools: `add_task`, `list_tasks`, `complete_task`, `delete_task`, `update_task`.

## How to Interact

1.  Start the Backend, MCP Server, and Frontend in separate terminal windows.
2.  Open your browser to `http://localhost:3000`.
3.  Use the chat interface to interact with the Todo AI Chatbot. Example commands:
    *   "Add a new task: Buy groceries"
    *   "List my pending tasks"
    *   "Complete task 1" (assuming task ID 1 exists)
    *   "Update task 2 title to: Read a book"
    *   "Delete task 3"

## Deliverables Completed

1.  System design (`specs/phase3-todo-chatbot/spec.md`, `architecture.md`)
2.  Detailed specs (`specs/phase3-todo-chatbot/spec.md`)
3.  Implementation plan (`specs/phase3-todo-chatbot/plan.md`)
4.  Backend code (`backend/`)
5.  MCP server code (`mcp_server/`)
6.  Frontend code (`frontend/`)
7.  SQLModel models (`backend/models.py`)
8.  Alembic migrations (`backend/migrations/`)
9.  Env examples (`backend/.env.example`, `frontend/.env.local.example`)
10. README (`README.md`)