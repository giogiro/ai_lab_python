from node_class import Node
from collections import deque
from colorama import init, Fore, Back, Style
from bfs_func import bfs
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
        self.__path, self.__visited = bfs(self.__matrix, self.__start, self.__goal)
                
    
    

            
            
