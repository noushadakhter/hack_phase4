# MCP Tools Specification

This document defines the function signatures, parameters, and return values for the stateless MCP tools that the AI Agent will use to interact with the system's data.

---

### 1. `add_task`

- **Description:** Creates a new to-do task for a specified user.
- **Signature:** `add_task(user_id: int, title: str, description: Optional[str] = None) -> dict`
- **Parameters:**
  - `user_id` (int, required): The ID of the user for whom the task is being created.
  - `title` (str, required): The title or main content of the task.
  - `description` (str, optional): An optional, more detailed description of the task.
- **Returns:** A dictionary representing the newly created task object.
  - **Example:** `{"id": 101, "title": "Buy milk", "description": "Get 2% milk", "completed": false}`

---

### 2. `list_tasks`

- **Description:** Retrieves a list of to-do tasks for a specified user, with an optional status filter.
- **Signature:** `list_tasks(user_id: int, status: str = "all") -> List[dict]`
- **Parameters:**
  - `user_id` (int, required): The ID of the user whose tasks are to be retrieved.
  - `status` (str, optional): The filter for the task status.
    - **Allowed Values:** `"all"`, `"pending"`, `"completed"`
    - **Default:** `"all"`
- **Returns:** A list of dictionaries, where each dictionary is a task object.
  - **Example:** `[{"id": 101, "title": "Buy milk", ...}, {"id": 102, "title": "Walk the dog", ...}]`

---

### 3. `complete_task`

- **Description:** Marks an existing task as completed.
- **Signature:** `complete_task(user_id: int, task_id: int) -> dict`
- **Parameters:**
  - `user_id` (int, required): The ID of the user who owns the task. This is used to ensure a user cannot complete another user's task.
  - `task_id` (int, required): The ID of the task to be marked as complete.
- **Returns:** A dictionary representing the updated task object.
  - **Example:** `{"id": 101, "title": "Buy milk", ..., "completed": true}`
- **Raises:** `TaskNotFoundError` if a task with the given `task_id` does not exist or does not belong to the `user_id`.

---

### 4. `update_task`

- **Description:** Updates the title and/or description of an existing task.
- **Signature:** `update_task(user_id: int, task_id: int, title: Optional[str] = None, description: Optional[str] = None) -> dict`
- **Parameters:**
  - `user_id` (int, required): The ID of the user who owns the task.
  - `task_id` (int, required): The ID of the task to be updated.
  - `title` (str, optional): The new title for the task.
  - `description` (str, optional): The new description for the task.
- **Returns:** A dictionary representing the updated task object.
- **Raises:** `TaskNotFoundError` if a task with the given `task_id` does not exist or does not belong to the `user_id`.

---

### 5. `delete_task`

- **Description:** Deletes an existing task.
- **Signature:** `delete_task(user_id: int, task_id: int) -> dict`
- **Parameters:**
  - `user_id` (int, required): The ID of the user who owns the task.
  - `task_id` (int, required): The ID of the task to be deleted.
- **Returns:** A confirmation dictionary.
  - **Example:** `{"success": true, "deleted_task_id": 101}`
- **Raises:** `TaskNotFoundError` if a task with the given `task_id` does not exist or does not belong to the `user_id`.
