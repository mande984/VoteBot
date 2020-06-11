from Chart import *


class Poll:
    """ What Poll Does

        Poll helps keep individual poll data separate by giving each an ID
        number and holding poll info for other
        classes to process
    """
    # Each poll will have its own id for keeping track of which is which
    id: int

    # Poll choices are held as strings, there are at most 5 choices in a poll
    poll_choices: str = ["" for x in range(5)]

    """
    get_graph takes in a poll object and sends it to chart to return a 
    visual of the results
    """
    def get_graph(self):
        return Chart(self)

    def __init__(self, poll_id: int):
        self.id = poll_id
