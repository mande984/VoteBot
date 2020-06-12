from Chart import chart
from typing import List


class poll:
    # Each poll will have its own id for keeping track of which is which
    id: int
    # TODO: Replace all usage of incremental id's with uuid

    # Poll choices are held as strings, there are at most 5 choices in a poll
    poll_choices: List[str]

    # Each poll will have its own title
    poll_title: str

    def get_graph(self):
        """
        get_graph takes in a poll object and sends it to chart to return a
        visual of the results.

        Returns:
            chart (chart): The data from the poll as a pie chart
        """
        return chart(self)

    def get_poll_id(self):
        """
        get_poll_id takes in a poll object and returns the id number of the
        poll.

        Returns:
            self.id (int): The id number of the poll
        """
        # TODO: Replace all usage of incremental id's with uuid
        return self.id

    #TODO: Create a function to create JSON message containing the info for a
    # poll and post it as the user who created the poll

    # TODO: Create a destructor for the poll when it is finished

    # TODO: Create a function that makes a JSON message containing the
    #  finalized poll data along with the graph

    def __init__(self, poll_id: int, p_choices: List[str]):
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
