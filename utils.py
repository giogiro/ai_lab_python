from node_class import Node
from colorama import init, Fore, Back, Style

def crea_path(node, start, goal):  #percorro il percorso al contrario, da goal->goal.padre->padre->padre->padre...->None
    path = []
    curr = node
    while curr != None:
        if(curr != start and curr != goal):   #se il nodo è il goal o start non lo aggiungo
            path.append(curr)
        curr = curr.padre
    
    path.reverse()   #e alla fine inverto 
    return path
        
        
#actions ritorna una lista di liste ( [row1,col1], [row2, col2], ... ) queste ultime sono
#posizioni valide per fare la mossa
def actions(matrix, node):
    possible_actions = []
    if(node.row > 0  and matrix[node.row - 1][node.col] != "#"): #provo nodo sopra
        possible_actions.append([node.row-1, node.col])
    if(node.row < len(matrix)-1 and matrix[node.row + 1][node.col] != "#"):   #provo nodo sotto
        possible_actions.append([node.row+1, node.col])
    if(node.col > 0 and matrix[node.row][node.col-1] != "#"):    #provo nodo a sx
        possible_actions.append([node.row, node.col-1])
    if(node.col < len(matrix[0])-1 and matrix[node.row][node.col+1] != "#"):  #provo nodo a dx
        possible_actions.append([node.row, node.col+1])
    
    return possible_actions

#stampa UNA COPIA della matrice, alla quale aggiungo S, G, nodi visitati e percorso
def stampa_risultato(matrix, start, goal, path, visited):
    mod_matrix = matrix
    #metto S e G nelle posizioni di start e goal
    mod_matrix[start.row][start.col] = Fore.RED + "S" + Fore.BLUE #coloro S di rosso
    mod_matrix[goal.row][goal.col] = Fore.RED + "G" + Fore.BLUE #coloro G di rosso
    
    if(path != []):  #se ho trovato il percorso
        for node in path:
            mod_matrix[node.row][node.col] =  Style.RESET_ALL + "+" + Fore.BLUE    #se ho trovato il path, lo disegno sulla matrixce
            # e li coloro di blu
    if(visited):     #se ho visitato dei nodi
            for node in visited:
                #"disegno" le posizioni visitate solo se non sono nodi di goal, start, oppure se non ci ho gia messo + (nodi del path)
                if node != goal and node != start and mod_matrix[node.row][node.col] != Style.RESET_ALL + "+" + Fore.BLUE:
                    mod_matrix[node.row][node.col] =  Fore.YELLOW + "." + Fore.BLUE    #se ho visitato nodi, li disegno
    
    for row in mod_matrix:  #stampo matrice riga per  riga
        print( Fore.BLUE + "".join(row) + Style.RESET_ALL)
    
    Style.RESET_ALL
    
    print("Nodi visitati:", len(visited))
    print("lunghezza path:", len(path))
