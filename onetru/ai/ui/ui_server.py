"""
ui_server.py - FastAPI server for the OneTru AI Workbench UI
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

def get_app():
    """
    Create the FastAPI app with CORS middleware and health endpoint.
    
    Returns:
        FastAPI: The FastAPI app instance.
    """
    app = FastAPI()
    
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    @app.get("/healthy")
    async def healthy():
        """
        Health check endpoint.
        
        Returns:
            dict: Status of the application.
        """
        return {"status": "OK"}

    return app

def start_agent(host: str, port: int):
    """
    Starts the FastAPI server for the OneTru AI Workbench.

    Args:
        host (str): The host address.
        port (int): The port number.
    
    Returns:
        None
    """
    app = get_app()
    uvicorn.run(app, host=host, port=port)
