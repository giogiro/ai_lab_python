from node_class import Node
from collections import deque
from colorama import init, Fore, Back, Style

class Game :
    
    def __init__(self, matrix):
        self.__matrix = matrix      #"matrice" di gioco, campo
        self.__start = None         #nodo di start
        self.__goal = None          #nodo di end
        self.__path = []            #lista di nodi del percorso da start a end
        self.__visited = set()      #lista di nodi visitati
        
    def init_start(self, row, col):
        if self.__matrix[row][col] == " ":  #se la posizione non è #, cioè è valida
            self.__path = []    # reinizializzo il path, perchè sto cambiando la posizione di start
            self.__visited = set()  #reinizializzo anche visited
            
            #impongo la posizione giusta del nodo se ho inserito val negativi
            row = len(self.__matrix)+row if row < 0 else row
            col = len(self.__matrix[0])+col if col < 0 else col
            
            #creo il nodo __me
            self.__start = Node(row,col)   
        else:
            print("<init_goal>  posizione non valida")
        
        return False if self.__start == None else True
        
        
    #stessa cosa di init_start, però metto la G di goal
    def init_goal(self, row, col):
        if self.__matrix[row][col] == " ":
            self.__path = []    # reinizializzo il path, perchè sto la posizione di goal
            self.__visited = set()  ##reinizializzo anche visited

            #impongo la posizione giusta del nodo se ho inserito val negativi
            row = len(self.__matrix)+row if row < 0 else row
            col = len(self.__matrix[0])+col if col < 0 else col
            #creo il nodo goal
            self.__goal = Node(row,col)
        else:
            print("<init_goal>  posizione non valida")
        
        return False if self.__goal == None else True
    

    #stampa UNA COPIA della matrice, alla quale aggiungo S, G, nodi visitati e percorso
    def stampa(self):
        mod_matrix = self.__matrix
        if(self.__start != None):   #se ho gia impostato start
            mod_matrix[self.__start.row][self.__start.col] = Fore.RED + "S" + Fore.BLUE #coloro S di rosso
        if(self.__goal != None):    #se ho gia impostato goal
            mod_matrix[self.__goal.row][self.__goal.col] = Fore.RED + "G" + Fore.BLUE #coloro G di roos
        if(self.__path != []):  #se ho gia trovato il percorso
            for node in self.__path:
                mod_matrix[node.row][node.col] =  Style.RESET_ALL + "+" + Fore.BLUE    #se ho trovato il path, lo disegno sulla matrixce
                # e li coloro di blu
        if(self.__visited):     #se ho visitato dei nodi
                for node in self.__visited:
                    #"disegno" le posizioni visitate solo se non sono nodi di goal, start, oppure se non ci ho gia messo + (nodi del path)
                    if node != self.__goal and node != self.__start and mod_matrix[node.row][node.col] != Style.RESET_ALL + "+" + Fore.BLUE:
                        mod_matrix[node.row][node.col] =  Fore.YELLOW + "." + Fore.BLUE    #se ho visitato nodi, li disegno
        
        for row in mod_matrix:  #stampo matrice riga per  riga
            print( Fore.BLUE + "".join(row) + Style.RESET_ALL)
        
        Style.RESET_ALL


    #actions ritorna una lista di liste ( [row1,col1], [row2, col2], ... ) queste ultime sono
    #posizioni valide per fare la mossa
    def actions(self, node):
        possible_actions = []
        if(node.row > 0  and self.__matrix[node.row - 1][node.col] != "#"): #provo nodo sopra
            possible_actions.append([node.row-1, node.col])
        if(node.row < len(self.__matrix)-1 and self.__matrix[node.row + 1][node.col] != "#"):   #provo nodo sotto
            possible_actions.append([node.row+1, node.col])
        if(node.col > 0 and self.__matrix[node.row][node.col-1] != "#"):    #provo nodo a sx
            possible_actions.append([node.row, node.col-1])
        if(node.col < len(self.__matrix[0])-1 and self.__matrix[node.row][node.col+1] != "#"):  #provo nodo a dx
            possible_actions.append([node.row, node.col+1])
        
        return possible_actions
    
    
    def crea_path(self, node):  #percorro il percorso al contrario, da goal->goal.padre->padre->padre->padre...->None
        curr = node
        while curr != None:
            if(curr != self.__start and curr != self.__goal):   #se il nodo è il goal o start non lo aggiungo
                self.__path.append(curr)
            curr = curr.padre
        
        self.__path.reverse()   #e alla fine inverto 
        
    #ritorna il path come stringa
    def path_toString(self):
        res = "Percorso: "
        for node in self.__path:
            res = res + "(" + str(node.col) + ", " + str(node.row) + ") "
            
        return res
    
    #ritorna quanti nodi ho visitato
    def size_visited(self):
        return len(self.__visited)
    
    def BFS(self):
        
        #se non ho inizializzato le posizioni di start e goal ritorno None
        if self.__goal == None or self.__start == None:
            print("<BFS> non hai inserito il goal o lo start")
            return None
        
        #reinizializzo visited e path, perchè sto rifacendo la ricerca
        self.__path = []
        self.__visited = set()
        
        frontier = deque()
        #visited = set() #non serve, ho gia un attributo __visited in questa classe
        
        frontier.append(self.__start)
        
        while frontier:
            
            node = frontier.popleft()   #perchè append mette alla fine della coda, e io prendo all'inizio
            
            for position in self.actions(node):
                child = Node(position[0], position[1], node)
            
                if(child not in self.__visited):
                    self.__visited.add(child)

                    if(child == self.__goal):
                        self.crea_path(child)
                        return
                    
                    if(child not in frontier):
                        frontier.append(child)
        
        return None       
                
    
    

            
            
