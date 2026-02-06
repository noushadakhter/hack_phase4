# Implementation Tasks: Phase III - Todo AI Chatbot

This document lists the development tasks required to build the Todo AI Chatbot, based on the architectural plan.

## Phase 1: Backend Development

- [ ] **Task 1.1: Setup Backend Environment**
  - [ ] Create `backend/app` directory structure as per `plan.md`.
  - [ ] Initialize `requirements.txt` with `fastapi`, `uvicorn`, `sqlmodel`, `psycopg2-binary`, `python-dotenv`, `passlib[bcrypt]`, `python-jose[cryptography]`.
  - [ ] Create a virtual environment and install dependencies.

- [ ] **Task 1.2: Database and Models**
  - [ ] Create `backend/app/models.py` with `User` and `Todo` SQLModel classes.
  - [ ] Create `backend/app/database.py` to handle database session and engine creation (connecting to Neon DB via environment variables).
  - [ ] Create initial `backend/.env` file from `.env.example` with a placeholder for the `DATABASE_URL`.
  - [ ] Implement a function to create DB and tables.

- [ ] **Task 1.3: Schemas and CRUD**
  - [ ] Create `backend/app/schemas.py` with Pydantic schemas for `UserCreate`, `UserRead`, `TodoCreate`, `TodoRead`, etc.
  - [ ] Create `backend/app/crud.py` with functions for:
    - `get_user_by_email`
    - `create_user`
    - `get_todos`
    - `create_todo_for_user`
    - `update_todo`
    - `delete_todo`

- [ ] **Task 1.4: Authentication API**
  - [ ] Create `backend/app/dependencies.py` for JWT token handling and user dependency injection.
  - [ ] Create `backend/app/api/endpoints/auth.py` with `/signup` and `/login` routes.
  - [ ] Hash passwords on signup and verify on login.
  - [ ] Return JWT token on successful login.

- [ ] **Task 1.5: Core App and Task API**
  - [ ] Create `backend/app/main.py` to initialize the FastAPI app and include routers.
  - [ ] Create `backend/app/api/endpoints/tasks.py` (optional, for testing) with full CRUD operations for Todos, protected by the JWT dependency.

- [ ] **Task 1.6: Chat Agent API**
  - [ ] Create `backend/app/api/endpoints/chat.py`.
  - [ ] Implement the `/api/chat` endpoint.
  - [ ] Inside the endpoint, create placeholder logic to parse a user's message and call the appropriate `crud` function. (Full NLP integration can be a sub-task).

## Phase 2: Frontend Development

- [ ] **Task 2.1: Setup Frontend Environment**
  - [ ] Initialize a new Next.js application in the `frontend` directory.
  - [ ] Install necessary packages: `tailwindcss`, `axios` (or use fetch), and a state management library (e.g., `zustand`).

- [ ] **Task 2.2: Authentication UI**
  - [ ] Create the folder structure for `(auth)` routes.
  - [ ] Build the signup form at `frontend/src/app/(auth)/signup/page.tsx`.
  - [ ] Build the login form at `frontend/src/app/(auth)/login/page.tsx`.
  - [ ] Create `frontend/src/hooks/useAuth.ts` for managing auth state (token, user info).

- [ ] **Task 2.3: API Client**
  - [ ] Create `frontend/src/lib/api.ts` to configure an Axios instance or wrapper around `fetch` for making requests to the backend, including setting the `Authorization` header with the JWT token.

- [ ] **Task 2.4: Chat Interface**
  - [ ] Create the main dashboard page at `frontend/src/app/(main)/dashboard/page.tsx`.
  - [ ] Implement a basic chat UI using a component library or custom components (`MessageList`, `MessageInput`).
  - [ ] Fetch and display the user's current tasks on load.

- [ ] **Task 2.5: Frontend-Backend Integration**
  - [ ] Wire up the login and signup forms to the backend API endpoints.
  - [ ] On successful login, store the JWT token and redirect to the dashboard.
  - [ ] Wire up the chat input to the `/api/chat` backend endpoint.
  - [ ] When the chatbot sends back an updated task list, refresh the UI.
