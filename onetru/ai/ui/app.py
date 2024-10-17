"""
app.py - Handles the OneTru AI Workbench Agent functionality
"""

import chainlit as cl
import requests
from onetruai.ui.utils import handle_server_response

@cl.on_chat_start
async def chat_start():
    """
    Handles the start of a chat session.
    
    Sends a welcome message to the user.
    """
    welcome_message = "Welcome to the OneTru AI Workbench Agent! Please Ask your Questions below!"
    await cl.Message(content=welcome_message).send()
    cl.user_session.set("initialized", True)

@cl.on_message
async def handle_message(message: cl.Message):
    """
    Handles user messages, sends them to the server for processing,
    and displays the response back to the user.
    
    Args:
        message (cl.Message): The message received from the user.

    Returns:
        None
    """
    query = message.content
    try:
        response = requests.post(f"http://localhost:8000/query", params={"query": query})
        answer, text_elements, error_message = handle_server_response(response)
    except requests.exceptions.RequestException as e:
        error_message = "There was an issue processing your request."
    
    if error_message:
        await cl.Message(content=error_message).send()
    else:
        await cl.Message(content=answer, elements=text_elements).send()
