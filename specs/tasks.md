# Implementation Tasks

This checklist breaks down the implementation plan into actionable development tasks.

## Phase 1: Backend Development

- [ ] **Task 1.1: Core Backend Setup**
  - [ ] Create `backend/settings.py` to load environment variables.
  - [ ] Create `backend/models.py` with `User`, `Task`, `Conversation`, `Message` SQLModel classes.
  - [ ] Create `backend/db.py` with database engine and session logic.

- [ ] **Task 1.2: Authentication**
  - [ ] Create `backend/auth.py` with password hashing and JWT functions.
  - [ ] Implement `/register` and `/login` endpoints in the `auth.py` router.

- [ ] **Task 1.3: MCP Tools**
  - [ ] Create `backend/mcp_server.py`.
  - [ ] Implement `add_task` function.
  - [ ] Implement `list_tasks` function.
  - [ ] Implement `update_task` function.
  - [ ] Implement `complete_task` function.
  - [ ] Implement `delete_task` function.
  - [ ] Configure and run the MCP server, registering all tool functions.

- [ ] **Task 1.4: AI Agent**
  - [ ] Create `backend/agent.py`.
  - [ ] Configure the OpenAI Agent with instructions from `agent-spec.md`.
  - [ ] Implement the main agent logic to process conversations and call MCP tools.

- [ ] **Task 1.5: API & Main App**
  - [ ] Create `backend/chat_endpoint.py`.
  - [ ] Implement the `POST /api/{user_id}/chat` endpoint logic (get/create conversation, save messages, call agent).
  - [ ] Create `backend/main.py` to initialize the FastAPI app.
  - [ ] Include `auth.py` and `chat_endpoint.py` routers in `main.py`.

- [ ] **Task 1.6: Database Migrations**
  - [ ] Install `alembic` (`pip install alembic`).
  - [ ] Initialize Alembic in the `backend` directory (`alembic init migrations`).
  - [ ] Configure `alembic.ini` and `migrations/env.py` to work with SQLModel.
  - [ ] Generate the initial migration script (`alembic revision --autogenerate -m "Initial schema"`).
  - [ ] Apply the migration (`alembic upgrade head`).

## Phase 2: Frontend Development

- [ ] **Task 2.1: Core Frontend Setup**
  - [ ] Initialize a new Next.js application in the `frontend` directory.
  - [ ] Install OpenAI ChatKit and other necessary dependencies (e.g., `axios`, `zustand`).

- [ ] **Task 2.2: Authentication UI**
  - [ ] Create `frontend/components/Auth.tsx` with login and registration forms.
  - [ ] Implement state management for authentication tokens and user state (e.g., in a Zustand store).

- [ ] **Task 2.3: API Client**
  - [ ] Create `frontend/lib/chat.ts` to handle API calls to the backend chat endpoint.
  - [ ] Ensure the client automatically attaches the auth token to requests.

- [ ] **Task 2.4: Chat UI**
  - [ ] Create `frontend/components/ChatUI.tsx` using OpenAI ChatKit.
  - [ ] Wire the component to the `sendMessage` function from `chat.ts`.
  - [ ] Implement logic in `frontend/app/page.tsx` to show `Auth.tsx` or `ChatUI.tsx` based on auth state.

## Phase 3: Finalization

- [ ] **Task 3.1: Environment Setup**
  - [ ] Create `backend/.env.example`.
  - [ ] Create `frontend/.env.example`.

- [ ] **Task 3.2: Documentation**
  - [ ] Create `README.md` with setup and run instructions.

- [ ] **Task 3.3: Validation**
  - [ ] Create `validation-checklist.md` to verify all requirements.
  - [ ] Manually test all functional features against the checklist.
