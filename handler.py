import json
import requests
from loguru import logger as log


def hello(event, context):
    response = requests.get('https://www.google.com')
    message = [
        "Go Serverless v1.0! Your function executed successfully!",
        f"Request Google - Status Code: {response.status_code}",
    ]

    # Response Formation
    body = {
        "message": "\n".join(message),
        "input": event
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }
    
    log.info(response)

    return response

    # Use this code if you don't use the http event with the LAMBDA-PROXY
    # integration
    """
    return {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "event": event
    }
    """

if __name__ == "__main__":
    hello('', '')