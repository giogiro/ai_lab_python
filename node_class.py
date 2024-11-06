class Node :
    
    def __init__(self, row, col, padre=None):
        self.row = row
        self.col = col
        self.padre = padre
        
    def __eq__(self, other):
        # Controlla se l'altro oggetto è della stessa classe e se ha le stesse coordinate
        if isinstance(other, Node):
            return self.row == other.row and self.col == other.col
        return False
    
    def __hash__(self):
        # Combina row e y per generare un hash univoco per questo oggetto
        return hash((self.row, self.col))

    def setPadre(self, row, col):
        self.padre = Node(row, col)