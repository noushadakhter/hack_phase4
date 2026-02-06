# Phase III: Todo AI Chatbot - Implementation Plan

## 1. Introduction
This implementation plan details the steps required to build the "Phase III: Todo AI Chatbot" based on the provided specifications and architecture. The development will follow a strict Spec-Driven Development and Agentic Dev Stack workflow.

## 2. Overall Strategy
The implementation will proceed in a modular fashion, starting with the backend infrastructure (database, ORM, migrations, API endpoints), then the MCP Server and tools, followed by the OpenAI Agent integration, and finally the ChatKit frontend. Authentication will be integrated at each relevant stage.

## 3. Task Breakdown

### Phase 1: Backend Infrastructure (FastAPI, SQLModel, PostgreSQL, Alembic)

*   **Task 1.1: Setup FastAPI Project Structure**
    *   Create `backend/` directory with basic FastAPI app structure.
    *   Install FastAPI, Uvicorn, SQLModel, Alembic, Psycopg2.
    *   Setup `requirements.txt` in `backend/`.

*   **Task 1.2: Configure Database (Neon PostgreSQL)**
    *   Define environment variables for `DATABASE_URL` in `backend/.env.example`.
    *   Configure `SQLModel` to connect to PostgreSQL.

*   **Task 1.3: Implement SQLModel Database Models**
    *   Define `Task`, `Conversation`, and `Message` models in `backend/models.py` based on specifications.
    *   Ensure proper type hints and relationships (e.g., `conversation_id` FK).
    *   Add `created_at` and `updated_at` fields with appropriate defaults/callbacks.

*   **Task 1.4: Setup Alembic Migrations**
    *   Initialize Alembic in `backend/migrations`.
    *   Configure `alembic.ini` and `env.py` to work with SQLModel.
    *   Generate initial migration script for `Task`, `Conversation`, and `Message` models.
    *   Apply migration to create tables in the database.

*   **Task 1.5: Implement Database CRUD Operations (backend/app/crud.py)**
    *   Create `crud.py` for `Task`, `Conversation`, and `Message` models.
    *   Functions for creating, reading, updating, and deleting tasks.
    *   Functions for managing conversations and messages (e.g., `get_conversation_history`, `save_message`).

*   **Task 1.6: Develop Base API Endpoints (backend/main.py)**
    *   Create a basic FastAPI app in `backend/main.py`.
    *   Implement health check endpoint.

### Phase 2: Authentication (Better Auth)

*   **Task 2.1: Integrate Better Auth**
    *   Install Better Auth library (if available, otherwise mock/stub as per instructions).
    *   Configure FastAPI to use Better Auth for endpoint protection.
    *   Implement dependency for extracting `user_id` from authenticated requests.

*   **Task 2.2: Secure Chat Endpoint**
    *   Apply authentication dependency to the chat endpoint (`POST /api/{user_id}/chat`).
    *   Ensure `user_id` in the path matches the authenticated user's ID.

### Phase 3: MCP Server and Tools

*   **Task 3.1: Setup MCP Server Structure**
    *   Create `mcp_server/` directory.
    *   Install Official MCP SDK.

*   **Task 3.2: Implement MCP Tools (`add_task`, `list_tasks`, `complete_task`, `delete_task`, `update_task`)**
    *   Each tool function will encapsulate the logic for interacting with the database via the CRUD operations defined in `backend/app/crud.py`.
    *   Ensure tool functions return the specified response format.
    *   These tools will be callable by the OpenAI Agent.

### Phase 4: OpenAI Agent Integration

*   **Task 4.1: Setup OpenAI Agent Runner**
    *   Install OpenAI Agents SDK.
    *   Configure the agent to use the MCP tools.
    *   Define the agent's internal roles: `IntentClassifier`, `ToolSelector`, `ToolExecutor`, `ResponseFormatter`.

*   **Task 4.2: Implement Agent Behavior and Intent Mapping**
    *   Map user intents (e.g., "add", "list") to the corresponding MCP tools.
    *   Implement logic for confirming actions with the user.
    *   Develop robust error handling within the agent's responses.

*   **Task 4.3: Integrate Agent into FastAPI Chat Endpoint**
    *   Modify `POST /api/{user_id}/chat` to:
        1.  Fetch conversation history.
        2.  Append new message.
        3.  Save user message.
        4.  Run the OpenAI Agent with the current conversation history.
        5.  Capture agent's tool calls and response.
        6.  Save assistant message and tool calls.
        7.  Return agent's response to the frontend.

### Phase 5: Frontend (OpenAI ChatKit)

*   **Task 5.1: Setup ChatKit Project**
    *   Create `frontend/` directory if not already present.
    *   Initialize ChatKit project.
    *   Configure `NEXT_PUBLIC_OPENAI_DOMAIN_KEY` environment variable.

*   **Task 5.2: Develop Chat UI**
    *   Implement the core chat interface components.
    *   Display conversation history.
    *   Input field for user messages.
    *   Send button.

*   **Task 5.3: Implement Conversation Continuity**
    *   Manage `conversation_id` to ensure continuous conversations.
    *   Handle new conversations (no `conversation_id`).

*   **Task 5.4: Integrate with FastAPI Chat API**
    *   Make API calls to `POST /api/{user_id}/chat`.
    *   Handle request and response parsing.

*   **Task 5.5: Implement Loading States and Error Display**
    *   Show loading indicators during API calls.
    *   Display error messages gracefully to the user.

### Phase 6: Documentation and Deliverables

*   **Task 6.1: Update `README.md`**
    *   Provide clear instructions for setup, running the backend, mcp_server, and frontend.
    *   Explain the project's purpose, architecture, and features.

*   **Task 6.2: Create `.env.example` files**
    *   For both backend and frontend, detailing all necessary environment variables.

*   **Task 6.3: Code Review and Refinement**
    *   Ensure clean architecture, typed Python, modular structure.
    *   Verify logging, error handling, and security best practices.
    *   Confirm deployment readiness.

## 4. Dependencies
- Python 3.9+
- Node.js (for frontend)
- Docker/Docker Compose (for local development of PostgreSQL)
- Neon PostgreSQL Account

## 5. Risks and Mitigations
- **Complexity of OpenAI Agents SDK**: Potential steep learning curve. Mitigation: Thorough documentation review and incremental implementation.
- **Better Auth Integration**: Specific implementation details may vary. Mitigation: Start with a basic integration and iterate.
- **Frontend-Backend Integration**: Ensuring smooth data flow and error handling between ChatKit and FastAPI. Mitigation: Incremental development and thorough testing of API endpoints.
- **Stateless Backend Challenge**: Properly persisting all necessary state in the DB. Mitigation: Careful design of database schemas and CRUD operations.

## 6. Definition of Done
- All specifications met.
- All tasks in this plan are completed and verified.
- Code is clean, well-tested, and adheres to quality bar.
- Project is deployable.
- All deliverables are provided.