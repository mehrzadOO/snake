from collections import deque
from Utility import Node
from Algorithm import Algorithm


class BFS(Algorithm):
    def __init__(self, grid):
        super().__init__(grid)


    def run_algorithm(self, snake):
        # start clean
        self.frontier = deque([])
        self.explored_set = []
        self.path = []

        initialstate, goalstate = self.get_initstate_and_goalstate(snake)

        # open list
        self.frontier.append(initialstate)

        # while we have states in open list
        while len(self.frontier) > 0:
            node = self.frontier.popleft()
            self.explored_set.append(node)

            neighbors = self.get_neighbors(node)

            for neighbor in neighbors:
                if self.inside_body(snake, neighbor) or self.outside_boundary(neighbor):
                    self.explored_set.append(neighbor)

                elif neighbor not in self.frontier and neighbor not in self.explored_set:
                    neighbor.parent = node
                    self.explored_set.append(neighbor)
                    self.frontier.append(neighbor)

                    if neighbor.equal(goalstate):
                        return self.get_path(neighbor)

        return None
