from collections import deque
import random
from node_class import Node
import utils

def bfs(matrix, start, goal):
    
    #izializzo visited e path
    path = []
    visited = set()
    
    frontier = deque()
    #visited = set() #non serve, ho gia un attributo __visited in questa classe
    
    frontier.append(start)
    
    while frontier:
        
        node = frontier.popleft()   #perchè append mette alla fine della coda, e io prendo all'inizio
        
        valid_moves = utils.actions(matrix, node)
        #Mixo le mosse valide, così da non seguire sempre gli stessi pattern
        random.shuffle(valid_moves)
    
        for position in valid_moves:
            child = Node(position[0], position[1], node)
        
            if(child not in visited):
                visited.add(child)

                if(child == goal):
                    path = utils.crea_path(child, start, goal)   #ho trovato il goal
                    break
                
                if(child not in frontier):
                    frontier.append(child)
    
    print("\nBFS:")
    utils.stampa_risultato(matrix, start, goal, path, visited)
