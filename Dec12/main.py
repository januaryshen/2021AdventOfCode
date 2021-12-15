import os
from collections import defaultdict


class Graph:
    def __init__(self):
        self._nodes: defaultdict[str, list] = defaultdict(list)

    def add_edge(self, node: str, neighbor: str):
        """Add an edge to the graph going in both directions"""
        self._nodes[node].append(neighbor)
        self._nodes[neighbor].append(node)

    def get_neighbors(self, node: str) -> list[str]:
        """Get the neighbors of a given node"""
        return self._nodes[node]

    def is_small_cave(self, node: str) -> bool:
        """Check if a node is a small cave (i.e. it contains only lowercase letters)"""
        return node.islower()

    def __dfs_count1(self, current: str, start: str, end: str, visited: set) -> int:
        """
        Using DFS, recursively find all paths from start to end that visit small caves at most once.
        Large caves can be visited any number of times.
        Args:
            current (str): The current node
            start (str): The starting node
            end (str): The ending node
            visited (set): The set of visited nodes
        Returns:
            int: The number of paths
        """
        # path found
        if current == end:
            return 1

        # return total of paths found from each neighbor
        # a neighbor can be visited if it is a large cave
        # or if it is a small cave and it has not been visited
        return sum(
            self.__dfs_count1(neighbor, start, end, visited | {neighbor})
            for neighbor in self.get_neighbors(current)
            if not self.is_small_cave(neighbor) or neighbor not in visited
        )

    def find_path_count1(self, start: str, end: str) -> int:
        """
        Count paths from start to end by calling the recursive helper function __dfs_count
        Args:
            start (str): The starting node
            end (str): The ending node
        Returns:
            int: The number of paths
        """
        return self.__dfs_count1(current=start, start=start, end=end, visited={start})

    def __str__(self):
        return str(self._nodes)

    def __dfs_count2(
        self,
        current: str,
        start: str,
        end: str,
        visited: set,
        can_visit_twice: bool = True,
    ) -> int:
        """
        Using DFS, recursively find all paths from start to end that visit small caves at most once,
        with the exception of a single small cave that can be visited twice.
        Large caves can be visited any number of times.
        Args:
            current (str): The current node
            start (str): The starting node
            end (str): The ending node
            visited (set): The set of visited nodes
            can_visit_twice (bool): Whether or not it is permitted to add a visited small cave a second time
        Returns:
            int: The number of paths
        """
        if current == end:
            return 1

        count = 0

        # add up paths from visiting each neighbor
        for neighbor in self.get_neighbors(current):
            # visit if node is a large cave or a small cave that has not been visited before
            if not self.is_small_cave(neighbor) or neighbor not in visited:
                count += self.__dfs_count2(
                    neighbor, start, end, visited | {neighbor}, can_visit_twice
                )
            # if it's a small cave and we still can visit a small cave twice
            elif can_visit_twice and neighbor not in {start, end}:
                # add the rest of the paths while not visiting the same small cave twice
                count += self.__dfs_count2(
                    neighbor, start, end, visited | {neighbor}, False
                )

        return count

    def find_path_count2(self, start: str, end: str) -> int:
        """
        Count paths from start to end by calling the recursive helper function __dfs_count
        Args:
            start (str): The starting node
            end (str): The ending node
        Returns:
            int: The number of paths
        """
        return self.__dfs_count2(current=start, start=start, end=end, visited={start})

    @classmethod
    def from_file(cls, filename: str) -> "Graph":
        """
        Create a graph from a file
        Args:
            filename (str): The filename
        Returns:
            Graph: The graph
        """
        graph = cls()
        with open(filename) as f:
            data = f.read().splitlines()
        for line in data:
            node, neighbor = line.split("-")
            graph.add_edge(node, neighbor)
        return graph


def part1(inputData):
    graph = Graph.from_file(inputData)
    print(graph.find_path_count1("start", "end"))


def part2(inputData):
    graph = Graph.from_file(inputData)
    print(graph.find_path_count2("start", "end"))


if __name__ == "__main__":
    input_data = "./data.txt"
    # source:https://github.com/DenverCoder1/Advent-of-Code-2021/blob/main/Day-12/part2.py
    part1(input_data)
    part2(input_data)

