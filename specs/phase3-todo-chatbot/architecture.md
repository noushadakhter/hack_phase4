# Phase III: Todo AI Chatbot - Architecture Diagram (Conceptual)

```mermaid
graph TD
    A[User] -->|Interacts with| B(ChatKit UI)
    B -->|POST /api/{user_id}/chat| C(FastAPI Backend)

    subgraph FastAPI Backend
        C --1. Request Received--> D{API Endpoint}
        D --2. Fetch Conversation History--> E(Neon PostgreSQL)
        D --3. Append New Message--> F[Conversation History]
        D --4. Save User Message--> E
        D --5. Run Agent with MCP Tools--> G(OpenAI Agent Runner)
    end

    subgraph OpenAI Agent Runner
        G --> H[IntentClassifier]
        G --> I[ToolSelector]
        G --> J[ToolExecutor]
        G --> K[ResponseFormatter]
        J --> L(MCP Server)
    end

    subgraph MCP Server (Tools)
        L --> M[add_task]
        L --> N[list_tasks]
        L --> O[complete_task]
        L --> P[delete_task]
        L --> Q[update_task]
        M,N,O,P,Q --> E
    end

    G --> R[Agent Response]
    R --6. Capture Tool Calls--> D
    R --7. Save Assistant Message--> E
    D --8. Return Response--> B
    E -- Database Storage --> E
    subgraph Authentication
        Auth[Better Auth] -- Protects --> D
        Auth -- Associates --> D
    end
```

### Component Breakdown:

1.  **User**: End-user interacting with the Todo AI Chatbot.
2.  **ChatKit UI**:
    *   Frontend interface built with OpenAI ChatKit.
    *   Handles user input, displays chat history, loading states, and error messages.
    *   Communicates with the FastAPI Backend.
3.  **FastAPI Backend**:
    *   Stateless Python backend using FastAPI.
    *   Receives chat requests via `POST /api/{user_id}/chat`.
    *   Manages the flow of conversation:
        *   Fetches conversation history from `Neon PostgreSQL`.
        *   Appends new user messages.
        *   Saves user messages.
        *   Invokes the `OpenAI Agent Runner`.
        *   Captures tool calls from the agent.
        *   Saves assistant responses and tool calls.
        *   Returns structured responses to the `ChatKit UI`.
    *   Protected by `Better Auth` to associate requests with authenticated users.
4.  **OpenAI Agent Runner**:
    *   Utilizes OpenAI Agents SDK for natural language understanding, reasoning, and tool selection.
    *   **Internal Roles**:
        *   `IntentClassifier`: Determines the user's intent (e.g., add task, list tasks).
        *   `ToolSelector`: Chooses the appropriate MCP tool based on the classified intent.
        *   `ToolExecutor`: Executes the selected MCP tool by making calls to the `MCP Server`.
        *   `ResponseFormatter`: Formats the agent's response, potentially incorporating results from tool execution.
5.  **MCP Server (Tools)**:
    *   Implemented using the Official MCP SDK.
    *   Exposes a set of tools for task management: `add_task`, `list_tasks`, `complete_task`, `delete_task`, `update_task`.
    *   Each tool interacts with the `Neon PostgreSQL` database to perform CRUD operations on `Task` objects.
6.  **Neon PostgreSQL**:
    *   Serverless PostgreSQL database.
    *   Stores `Task`, `Conversation`, and `Message` models.
    *   Provides persistent storage for all application data, enabling the backend to remain stateless.
7.  **Better Auth**:
    *   Authentication mechanism for securing the FastAPI chat endpoint.
    *   Ensures that only authenticated users can access the chat functionality.
    *   Associates the `user_id` from the authentication system with the API requests.
```