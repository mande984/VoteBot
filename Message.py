import json
from enum import Enum
import os


class MessageType(Enum):
    ERROR = 0
    POLL_CREATED = 1
    POLL_ENDED = 2


def create_message(type: MessageType, *args):
    """
    create_message is a helper function for creating json messages to be
    exported to slack. It takes in a MessageType and different arguments to
    help create the message and returns the correctly formatted message.

    Parameters:
        type: the message type to be created

    Returns:
        the json payload to be sent to slack to display to the user
    """
    if type == MessageType.ERROR:
        return error_message(args[0])
    if type == MessageType.POLL_CREATED:
        pass
    if type == MessageType.POLL_ENDED:
        pass


def error_message(payload):
    """
    error_message creates an error message payload to be sent to slack

    Parameters:
        payload: the channel id that the error message to be sent to

    Returns:
        the error message as a json payload
    """
    exit_message = {
        "channel": payload["channel_id"],
        "text": {
            "type": "mrkdwn",
            "text": "There has been an error, please try again!"
        }
    }
    return exit_message
