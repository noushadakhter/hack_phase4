# Frontend Specification: Todo AI Chatbot (Phase III)

**Version:** 1.0.0
**Date:** 2026-01-22
**Status:** Draft

---

## 1. Overview

This document specifies the frontend architecture for the Phase III Todo AI Chatbot. The frontend will be a modern, responsive, single-page application built with Next.js (App Router). It will provide user authentication interfaces and a conversational chat UI for interacting with the AI backend.

## 2. Core Technologies

- **Framework:** Next.js 15+ (App Router)
- **Language:** TypeScript
- **Styling:** Tailwind CSS
- **UI Components:** Shadcn/UI (recommended for accessible, modern components)
- **Chat Interface:** Custom components, potentially leveraging a headless library like `react-chat-hooks`.

## 3. Architecture & Data Flow

The frontend is a pure client of the backend API. It maintains no business logic and is responsible only for presentation and user interaction.

1.  **Authentication:** The app protects chat routes. Unauthenticated users are redirected to `/login`. JWT tokens received from the backend are stored securely (e.g., in an HttpOnly cookie or secure local storage wrapper).
2.  **API Communication:** All API calls to the backend include the `Authorization: Bearer <JWT>` header. A centralized API client (e.g., using `fetch` or `axios`) will manage this.
3.  **State Management:** Client-side state (e.g., current messages, loading status, user info) will be managed using React hooks (`useState`, `useContext`, `useReducer`) or a lightweight state management library like Zustand.
4.  **Real-time Feel:** While the interaction is request-response, the UI will implement loading indicators and optimistic updates where appropriate to feel responsive.

## 4. Folder Structure (Proposed)

```
frontend/
├── src/
│   ├── app/
│   │   ├── (auth)/         # Group for auth pages
│   │   │   ├── login/
│   │   │   │   └── page.tsx
│   │   │   └── signup/
│   │   │       └── page.tsx
│   │   ├── (main)/         # Group for protected main app
│   │   │   ├── layout.tsx  # Layout containing navbar, etc.
│   │   │   └── page.tsx    # Main chat interface page
│   │   ├── layout.tsx      # Root layout
│   │   └── globals.css
│   ├── components/
│   │   ├── auth/
│   │   │   ├── LoginForm.tsx
│   │   │   └── SignupForm.tsx
│   │   ├── chat/
│   │   │   ├── ChatWindow.tsx
│   │   │   ├── MessageBubble.tsx
│   │   │   └── ChatInput.tsx
│   │   └── ui/             # Reusable UI components (from Shadcn/UI)
│   │       ├── Button.tsx
│   │       ├── Input.tsx
│   │       └── Card.tsx
│   ├── lib/
│   │   ├── auth.ts         # Auth hooks, token management
│   │   ├── api.ts          # Centralized API client
│   │   └── types.ts        # TypeScript types for API objects
│   └── hooks/
│       └── useChat.ts      # Custom hook to manage chat state & logic
├── .env.local
├── tailwind.config.js
├── postcss.config.js
└── tsconfig.json
```

## 5. Routing (Next.js App Router)

- **`/` (root):** The main chat page. This route is protected. If the user is not authenticated, they are redirected to `/login`.
- **`/login`:** Public page containing the `LoginForm` component. On successful login, the user is redirected to `/`.
- **`/signup`:** Public page containing the `SignupForm` component. On successful signup, the user is redirected to `/login`.

## 6. Component Breakdown

### Auth Components (`src/components/auth/`)

- **`LoginForm.tsx`:** A client component with email/password fields. Handles form state, validation, and submission to the `/login` API endpoint.
- **`SignupForm.tsx`:** A client component with email/password fields. Handles form state, validation, and submission to the `/signup` API endpoint.

### Chat Components (`src/components/chat/`)

- **`ChatWindow.tsx`:** The main container for the conversation. It will map over the list of messages and render `MessageBubble` for each. It will also show a typing indicator when a response is pending.
- **`MessageBubble.tsx`:** A simple component to display a single message. It will have different styling based on the message `role` ("user" or "assistant").
- **`ChatInput.tsx`:** A form with a text input and a submit button. It will be disabled while the assistant is "typing".

### Main Pages (`src/app/`)

- **`app/(main)/page.tsx`:** The core chat application page. It will use a custom hook (`useChat`) to manage the conversation state and orchestrate the child chat components.
- **`app/(auth)/login/page.tsx` & `app/(auth)/signup/page.tsx`:** Pages for hosting the respective auth forms.

## 7. State Management

- **Auth State:** A global context (`AuthContext`) will provide user information and authentication status (`isAuthenticated`) to the entire application. This context will also contain `login` and `logout` functions.
- **Chat State:** The `useChat` custom hook will manage the chat logic on the main page. It will handle:
  - The array of messages.
  - The current `conversation_id`.
  - The loading/typing status.
  - A function to send a new message to the backend.

## 8. UI/UX Considerations

- **Responsive Design:** The layout must work seamlessly on both desktop and mobile devices. The chat interface should be full-height and the input should be accessible.
- **Loading States:** A clear loading indicator (e.g., a "typing" bubble) must be displayed while waiting for the assistant's response. Buttons should be disabled during API calls.
- **Error Handling:** API errors (e.g., network issues, server errors) should be gracefully handled and communicated to the user (e.g., via a toast notification).
- **Empty State:** The chat window should display a welcome message from the assistant before the user has sent any messages.

## 9. Environment Variables

File: `.env.local`

```
NEXT_PUBLIC_API_URL="http://127.0.0.1:8000"
```
