from node_class import Node
from collections import deque
from colorama import init, Fore, Back, Style

class Game :
    
    def __init__(self, matrix):
        self.__matrix = matrix
        self.__start = None
        self.__goal = None
        self.__path = []
        self.__visited = set()
        
    def init_start(self, x, y):
        if self.__matrix[x][y] == " ":
            self.__path = []    # reinizializzo il path, perchè sto cambiando il percorso
            
            #impongo la posizione giusta del nodo se ho inserito val negativi
            x = len(self.__matrix)+x if x < 0 else x
            y = len(self.__matrix[0])+y if y < 0 else y
            
            #creo il nodo __me
            self.__start = Node(x,y)   
        else:
            print("<init_goal>  posizione non valida")
        
        return False if self.__start == None else True
        
        
    def init_goal(self, x, y):
        if self.__matrix[x][y] == " ":
            self.__path = []    # reinizializzo il path, perchè sto cambiando il percorso
            
            #impongo la posizione giusta del nodo se ho inserito val negativi
            x = len(self.__matrix)+x if x < 0 else x
            y = len(self.__matrix[0])+y if y < 0 else y
            #creo il nodo goal
            self.__goal = Node(x,y)
        else:
            print("<init_goal>  posizione non valida")
        
        return False if self.__goal == None else True
    

    def stampa(self):
        mod_matrix = self.__matrix
        if(self.__start != None):
            mod_matrix[self.__start.x][self.__start.y] = Fore.RED + "S" + Fore.BLUE #coloro S di rosso
        if(self.__goal != None):
            mod_matrix[self.__goal.x][self.__goal.y] = Fore.RED + "G" + Fore.BLUE #coloro G di roos
        if(self.__path != []):
            for node in self.__path:
                mod_matrix[node.x][node.y] =  Style.RESET_ALL + "+" + Fore.BLUE    #se ho trovato il path, lo disegno sulla matrice
                # e li coloro di blu
        if(self.__visited):
                for node in self.__visited:
                    #"disegno" le posizioni visitate solo se non sono nodi di goal, start, oppure nel path
                    if node != self.__goal and node != self.__start and mod_matrix[node.x][node.y] != Style.RESET_ALL + "+" + Fore.BLUE:
                        mod_matrix[node.x][node.y] =  Fore.YELLOW + "." + Fore.BLUE    #se ho visitato nodi, li disegno
        
        for row in mod_matrix:
            print( Fore.BLUE + "".join(row) + Style.RESET_ALL)
        
        Style.RESET_ALL


    #actions ritorna una lista di liste ( [x1,y1], [x2, y2], ... ) queste ultime sono
    #posizioni valide per fare la mossa
    def actions(self, node):
        possible_actions = []
        if(node.x > 0  and self.__matrix[node.x - 1][node.y] != "#"):
            possible_actions.append([node.x-1, node.y])
        if(node.x < len(self.__matrix)-1 and self.__matrix[node.x + 1][node.y] != "#"):
            possible_actions.append([node.x+1, node.y])
        if(node.y > 0 and self.__matrix[node.x][node.y-1] != "#"):
            possible_actions.append([node.x, node.y-1])
        if(node.y < len(self.__matrix[0])-1 and self.__matrix[node.x][node.y+1] != "#"):
            possible_actions.append([node.x, node.y+1])
        
        return possible_actions
    
    
    def crea_path(self, node):
        curr = node
        while curr != None:
            if(curr != self.__start and curr != self.__goal):
                self.__path.append(curr)
            curr = curr.padre
        
        self.__path.reverse()    
        
            
    def path_toString(self):
        res = "Percorso: "
        for node in self.__path:
            res = res + "(" + str(node.y) + ", " + str(node.x) + ") "
            
        return res
    
    def size_visited(self):
        return len(self.__visited)
    
    def BFS(self):
        
        #se non ho inizializzato le posizioni di start e goal ritorno None
        if self.__goal == None or self.__start == None:
            print("<BFS> non hai inserito il goal o lo start")
            return None
        
        
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
                
         

            
            
