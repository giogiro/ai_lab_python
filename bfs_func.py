from collections import deque
from node_class import Node
import utils
def bfs(matrix, start, goal):
    
    #se non ho inizializzato le posizioni di start e goal ritorno None
    if goal == None or start == None:
        print("<BFS> non hai inserito il goal o lo start")
        return [], set()
    
    #reinizializzo visited e path, perchè sto rifacendo la ricerca
    visited = set()
    
    frontier = deque()
    #visited = set() #non serve, ho gia un attributo __visited in questa classe
    
    frontier.append(start)
    
    while frontier:
        
        node = frontier.popleft()   #perchè append mette alla fine della coda, e io prendo all'inizio
        
        for position in utils.actions(matrix, node):
            child = Node(position[0], position[1], node)
        
            if(child not in visited):
                visited.add(child)

                if(child == goal):
                    return utils.crea_path(child, start, goal), visited   #ho trovato il goal
                
                if(child not in frontier):
                    frontier.append(child)
    
    return [], set()  #non c'è una soluzione.
