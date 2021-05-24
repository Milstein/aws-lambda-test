import json


def hello(event, context):
    body = {
        "message": "v1.0!"
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response

    # Use this code if you don't use the http event with the LAMBDA-PROXY
    # integration
    """
    return {
        "message": "v1.0!",
        "event": event
    }
    """

def imageResize(event, context):
    body = {
        "message": "resized your image"
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response
