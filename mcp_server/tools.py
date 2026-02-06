from typing import Any, Optional, List
from fastmcp.tools.tool import Tool
from fastapi import Depends

from pydantic import BaseModel, Field
from sqlmodel import Session

# Assuming the backend's database and crud operations are accessible.
# In a real-world MCP setup, these might be exposed via an API or a shared library.
# For this exercise, we'll assume direct import for simplicity,
# but note that in a distributed MCP setup, this would be a client call.

# To make direct imports work, we need to ensure the backend directory is in the PYTHONPATH
# For this simulated environment, we'll assume it's handled or mock the session/crud.

# Placeholder for database session and CRUD operations
# In a real FastMCP server, you might inject these or use a client to the backend API.
# For now, we'll create a dummy session for tool definitions to pass Pydantic validation.
# The actual execution will need a proper session.

from backend.app.database import get_session # Import get_session from backend
from backend.app import crud
from backend.models import Task as DBTask, Role # Import DBTask to avoid conflict with ToolParam Task


class AddTaskParams(BaseModel):
    user_id: str = Field(description="The ID of the user creating the task.")
    title: str = Field(description="The title of the task.")
    description: Optional[str] = Field(default=None, description="A detailed description for the task.")

class TaskResult(BaseModel):
    task_id: int
    status: str
    title: str

async def add_task_tool(params: AddTaskParams, session: Any = Depends(get_session)) -> TaskResult:
    # In a real FastMCP server, the session would be managed by FastMCP's dependency injection.
    # Here, we pass it explicitly for clarity in this mock-up.
    task = crud.create_task(session=session, user_id=params.user_id, title=params.title, description=params.description)
    return TaskResult(task_id=task.id, status="created", title=task.title)

class ListTasksParams(BaseModel):
    user_id: str = Field(description="The ID of the user whose tasks are to be listed.")
    status: Optional[str] = Field(
        default="all",
        description="Filter tasks by status: 'all', 'pending', or 'completed'.",
        pattern="^(all|pending|completed)$"
    )

class ListedTask(BaseModel):
    id: int
    title: str
    completed: bool

class ListTasksResult(BaseModel):
    tasks: List[ListedTask]

async def list_tasks_tool(params: ListTasksParams, session: Any = Depends(get_session)) -> ListTasksResult:
    tasks = crud.get_tasks(session=session, user_id=params.user_id, status=params.status)
    return ListTasksResult(tasks=[ListedTask(id=t.id, title=t.title, completed=t.completed) for t in tasks])

class CompleteTaskParams(BaseModel):
    user_id: str = Field(description="The ID of the user who owns the task.")
    task_id: int = Field(description="The ID of the task to complete.")

async def complete_task_tool(params: CompleteTaskParams, session: Any = Depends(get_session)) -> TaskResult:
    task = crud.update_task(session=session, task_id=params.task_id, user_id=params.user_id, completed=True)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found or not owned by user.")
    return TaskResult(task_id=task.id, status="completed", title=task.title)

class DeleteTaskParams(BaseModel):
    user_id: str = Field(description="The ID of the user who owns the task.")
    task_id: int = Field(description="The ID of the task to delete.")

async def delete_task_tool(params: DeleteTaskParams, session: Any = Depends(get_session)) -> TaskResult:
    task = crud.delete_task(session=session, task_id=params.task_id, user_id=params.user_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found or not owned by user.")
    return TaskResult(task_id=task.id, status="deleted", title=task.title)

class UpdateTaskParams(BaseModel):
    user_id: str = Field(description="The ID of the user who owns the task.")
    task_id: int = Field(description="The ID of the task to update.")
    title: Optional[str] = Field(default=None, description="The new title for the task.")
    description: Optional[str] = Field(default=None, description="The new description for the task.")
    completed: Optional[bool] = Field(default=None, description="The new completion status for the task.")

async def update_task_tool(params: UpdateTaskParams, session: Any = Depends(get_session)) -> TaskResult:
    task = crud.update_task(session=session, task_id=params.task_id, user_id=params.user_id, title=params.title, description=params.description, completed=params.completed)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found or not owned by user.")
    return TaskResult(task_id=task.id, status="updated", title=task.title)

# Define the MCP Tools
add_task = Tool.from_function(
    add_task_tool,
    name="add_task",
    description="Adds a new todo task for a user.",
)

list_tasks = Tool.from_function(
    list_tasks_tool,
    name="list_tasks",
    description="Lists todo tasks for a user, optionally filtered by status.",
)

complete_task = Tool.from_function(
    complete_task_tool,
    name="complete_task",
    description="Marks a specific todo task as completed.",
)

delete_task = Tool.from_function(
    delete_task_tool,
    name="delete_task",
    description="Deletes a specific todo task.",
)

update_task = Tool.from_function(
    update_task_tool,
    name="update_task",
    description="Updates the title, description, or completion status of a specific todo task.",
)

# List of all tools to be exposed by the MCP Server
ALL_TOOLS = [add_task, list_tasks, complete_task, delete_task, update_task]

# Note: The actual FastMCP server setup (e.g., in main.py of mcp_server)
# would then expose these tools. For this setup, we'll create a simple
# FastMCP application that uses these tools.
