from collections import deque
import random
from node_class import Node
import utils

def dfs(matrix, start, goal):
    
    visited = set()
    path = []

    #se start e goal sono nella stessa posizione, il path è solo start.
    if start == goal:
        visited.add(start)
        path.append(start)
        utils.stampa_risultato(matrix, start, goal, path, visited)
    
    else:   #se no, fai la chiamata alla vera dfs
        node = recursive_dfs(matrix, start, goal, path, visited)

        if(node):   #se ho trovato il nodo, creo il path, se no il path resta vuoto
            path = utils.crea_path(node, start, goal)
    
    #in qualsiasi caso stampo il risultato
    utils.stampa_risultato(matrix, start, goal, path, visited)
    

def recursive_dfs(matrix, curr, goal, path, visited):
    
    valid_moves = utils.actions(matrix, curr)
    #Mixo le mosse valide, così da non seguire sempre gli stessi pattern
    random.shuffle(valid_moves)
    
    for position in valid_moves:
        child = Node(position[0], position[1], curr)
        
        if child not in visited:
            visited.add(child)
            
            if child == goal:
                return child
            
            result = recursive_dfs(matrix, child, goal, path, visited)
            
            #se ho trovato un nodo == goal, ritorno, se no provo le altre mosse di questo nodo
            if result:
                return result
            
        
    return None
    