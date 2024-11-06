import math


class Node :
    
    def __init__(self, row, col, padre=None, heur=None):
        self.row = row
        self.col = col
        self.padre = padre
        self.heur = heur
        
    def __eq__(self, other):
        # Controlla se l'altro oggetto è della stessa classe e se ha le stesse coordinate
        if isinstance(other, Node):
            return self.row == other.row and self.col == other.col
        return False
    
    def __hash__(self):
        # Combina row e y per generare un hash univoco per questo oggetto
        return hash((self.row, self.col))
    
        # Aggiungi il metodo per il confronto tra nodi (compara la euristica)
    def __lt__(self, other):
        return self.heur < other.heur  # Confronta in base alla euristica

    def setPadre(self, row, col):
        self.padre = Node(row, col)
        
    def setHeuristic(self, goal, type):
        if not isinstance(goal, Node):
            return
        
        if type == "euclidean":
            self.heur = math.sqrt( (self.row - goal.row )**2 + (self.col - goal.col)**2)
        
        elif type == "manhattan":
            # Distanza di Manhattan
            self.heur = abs(self.row - goal.row) + abs(self.col - goal.col)
        