# Agentic Architecture Specification: Todo-App

## 1. Overview of Agentic Architecture

This document defines the architecture of a multi-agent system designed for the spec-driven development of a Full-Stack Todo Web Application. The system is built for a hackathon environment, emphasizing clear separation of concerns, professional structure, and adherence to Spec-Kit Plus and Claude Code style workflows.

The architecture consists of a primary `Orchestrator Agent` that manages a team of specialized `Sub-Agents`. Each Sub-Agent has a distinct domain of responsibility (e.g., frontend, backend, database). Agents utilize a shared `Skills Registry` to perform tasks, ensuring that capabilities are reusable and well-defined. The entire system is designed to take a high-level feature specification as input and produce a detailed implementation plan, ready for code generation in a later phase.

---

## 2. Primary Orchestrator Agent

- **Role:** Central Coordinator and Project Manager.
- **Responsibilities:**
    - Acts as the primary interface for receiving high-level feature specifications.
    - Decomposes specifications into actionable tasks for Sub-Agents.
    - Manages the end-to-end workflow, delegating tasks and coordinating communication between agents.
    - Consolidates outputs from Sub-Agents into a unified, compliant implementation plan.
    - Ensures all agent activities align with the project's architectural principles and specifications.
- **Skills:**
    - `agent_coordination`
    - `task_decomposition`
    - `spec_compliance_validation`
- **Input:** High-level feature specification (`spec.md`).
- **Output:** A consolidated implementation plan (`plan.md`) and a set of structured tasks for development agents (`tasks.md`).

---

## 3. Sub-Agents (Specialized)

### A. Spec Analyst Agent
- **Role:** Requirements and Specification Expert.
- **Responsibilities:**
    - Parses and analyzes incoming feature specifications for clarity, completeness, and feasibility.
    - Translates natural language requirements into a structured, machine-readable format.
    - Validates that the proposed work does not violate existing system constraints or architectural principles.
- **Skills:**
    - `spec_analysis`
    - `spec_compliance_validation`
- **Input:** Raw feature specification text.
- **Output:** Structured and validated list of requirements and constraints.

### B. Backend Agent
- **Role:** FastAPI and Business Logic Specialist.
- **Responsibilities:**
    - Designs RESTful API endpoints based on feature requirements.
    - Defines data structures and object-relational mapping (ORM) models using SQLModel.
    - Creates API contracts, including request/response schemas and status codes.
- **Skills:**
    - `fastapi_api_design`
    - `sqlmodel_orm`
    - `error_handling_strategy`
- **Input:** Backend-specific tasks from the Orchestrator.
- **Output:** API specification documents and database model definitions.

### C. Frontend Agent
- **Role:** Next.js and User Interface Specialist.
- **Responsibilities:**
    - Designs the component hierarchy and state management strategy for the Next.js App Router.
    - Defines the user authentication flow and integrates it using the Better Auth library.
    - Maps UI/UX requirements to a concrete frontend architecture.
- **Skills:**
    - `nextjs_app_router`
    - `better_auth_integration`
- **Input:** Frontend-specific tasks from the Orchestrator.
- **Output:** Frontend architectural plan, including component trees, state management design, and auth flow diagrams.

### D. Database Agent
- **Role:** Neon Serverless PostgreSQL Specialist.
- **Responsibilities:**
    - Designs the physical database schema based on the Backend Agent's ORM definitions.
    - Develops strategies for schema migrations, indexing, and performance tuning specific to a serverless environment.
    - Ensures data integrity and defines constraints at the database level.
- **Skills:**
    - `postgres_schema_design`
    - `neon_serverless_optimization`
- **Input:** Logical data model from the Backend Agent.
- **Output:** Database schema (DDL), migration scripts, and optimization notes.

### E. Security & Authentication Agent
- **Role:** Security, Authentication, and Authorization Specialist.
- **Responsibilities:**
    - Defines the JWT structure, signing process, and validation logic.
    - Designs and enforces API security measures to prevent common vulnerabilities (e.g., SQLi, XSS).
    - Implements data access policies to ensure strict user isolation (multi-tenancy).
- **Skills:**
    - `jwt_token_validation`
    - `api_security_enforcement`
    - `user_isolation_enforcement`
- **Input:** Security requirements and API design from other agents.
- **Output:** Security and authentication strategy document, including JWT specifications and data access rules.

---

## 4. Skills Registry

