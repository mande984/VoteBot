from typing import List
import uuid
import json


class poll:
    # Each poll will have its own id for keeping track of which is which
    id: uuid

    # Poll choices are held as strings, there are at most 5 choices in a poll
    poll_choices: List[str]

    # Each poll will have its own title
    poll_title: str

    # The graph for the poll, filled when the end process is started
    end_chart = None

    def end(self):
        """
        end will call chart on the current poll and return the graph for the
        poll

        Returns:
            graph of the poll as a Chart object
        """
        pass

    def __init__(self, poll_id: uuid, p_choices: List[str]):
        """
        Poll helps keep individual poll data separate by giving each an ID
        number and holding poll data for creating JSON messages.

        Parameters:
            poll_id (int): the unique id for the poll
            p_choices (List[str]): the title for the poll and the choices to
            vote on as a list
        """
        self.id = poll_id
        self.poll_title = p_choices.pop(0)
        self.poll_choices = p_choices

    # TODO: Create a function to create JSON message containing the info for
    #  a poll and post it as the user who created the poll
    def display_poll(self):
        """
        display_poll creates a JSON payload for slack that shows the current
        poll and it's options so that users can vote on it

        Returns:
            json_payload: the poll, held as a json object
        """
        json_payload = {
            "blocks": [
                {
                    "type": "section",
                    "text": {
                        "type": "mrkdwn",
                        "text": self.poll_title
                    }
                },
                {
                    "type": "divider"
                }
            ]
        }

        for option in self.poll_choices:
            json_poll_option = {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": option
                }
            }
        return 0
