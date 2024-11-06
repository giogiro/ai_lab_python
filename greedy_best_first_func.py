from collections import deque
import heapq
import queue
import random
from node_class import Node
import utils

def greedy_best_first(matrix, start, goal, heuristic):
    
    goal_found = False
    #izializzo visited e path
    path = []
    visited = set()
    
    # La lista delle priorità, che simula la coda di priorità
    frontier = []
    heapq.heappush(frontier, (0, start))  # (priorità, nodo), la priorità è la euristica 0 per il nodo di partenza
        
    while frontier and not goal_found:
        
        _, node = heapq.heappop(frontier)
        
        valid_moves = utils.actions(matrix, node)
        #Mixo le mosse valide, così da non seguire sempre gli stessi pattern
        random.shuffle(valid_moves)
    
        for position in valid_moves:
            
            
            child = Node(position[0], position[1], node)
            
            child.setHeuristic(goal, heuristic)
            
            if(child not in visited):
                visited.add(child)

                if(child == goal):
                    path = utils.crea_path(child, start, goal)   #ho trovato il goal
                    goal_found = True  # Imposta il flag a True per uscire dal ciclo
                    break   #esce dal ciclo for
                
                if(child not in frontier):
                    heapq.heappush(frontier, (child.heur, child))  # Aggiungi alla coda di priorità (heap)

    print("\nGreedy Best First Search:")
    utils.stampa_risultato(matrix, start, goal, path, visited)
