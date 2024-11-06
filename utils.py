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


