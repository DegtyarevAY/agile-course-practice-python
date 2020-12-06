from dijkstra_algorithm.model.dijkstra import Graph
import re


def is_correct_number_entered(value):
    if value is None or len(str(value).strip()) == 0:
        return False
    else:
        is_int_value = re.match("\\d+$", str(value))
        if is_int_value is None:
            return False
        else:
            int_value = int(value)
            if int_value <= 0:
                return False
            return True


class DAViewModel:
    def __init__(self, num_vertex=0):
        self.num_vertex = ''
        self.start_vertex = ''
        self.btn_create_graph_state = 'disabled'

    def set_num_vertex(self, value):
        self.num_vertex = value

        if is_correct_number_entered(value):
            self.set_btn_create_graph_enabled()
        else:
            self.set_btn_create_graph_disabled()

    def get_num_vertex(self):
        return self.num_vertex

    def set_btn_create_graph_disabled(self):
        self.btn_create_graph_state = 'disabled'

    def set_btn_create_graph_enabled(self):
        self.btn_create_graph_state = 'normal'

    def get_btn_create_graph_state(self):
        return self.btn_create_graph_state

    def set_start_vertex(self, start):
        self.start_vertex = start

    def get_start_vertex(self):
        return self.start_vertex

    def run_dijkstra(self, matrix):
        weights = [[int(val) for val in row] for row in matrix]
        graph = Graph(int(self.num_vertex), weights)
        return graph.dijkstra(int(self.start_vertex))
