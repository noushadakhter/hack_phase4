# Actionable Tasks: Todo AI Chatbot (Phase III)

**Version:** 1.0.0
**Date:** 2026-01-22
**Status:** Pending

---

## Phase 1: Backend Foundation

-   [ ] **Task 1.1:** Create `backend` directory.
-   [ ] **Task 1.2:** Create `backend/requirements.txt` with the following content:
    ```
    fastapi
    uvicorn[standard]
    sqlmodel
    psycopg2-binary
    python-dotenv
    fastapi-better-auth
    openai
    passlib[bcrypt]
    python-jose[cryptography]
    ```
-   [ ] **Task 1.3:** Create the initial file structure: `main.py`, `auth.py`, `chat.py`, `agent.py`, `mcp_server.py`, `db.py`, `models.py`, `schemas.py`.
-   [ ] **Task 1.4:** Create `backend/.env` file with placeholder content.
-   [ ] **Task 1.5:** Implement database connection logic in `db.py`.
-   [ ] **Task 1.6:** Implement all SQLModel classes in `models.py` as per the spec.
-   [ ] **Task 1.7:** Add logic to `main.py` to create database tables on startup.
-   [ ] **Task 1.8:** Implement `POST /signup` and `POST /login` endpoints in `auth.py`.
-   [ ] **Task 1.9:** Configure the `BetterAuth` middleware in `main.py`.

## Phase 2: Backend Core Logic

-   [ ] **Task 2.1:** Implement the `create_todo` MCP tool in `mcp_server.py`.
-   [ ] **Task 2.2:** Implement the `list_todos` MCP tool in `mcp_server.py`.
-   [ ] **Task 2.3:** Implement the `update_todo` MCP tool in `mcp_server.py`.
-   [ ] **Task 2.4:** Implement the `mark_complete` MCP tool in `mcp_server.py`.
-   [ ] **Task 2.5:** Implement the `delete_todo` MCP tool in `mcp_server.py`.
-   [ ] **Task 2.6:** Define the AI agent in `agent.py`, including its system prompt and tools.
-   [ ] **Task 2.7:** Implement the `ChatMessage` and `ChatResponse` Pydantic schemas in `schemas.py`.
-   [ ] **Task 2.8:** Implement the `POST /chat` endpoint logic in `chat.py`.
-   [ ] **Task 2.9:** Add the chat router to `main.py` and protect it with auth.
-   [ ] **Task 2.10:** Configure CORS middleware in `main.py`.

## Phase 3: Frontend Foundation

-   [ ] **Task 3.1:** Create the `frontend` Next.js project.
-   [ ] **Task 3.2:** Install npm dependencies: `tailwindcss`, `axios`, `zustand`.
-   [ ] **Task 3.3:** Initialize Tailwind CSS.
-   [ ] **Task 3.4:** Create the frontend folder structure (`/app`, `/components`, `/lib`, `/hooks`).
-   [ ] **Task 3.5:** Create `frontend/.env.local` with `NEXT_PUBLIC_API_URL`.
-   [ ] **Task 3.6:** Set up a basic `src/lib/api.ts` file for axios instance configuration.

## Phase 4: Frontend Authentication

-   [ ] **Task 4.1:** Create a Zustand store in `src/lib/auth.ts` for managing auth state.
-   [ ] **Task 4.2:** Implement the `LoginForm` component in `src/components/auth/LoginForm.tsx`.
-   [ ] **Task 4.3:** Implement the `SignupForm` component in `src/components/auth/SignupForm.tsx`.
-   [ ] **Task 4.4:** Create the pages `app/(auth)/login/page.tsx` and `app/(auth)/signup/page.tsx`.
-   [ ] **Task 4.5:** Implement a `ProtectedRoute` component or layout that redirects unauthenticated users.

## Phase 5: Frontend Chat

-   [ ] **Task 5.1:** Implement the `MessageBubble` component.
-   [ ] **Task 5.2:** Implement the `ChatInput` component.
-   [ ] **Task 5.3:** Implement the `ChatWindow` component.
-   [ ] **Task 5.4:** Create the `useChat` hook in `src/hooks/useChat.ts` to manage all chat logic.
-   [ ] **Task 5.5:** Assemble the components on the main chat page `app/(main)/page.tsx` and integrate the `useChat` hook.

## Phase 6: Finalization

-   [ ] **Task 6.1:** Create `.env.example` files for both frontend and backend.
-   [ ] **Task 6.2:** Perform a full end-to-end test of the application flow.
-   [ ] **Task 6.3:** Write a `README.md` with setup and run instructions.
