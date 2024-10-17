"""
Utils module for OneTru AI Workbench backend utilities.
"""

def format_query(query: str) -> str:
    """
    Formats the user query before sending it to the AI server.
    
    Args:
        query (str): The raw query input from the user.
    
    Returns:
        str: The formatted query, typically cleaned or normalized for processing.
    """
    return query.strip().lower()


def handle_server_response(response):
    """
    Processes the server response to extract relevant information.

    Args:
        response (requests.Response): The response object returned by the server.

    Returns:
        tuple: A tuple containing (answer, text_elements, error_message).
            - answer (str): The final answer from the server.
            - text_elements (list): Additional text elements for rich content.
            - error_message (str): Error message if the request failed.
    """
    if response.status_code == 200:
        data = response.json()
        answer = data.get("answer", "No answer found.")
        text_elements = data.get("text_elements", [])
        return answer, text_elements, None
    else:
        return None, [], f"Error: {response.status_code}"
