class Node :
    
    def __init__(self, x, y, padre=None):
        self.x = x
        self.y = y
        self.padre = padre
        
    def __eq__(self, other):
        # Controlla se l'altro oggetto è della stessa classe e se ha le stesse coordinate
        if isinstance(other, Node):
            return self.x == other.x and self.y == other.y
        return False
    
    def __hash__(self):
        # Combina x e y per generare un hash univoco per questo oggetto
        return hash((self.x, self.y))

    def setPadre(self, x, y):
        self.padre = Node(x,y)