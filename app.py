import os
import logging
import re
import uuid
import json
from Message import MessageType
from Message import error_message
from flask import Flask, request
from slack import WebClient
from slackeventsapi import SlackEventAdapter
from Poll import poll
from typing import List

""" What VoteBot Does

The idea for this app is for users to be able to create a poll using "/vote [
title] [poll options]" and have others vote using reactions to the app's 
poll message. Once the voting is done, I want to use the plotly graphing 
library to output a pie chart with the results of the poll and the 
percentages of votes for each choice.
"""

# Initialize a Flask app to host the events adapter
app = Flask(__name__)
slack_events_adapter = SlackEventAdapter(os.environ["SLACK_SIGNING_SECRET"],
                                         "/slack/events", app)

slack_web_client = WebClient(
    token=os.environ['SLACK_BOT_TOKEN'])  # Initialize a Web API client

current_polls: List[poll] = []  # current_polls contains all running polls

poll_id: uuid  # The id number for the last poll added


@slack_events_adapter.on("reaction_added")
def reaction_added(event_data):
    # TODO: Find what poll the reaction was added to and keep a running count
    #  of the votes
    pass


@slack_events_adapter.on("reaction_removed")
def reaction_removed(event_data):
    # TODO: Find what poll the reaction was removed from and subtract the
    #  vote from the count
    pass


@app.route("/vote", methods=['POST'])
def poll_request(event_data):
    """
    poll_request works on the user's command "/vote [title] [poll options]"
    and based on the data creates a new poll and starts tracking the voting.

    Parameters:
        event_data: the json payload of data sent from slack triggered by a
        user performing the /vote command
    """
    # When someone sends a /vote command, the text header should contains
    # data in the form "[title] [poll options w/ commas between]"
    error_message(event_data)
    '''
    poll_command_text = re.split(',', event_data["text"])
    if not 3 < len(poll_command_text) < 6:
        error_handler(event_data)
    new_poll = poll(uuid.uuid4(), poll_command_text)
    current_polls.append(new_poll)
    # TODO: Create JSON message with the poll, and send the poll id to the
    #  user so they can end the poll
    '''
    pass


@app.route("/endvote", methods=['POST'])
def end_poll(event_data):
    """
    end_poll works on the user's command "/endvote [poll id]" and uses the
    poll id to find the poll and go through the process of stopping voting,
    creating the final graph, and sending to the user the finished results of
    the voting.

    Parameters:
        event_data: the json payload of data sent from slack triggered by a
        user performing the /endvote command
    """
    # To end a poll, the person who started it can use the poll id to end it
    # with the format "/endvote [poll id]". The chart should be created and
    # output in another message to the chat.
    poll_command_text = re.split('', event_data["text"])
    for p in current_polls:
        if poll_command_text[0] == p.id:
            # TODO: Create the chart of the poll, send it in a JSON message,
            #  then remove the poll from current_polls
            pass
    pass


@slack_events_adapter.on("error")
def error_handler(payload):
    """
    error_handler will take in a payload message describing what went wrong
    and send it to the user on slack
    """
    message = error_message(payload)
    slack_web_client.api_call("chat.postMessage", message)


if __name__ == "__main__":
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    logger.addHandler(logging.StreamHandler())
    # The first poll when the app is run is always id 1
    _poll_id = 0
    app.run(port=3000)
