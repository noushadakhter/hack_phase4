from fastmcp import FastMCP
from fastapi import FastAPI, Depends
from sqlmodel import Session
from contextlib import asynccontextmanager

from mcp_server.tools import ALL_TOOLS
from backend.app.database import engine, get_session # Assuming backend is in PYTHONPATH

@asynccontextmanager
async def lifespan(app: FastAPI):
    # This runs when the FastMCP app starts up.
    # We can perform any necessary initialization here, e'g. check DB connection.
    print("FastMCP server starting up...")
    try:
        # Attempt to get a session to verify database connectivity
        async for session in get_session():
            print("Database connection verified for FastMCP server.")
            break # Exit after successful connection
    except Exception as e:
        print(f"Error connecting to database from FastMCP server: {e}")
        # Depending on requirements, you might want to raise the exception or log more thoroughly
    yield
    # This runs when the FastMCP app shuts down.
    print("FastMCP server shutting down...")

app = FastMCP(
    title="Todo AI Chatbot MCP Server",
    version="0.1.0",
    tools=ALL_TOOLS,
    lifespan=lifespan
)

# Optional: Add a health check endpoint for the MCP server itself
@app.get("/mcp_health", tags=["monitoring"])
async def mcp_health_check(session: Session = Depends(get_session)):
    try:
        # Attempt to execute a simple query to check database connectivity
        session.exec("SELECT 1")
        return {"status": "ok", "message": "MCP Server and database are healthy"}
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"MCP Server database connection failed: {e}"
        )