# Feature Specification: Frontend Todo Application UI/UX

**Feature Branch**: `1-frontend-todo-spec`  
**Created**: 2026-01-12  
**Status**: Draft  
**Governed By**: `@specs/constitution/sp-constitution.md`

## 1. Page Specs

### 1.1. Login / Signup Page (`/auth`)
- **Purpose**: Allows new users to register and existing users to sign in.
- **Layout**: Centered form layout.
- **Components Used**:
    - `AuthForm`
    - `Button`
    - `Input`
    - `Notification` (for errors)
- **Props**: None.
- **State**: `email`, `password`, `isLoginMode`, `isLoading`, `error`.

### 1.2. Dashboard Page (`/`)
- **Purpose**: Displays the list of the authenticated user's tasks. Main view after login.
- **Layout**: Main content area with a header.
- **Components Used**:
    - `Navbar`
    - `TaskList`
    - `TaskCard`
    - `TaskFilterControls`
    - `Button` (for "Create New Task")
    - `LoadingSpinner`
- **Props**: None.
- **State**: `tasks`, `filter`, `isLoading`, `error`.

### 1.3. Create Task Page (`/tasks/new`)
- **Purpose**: Provides a form for the user to create a new task.
- **Layout**: Main content area with a header.
- **Components Used**:
    - `Navbar`
    - `TaskForm`
    - `Button`
    - `Input`
    - `Notification`
- **Props**: None.
- **State**: `title`, `description`, `isLoading`, `error`.

### 1.4. Task Detail / Edit Page (`/tasks/[taskId]/edit`)
- **Purpose**: Allows a user to view the full details of a task and edit it.
- **Layout**: Main content area with a header.
- **Components Used**:
    - `Navbar`
    - `TaskForm`
    - `Button`
    - `Input`
    - `Notification`
- **Props**: `taskId` (from URL).
- **State**: `taskData`, `isLoading`, `error`.

### 1.5. Profile / Settings Page (`/profile`)
- **Purpose**: Allows the user to view their profile information and manage settings.
- **Layout**: Main content area with a header.
- **Components Used**:
    - `Navbar`
    - `ProfileForm`
    - `Button`
    - `Input`
- **Props**: None.
- **State**: `userData`, `isLoading`, `error`.

---

## 2. Component Specs

### 2.1. `TaskCard`
- **Props**: `task: { id, title, status, createdDate }`
- **State**: None.
- **Event Handlers**:
    - `onToggleComplete`: Fires when the completion checkbox is clicked.
    - `onClick`: Navigates to the Task Detail page.
- **API Interactions**: Calls `api.ts` `updateTaskStatus()` on toggle.
- **Styling**: Card layout with clean spacing, border, and hover effects. Background color may change based on `status`.

### 2.2. `Navbar`
- **Props**: None.
- **State**: `isMobileMenuOpen`.
- **Event Handlers**:
    - `onLogout`: Fires when the logout button is clicked.
- **API Interactions**: Calls `api.ts` `logoutUser()`.
- **Styling**: Sticky or fixed header, contains app logo, navigation links (Dashboard, Profile), and Logout button.

### 2.3. `AuthForm`
- **Props**: `isLoginMode: boolean`.
- **State**: `email`, `password`, `error`.
- **Event Handlers**:
    - `onSubmit`: Handles form submission.
    - `onToggleMode`: Switches between Login and Signup views.
- **API Interactions**: Calls `api.ts` `loginUser()` or `signupUser()`.
- **Styling**: Standard form layout with labels, inputs, and a submit button. Displays validation errors.

### 2.4. `TaskForm`
- **Props**: `initialData?: { title, description }`.
- **State**: `title`, `description`, `validationError`.
- **Event Handlers**:
    - `onSubmit`: Handles form submission for creating or updating a task.
- **API Interactions**: Calls `api.ts` `createTask()` or `updateTask()`.
- **Styling**: Form layout for creating/editing tasks. Includes input fields for title and description.

### 2.5. `Notification`
- **Props**: `message: string`, `type: 'success' | 'error'`.
- **State**: `isVisible`.
- **Event Handlers**: `onClose`.
- **API Interactions**: None.
- **Styling**: Toast-style component, typically fixed to a corner of the screen. Colors change based on `type`.

---

## 3. Folder / File Structure

```
/frontend
  └── src
      ├── app/
      │   ├── (auth)
      │   │   └── auth/page.tsx       # Login / Signup Page
      │   ├── (main)
      │   │   ├── layout.tsx
      │   │   ├── page.tsx            # Dashboard Page
      │   │   ├── profile/page.tsx    # Profile Page
      │   │   └── tasks
      │   │       ├── new/page.tsx    # Create Task Page
      │   │       └── [taskId]
      │   │           └── edit/page.tsx # Edit Task Page
      │   └── layout.tsx                # Root Layout
      ├── components/
      │   ├── ui/
      │   │   ├── Button.tsx
      │   │   ├── Input.tsx
      │   │   └── LoadingSpinner.tsx
      │   ├── auth/
      │   │   └── AuthForm.tsx
      │   ├── tasks/
      │   │   ├── TaskCard.tsx
      │   │   ├── TaskList.tsx
      │   │   ├── TaskForm.tsx
      │   │   └── TaskFilterControls.tsx
      │   └── common/
      │       ├── Navbar.tsx
      │       └── Notification.tsx
      └── lib/
          └── api.ts                    # Central API client
```

---

## 4. UX Notes

- **Interactions**: All interactive elements (buttons, links) must have clear hover and focus states. UI feedback (loading spinners, notifications) is critical for all asynchronous actions.
- **Responsiveness**: The application must be mobile-first. Components and layouts should adapt seamlessly from small mobile screens to large desktop monitors. Use flexible grids and media queries.
- **Error Handling**: User-facing error messages should be clear and concise. For example, instead of "API Error 500", show "Could not save your task. Please try again later."
- **Accessibility**: All forms should use proper `label` elements. Interactive elements must be keyboard-navigable. Use ARIA attributes where necessary to provide context to screen readers.
- **API States**: Every component that fetches data must gracefully handle three states:
    1.  **Loading**: A loading indicator (e.g., `LoadingSpinner` or skeleton screen) should be displayed.
    2.  **Success**: The data is displayed as intended.
    3.  **Error**: A user-friendly error message is shown, ideally with an option to retry.

---

## 5. API Integration Contract

- A central `api.ts` client will manage all `fetch` requests.
- Every authenticated request MUST include the JWT token in the `Authorization` header: `Authorization: Bearer <token>`.
- The client will handle token acquisition (from local storage or state management) and renewal.
- Functions in `api.ts` will correspond to backend endpoints (e.g., `getTasks()`, `createTask(data)`, `updateTask(id, data)`).
- The client is responsible for standardizing error shapes from the backend.
