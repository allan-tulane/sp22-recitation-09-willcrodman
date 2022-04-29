from collections import deque
from heapq import heappush, heappop 

def shortest_path(visited, frontier, graph):
    if len(frontier) == 0:
        return visited
    else:
        distance, node, edge_count = heappop(frontier)
        if node in visited:
            return shortest_path(visited, frontier, graph)
        else:
            visited[node] = (distance, edge_count)
            for neighbor, weight in graph[node]:
              print(distance + weight, neighbor, edge_count)
              heappush(frontier, (distance + weight, neighbor, edge_count + 1))                
        return shortest_path(visited, frontier, graph)

def shortest_shortest_path(graph, source):
    frontier = []
    visited = dict() 
    heappush(frontier, (0, source, 0))
    return shortest_path(visited, frontier, graph)
    
def test_shortest_shortest_path():

    graph = {
                's': {('a', 1), ('c', 4)},
                'a': {('b', 2)}, # 'a': {'b'},
                'b': {('c', 1), ('d', 4)}, 
                'c': {('d', 3)},
                'd': {},
                'e': {('d', 0)}
            }
    result = shortest_shortest_path(graph, 's')
    # result has both the weight and number of edges in the shortest shortest path
    assert result['s'] == (0,0)
    assert result['a'] == (1,1)
    assert result['b'] == (3,2)
    assert result['c'] == (4,1)
    assert result['d'] == (7,2)
    
    
def bfs_path(graph, source):
    result = dict() 
    frontier = set([source])
    while len(frontier) != 0:
        source = frontier.pop()
        neighbors = graph[source]
        for leaf in neighbors: 
          if leaf not in result.keys():
            frontier.add(leaf)
            result[leaf] = source
    return result 

def get_sample_graph():
     return {'s': {'a', 'b'},
            'a': {'b'},
            'b': {'c'},
            'c': {'a', 'd'},
            'd': {}
            }

def test_bfs_path():
    graph = get_sample_graph()
    parents = bfs_path(graph, 's')
    assert parents['a'] == 's'
    assert parents['b'] == 's'    
    assert parents['c'] == 'b'
    assert parents['d'] == 'c'
    
def get_path(parents, destination):
    source = list(parents.values())[0]
    path = str(source)
    neighbors = [k for k, v in parents.items() if v == path[-1]]
  
    while destination not in neighbors:
        for leaf in neighbors:
          if leaf in parents.values():
            path += leaf
            neighbors = [k for k, v in parents.items() if v == path[-1]]

    return path

def test_get_path():
    graph = get_sample_graph()
    parents = bfs_path(graph, 's')
    assert get_path(parents, 'd') == 'sbc'


graph = {'s': {'a', 'b'},
            'a': {'b'},
            'b': {'c'},
            'c': {'a', 'd'},
            'd': {}
            }