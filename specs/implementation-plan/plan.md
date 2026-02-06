# Implementation Plan: Todo AI Chatbot (Phase III)

**Version:** 1.0.0
**Date:** 2026-01-22
**Status:** Draft

---

## 1. Overview

This document outlines the step-by-step implementation plan to build the Phase III Todo AI Chatbot. The plan is divided into logical phases, starting with backend development, followed by the frontend, ensuring that dependencies are built in the correct order. This plan will be used to generate specific, actionable tasks.

---

## Phase 1: Backend Foundation Setup

*Goal: Establish the core FastAPI application, database connection, and user models.*

1.  **Project Scaffolding:**
    *   Create the `backend` directory.
    *   Initialize a Python virtual environment.
    *   Create the folder structure as defined in the backend spec (`auth.py`, `main.py`, `db.py`, `models.py`, etc.).
    *   Create `requirements.txt` with all necessary dependencies (`fastapi`, `uvicorn`, `sqlmodel`, `psycopg2-binary`, `python-dotenv`, `fastapi-better-auth`, `openai`).

2.  **Environment Setup:**
    *   Create the `.env` file with placeholders for `DATABASE_URL`, `JWT_SECRET_KEY`, and `OPENAI_API_KEY`.

3.  **Database and Model Implementation:**
    *   Implement the database engine and session management in `db.py`.
    *   Implement all SQLModel classes (`User`, `TodoItem`, `Conversation`, `Message`) in `models.py` exactly as specified.
    *   Modify `main.py` to create all database tables on startup.

4.  **Basic Authentication:**
    *   Implement the `POST /signup` and `POST /login` endpoints in `auth.py`.
    *   Configure `fastapi-better-auth` in `main.py`.
    *   Ensure password hashing is correctly implemented for user creation.

---

## Phase 2: Backend Core Logic

*Goal: Implement the AI agent, its tools, and the main conversational endpoint.*

1.  **MCP Tool Implementation:**
    *   In `mcp_server.py`, implement all the specified MCP tool functions (`create_todo`, `list_todos`, `update_todo`, `mark_complete`, `delete_todo`).
    *   Each function must take `user_id` as the first parameter and strictly enforce data ownership by querying against that ID.

2.  **AI Agent Definition:**
    *   In `agent.py`, define the OpenAI Agent.
    *   Provide the agent with the system prompt and the list of available MCP tools from `mcp_server.py`.

3.  **Chat Endpoint Implementation:**
    *   In `chat.py`, implement the `POST /chat` endpoint.
    *   This endpoint must be protected by JWT authentication.
    *   Implement the logic to:
        *   Load or create a conversation.
        *   Fetch message history from the database.
        *   Invoke the AI agent with the history and new message.
        *   Persist the new user message and the agent's response to the database.
        *   Return the agent's response to the client.

4.  **CORS and Middleware:**
    *   In `main.py`, configure CORS middleware to allow requests from the frontend's URL.

---

## Phase 3: Frontend Foundation Setup

*Goal: Establish the Next.js application and create basic UI components.*

1.  **Project Scaffolding:**
    *   Use `npx create-next-app@latest` to create the `frontend` directory.
    *   Install necessary dependencies: `tailwindcss`, `axios` (or use `fetch`), `zustand` (or `useContext`).
    *   Initialize Tailwind CSS and configure `tailwind.config.js`.
    *   Create the folder structure as defined in the frontend spec (`/app`, `/components`, `/lib`, etc.).

2.  **Environment Setup:**
    *   Create the `.env.local` file with the `NEXT_PUBLIC_API_URL` variable.

3.  **Basic UI Components:**
    *   Create basic, non-interactive UI components in `src/components/ui` (e.g., `Button`, `Input`, `Card`). Using `shadcn/ui` `init` and `add` commands is recommended here.

---

## Phase 4: Frontend Authentication

*Goal: Build the login/signup pages and establish global auth state.*

1.  **Auth Components:**
    *   Implement the `LoginForm` and `SignupForm` components. They will handle user input and call the backend API.

2.  **Auth Pages:**
    *   Create the `/login` and `/signup` pages using the components from the previous step.

3.  **Auth State Management:**
    *   Create an authentication context (`AuthContext`) or a Zustand store to manage the user's session (JWT and user info).
    *   This store will provide `login`, `logout`, and `isAuthenticated` status.
    *   Implement logic to securely store and retrieve the JWT.

4.  **Protected Routes:**
    *   Implement a wrapper or logic in the main layout (`app/(main)/layout.tsx`) that checks for authentication status and redirects to `/login` if the user is not authenticated.

---

## Phase 5: Frontend Chat Implementation

*Goal: Build the conversational interface and connect it to the backend.*

1.  **Chat UI Components:**
    *   Implement the `ChatWindow`, `MessageBubble`, and `ChatInput` components as specified.

2.  **Chat State Management (`useChat` hook):**
    *   Create the `useChat` custom hook to manage the lifecycle of a conversation.
    *   This hook will handle:
        *   Fetching/sending messages to the `/chat` endpoint.
        -   Managing the array of messages.
        *   Storing the current `conversation_id`.
        *   Tracking the loading state.

3.  **Main Chat Page:**
    *   Assemble the chat components on the main page (`/`).
    *   Use the `useChat` hook to power the interface.
    *   Ensure the UI correctly displays user messages, assistant responses, and loading indicators.

---

## Phase 6: Finalization and Review

*Goal: Ensure the application is stable, documented, and ready to run.*

1.  **Code Cleanup:** Review both frontend and backend code for clarity, consistency, and adherence to specs.
2.  **Environment Finalization:** Ensure all `.env` and `.env.local` files are correctly configured and documented in a `.env.example` file.
3.  **Testing:** Perform manual end-to-end testing of the full user flow: signup -> login -> chat -> create todo -> list todos -> logout.
4.  **Final Review:** One final check of all deliverables against the original prompt.
