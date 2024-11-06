from node_class import Node
from bfs_func import bfs
from dfs_func import dfs
class Game :
    
    def __init__(self, matrix):
        self.__matrix = matrix      #"matrice" di gioco, campo
        self.__start = None         #nodo di start
        self.__goal = None          #nodo di end
        
    def init_start(self, row, col):
        if self.__matrix[row][col] == " ":  #se la posizione non è #, cioè è valida

            #impongo la posizione giusta del nodo se ho inserito val negativi
            row = len(self.__matrix)+row if row < 0 else row
            col = len(self.__matrix[0])+col if col < 0 else col
            
            #creo il nodo __me
            self.__start = Node(row,col)   
            print("<init_start>  posizione START settata: (", row, col, ")")
            
        else:
            print("<init_start>  posizione START non valida")
                
        
    #stessa cosa di init_start, però metto la G di goal
    def init_goal(self, row, col):
        if self.__matrix[row][col] == " ":

            #impongo la posizione giusta del nodo se ho inserito val negativi
            row = len(self.__matrix)+row if row < 0 else row
            col = len(self.__matrix[0])+col if col < 0 else col
            #creo il nodo goal
            self.__goal = Node(row,col)
            print("<init_goal>  posizione GOAL settata: (", row, col, ")")

        else:
            print("<init_goal>  posizione GOAL non valida")
            
    
    #fa bfs(dal file bfs_func.py) che esegue e stampa direttamente il risultato
    def BFS(self):
        #se non ho inizializzato le posizioni di start e goal ritorno None
        if self.__goal == None or self.__start == None:
            print("<BFS> non hai inserito il goal o lo start")
    
        else:
            bfs(self.__matrix, self.__start, self.__goal)
     
                
    #fa bfs(dal file bfs_func.py) che esegue e stampa direttamente il risultato
    def DFS(self):
        #se non ho inizializzato le posizioni di start e goal ritorno None
        if self.__goal == None or self.__start == None:
            print("<BFS> non hai inserito il goal o lo start")
    
        else:
            dfs(self.__matrix, self.__start, self.__goal)
                
    
    

            
            
