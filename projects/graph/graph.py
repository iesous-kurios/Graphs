"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """

        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError("Does not exist")

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        # make a queue
        q = Queue()

        # make a set to track which nodes we have visited
        visited = set()

        # enqueue the starting node
        q.enqueue(starting_vertex)

        # loop while the queue isn't empty
        while q.size() > 0:
            # deque, this is our current node
            current_node = q.dequeue()

            # check to see if we have visited
            if current_node not in visited:
                print(current_node)
            # if not, we go to node add to visited
                visited.add(current_node)

                # then we get the neighbors
                neighbors = self.get_neighbors(current_node)

                # iterate over the neighbors, enque them
                for neighbor in neighbors:
                    q.enqueue(neighbor)




    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # make the stack
        stack = Stack()

        # make set to keep track of visited nodes
        visited = set()

        # push the first node
        stack.push(starting_vertex)

        # loop through while stack is not empty
        while stack.size() > 0:
            # pop, this is our current node
            current_node = stack.pop()

            # check to see if visited already

            if current_node not in visited:
                print(current_node)
                visited.add(current_node)

            # get the neighbors
                neighbors = self.get_neighbors(current_node)

            # loop through and stack neighbors
                for neighbor in neighbors:
                    stack.push(neighbor)


    def dft_recursive(self, vertex, visited=set()):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.

        1. need a base case

        2. need to call itself

        """

        

        if vertex not in visited:
            visited.add(vertex)
            print(vertex)

            neighbors = self.get_neighbors(vertex)
            if len(neighbors) == 0:
                return neighbors
            else:
                for neighbor in neighbors:
                    self.dft_recursive(neighbor, visited)

        

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.

        1. stop when we find the target node

        2. return the path we took to get the current node 
         - note, bfs will automatically be the shortest path

        Enqueue the PATH to the target node
        """
        # make a queue
        q = Queue()

        # make a set to track visited nodes
        visited = set()

        # enqueue the starting node
        q.enqueue([starting_vertex])


        # loop while queue is not empty
        while q.size() > 0:
            # dequeue, this is our current node
            current_path = q.dequeue()
            current_node = current_path[-1]


            # check to see if we found our target node
            if current_node == destination_vertex:
                # we are done!
                return current_path
                # check to see if we have visited

            if current_node not in visited:

                # if not, then add to visited
                visited.add(current_node)


                # then go to it and get its neighbors

                neighbors = self.get_neighbors(current_node)

                # enqueue the path to  neighbors
                for neighbor in neighbors:
                    path_copy = current_path + [neighbor]

                    q.enqueue(path_copy)






    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        # Create an empty stack and add current_path to it
        # i.e., Add [starting_vertex] to the stack
        stack = Stack()
        stack.push([starting_vertex])
        # Create an empty visited set to track the vertices if they are visited or not
        visited = set()
        # while stack is not empty
        while stack.size():
            # Get the path from stack by deleting it
            current_path = stack.pop()
            # Get the current_vertex from current_path array(last item in the array)
            current_vertex = current_path[-1]
            # if current_vertex is not in the visited set
            if current_vertex not in visited:
                #Add it to the visited set
                visited.add(current_vertex)
                # if current vertex == destination_vertex
                if current_vertex == destination_vertex:
                    return current_path  # return the current path
                else:
                    #for every neighbor of the current vertex
                    for neighbor in self.vertices[current_vertex]:
                        # get the copy of the current path
                        current_path_copy = list(current_path)
                        # add neighbor to current path copy
                        current_path_copy.append(neighbor)
                        # add the whole current path copy to the stack
                        stack.push(current_path_copy)
        return None

    def dfs_recursive(self, starting_vertex, destination_vertex, path=[], visited=set()):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        

        """

        if len(path) == 0:
            path.append(starting_vertex)
        if starting_vertex == destination_vertex:
            return path

        if starting_vertex not in visited:
            visited.add(starting_vertex)

            neighbors = self.get_neighbors(starting_vertex)

            for neighbor in neighbors:
                path_copy = path + [neighbor]

                # only return if we found destination_vertex


                result = self.dfs_recursive(neighbor, destination_vertex, path_copy)
                if result is not None:
                    return result

if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
    
