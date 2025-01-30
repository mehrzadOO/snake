from Algorithm import Algorithm


class A_STAR(Algorithm):
    def __init__(self, grid):
        super().__init__(grid)

    def run_algorithm(self, snake):
        self.frontier = []
        self.explored_set = []
        self.path = []

        initialstate, goalstate = self.get_initstate_and_goalstate(snake)

        self.frontier.append(initialstate)

        while len(self.frontier) > 0:

            lowest_index = 0
            for i in range(len(self.frontier)):
                if self.frontier[i].f < self.frontier[lowest_index].f:
                    lowest_index = i

            lowest_node = self.frontier.pop(lowest_index)

            if lowest_node.equal(goalstate):
                return self.get_path(lowest_node)

            self.explored_set.append(lowest_node)
            neighbors = self.get_neighbors(lowest_node)

            for neighbor in neighbors:
                if self.inside_body(snake, neighbor) or self.outside_boundary(neighbor) or neighbor in self.explored_set:
                    continue

                g = lowest_node.g + 1
                best = False

                if neighbor not in self.frontier:
                    neighbor.h = self.euclidean_distance(goalstate, neighbor)
                    self.frontier.append(neighbor)
                    best = True
                elif lowest_node.g < g:
                    best = True

                if best:
                    neighbor.parent = lowest_node
                    # neighbor.g = g
                    neighbor.f = neighbor.g + neighbor.h
        return None