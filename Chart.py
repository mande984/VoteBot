from Poll import poll
import plotly.express as px


class chart:
    """ What Chart Does

    Chart is a class that takes in a poll object and creates a pie chart
    using plotly to display the data in a nice way
    """

    """
    create_graph takes in a chart object and returns a plotly graph based off 
    of the poll data
    """
    def create_graph(self):
        # TODO: Create a graph using plotly based on the data of a finished
        #  poll and return it
        pass

    def __init__(self, poll: poll):
        self.poll = poll