| Skill Name                   | Description                                                                                                    | Used By Agent(s)                                    |
| ---------------------------- | -------------------------------------------------------------------------------------------------------------- | --------------------------------------------------- |
| `spec_analysis`              | Ability to parse, interpret, and structure requirements from a natural language specification document.        | `Spec Analyst`                                      |
| `task_decomposition`         | Ability to break down large, high-level goals into smaller, sequential, and parallelizable tasks for agents.   | `Orchestrator`                                      |
| `agent_coordination`         | Ability to manage workflows, delegate tasks, and handle communication and data flow between multiple agents.   | `Orchestrator`                                      |
| `fastapi_api_design`         | Skill to design clean, RESTful API endpoints, including routes, request/response models, and HTTP status codes.  | `Backend`                                           |
| `sqlmodel_orm`               | Skill to define database tables and relationships as Python objects using the SQLModel library.                | `Backend`                                           |
| `postgres_schema_design`     | Skill to design efficient and normalized relational database schemas for PostgreSQL.                           | `Database`                                          |
| `neon_serverless_optimization`| Knowledge of optimizing PostgreSQL for a serverless environment like Neon, focusing on cold starts and scaling.  | `Database`                                          |
| `nextjs_app_router`          | Skill to architect a frontend application using the Next.js App Router, including layouts, pages, and components.| `Frontend`                                          |
| `better_auth_integration`    | Skill to integrate the Better Auth library for handling frontend authentication flows and session management.    | `Frontend`                                          |
| `jwt_token_validation`       | Ability to create and validate JSON Web Tokens (JWTs) for stateless, secure authentication.                      | `Security & Auth`                                   |
| `api_security_enforcement`   | Skill to apply security best practices to API design, including input validation and rate limiting.              | `Security & Auth`                                   |
| `user_isolation_enforcement` | Skill to design database queries and business logic that strictly separates one user's data from another's.      | `Security & Auth`                                   |
| `error_handling_strategy`    | Ability to define a consistent, system-wide strategy for handling and reporting errors across application layers.| `Backend`                                           |
| `spec_compliance_validation` | Ability to check if the generated plans and artifacts conform to the original input specification.               | `Orchestrator`, `Spec Analyst`                        |

---

## 5. Agent-to-Skill Mapping

- **Orchestrator Agent:**
  - `agent_coordination`
  - `task_decomposition`
  - `spec_compliance_validation`
- **Spec Analyst Agent:**
  - `spec_analysis`
  - `spec_compliance_validation`
- **Backend Agent:**
  - `fastapi_api_design`
  - `sqlmodel_orm`
  - `error_handling_strategy`
- **Frontend Agent:**
  - `nextjs_app_router`
  - `better_auth_integration`
- **Database Agent:**
  - `postgres_schema_design`
  - `neon_serverless_optimization`
- **Security & Auth Agent:**
  - `jwt_token_validation`
  - `api_security_enforcement`
  - `user_isolation_enforcement`

---

## 6. Execution Workflow

1.  **Specification Input:** The `Orchestrator Agent` receives a high-level feature specification.
2.  **Analysis & Validation:** The `Orchestrator` passes the spec to the `Spec Analyst Agent`, which validates it and breaks it down into structured requirements.
3.  **Task Decomposition & Delegation:** The `Orchestrator` uses its `task_decomposition` skill to create a work plan. It then delegates tasks to the specialized `Backend`, `Frontend`, `Database`, and `Security & Auth` agents based on their roles.
4.  **Specialized Design:** Each Sub-Agent executes its assigned design tasks in parallel:
    - `Backend Agent` designs API endpoints and logical data models.
    - `Frontend Agent` designs the UI component structure and auth flow.
    - The `Backend Agent` sends its data model to the `Database Agent`, which designs the physical schema and optimizations.
    - The `Security & Auth Agent` reviews the API and auth flow designs to create a security strategy.
5.  **Consolidation:** Sub-Agents report their completed designs (API contracts, schema DDLs, component trees, security rules) back to the `Orchestrator`.
6.  **Compliance Review:** The `Orchestrator` performs a final `spec_compliance_validation` check to ensure the consolidated plan meets all original requirements.
7.  **Output Generation:** The `Orchestrator` produces the final `plan.md` and `tasks.md` files, which will guide the implementation phase.

---

## 7. Folder Structure for Agent Specs

This structure is compatible with Spec-Kit Plus and ensures each agent's specification is maintained in a clean, organized manner.

```
/specs
└── /agents
    ├── agentic-architecture.md   <-- This file
    ├── orchestrator.agent.md     <-- Detailed spec for the Orchestrator Agent
    ├── spec-analyst.agent.md     <-- Detailed spec for the Spec Analyst Agent
    ├── backend.agent.md          <-- Detailed spec for the Backend Agent
    ├── frontend.agent.md         <-- Detailed spec for the Frontend Agent
    ├── database.agent.md         <-- Detailed spec for the Database Agent
    └── security-auth.agent.md    <-- Detailed spec for the Security Agent
```
