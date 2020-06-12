import os
import logging
import re
from flask import Flask
from flask import request
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

# Initialize a Web API client
slack_web_client = WebClient(token=os.environ['SLACK_BOT_TOKEN'])

# current_polls contains the polls that are running
current_polls: List[poll] = []

# The id number for the last poll added
_poll_id: int


@staticmethod
def get_poll_id(poll_id=_poll_id):
    """
    get_poll_id is a static method that increases the current _poll_id and
    returns the next id as an int so a new poll can be created

    Returns:
        poll_id (int): an empty poll id for the next poll to use
    """
    # TODO: Replace all usage of incremental id's with uuid
    return poll_id + 1


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
    # When someone sends a /vote command, the text header should contains
    # data in the form "[title] [poll options w/ commas between]"
    poll_command_text = re.split(',', event_data["text"])
    if not 3 < len(poll_command_text) < 6:
        # TODO: Create JSON error message for incorrect input
        pass
    new_poll_id = get_poll_id()
    new_poll = poll(new_poll_id, poll_command_text)
    current_polls.append(new_poll)
    # TODO: Create JSON message with the poll, and send the poll id to the
    #  user so they can end the poll


@app.route("/endvote", methods=['POST'])
def end_poll(event_data):
    # To end a poll, the person who started it can use the poll id to end it
    # with the format "/endvote [poll id]". The chart should be created and
    # output in another message to the chat.
    # TODO: Parse input to make sure the poll id is correct
    # TODO: Create the chart of the poll, send it in a JSON message,
    #  then remove the poll from current_polls
    pass


@slack_events_adapter.on("error")
def error_handler(error):
    # TODO: Create a JSON error message
    pass


if __name__ == "__main__":
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    logger.addHandler(logging.StreamHandler())
    # The first poll when the app is run is always id 1
    _poll_id = 0
    app.run(port=3000)
