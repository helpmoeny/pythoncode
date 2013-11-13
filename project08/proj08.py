import cards

def setup():
    """
    paramaters: None (deck can be created within this function)
    returns:
    - a foundation (list of 4 empty lists)
    - cell (list of 4 empty lists)
    - a tableau (a list of 8 lists, the dealt cards)
    """
    foundation = [[],[],[],[]]
    cell = [[],[],[],[]]  
    tableau = [[],[],[],[],[],[],[],[]]
    my_deck = cards.Deck()
    my_deck.shuffle()
    for i in range(4):
        for k in range(7):
            tableau[i].append(my_deck.deal())
    for j in range(4,8):
        for l in range(6):
            tableau[j].append(my_deck.deal())

    return foundation,tableau,cell


def move_to_foundation(tableau,foundation,t_col,f_col):
    '''
    parameters: a tableau, a foundation, column of tableau, column of foundation
    returns: Boolean (True if the move is valid, False otherwise)
    moves a card at the end of a column of tableau to a column of foundation
    This function can also be used to move a card from cell to foundation
    '''
    valid=False

    t_col=t_col-1
    f_col=f_col-1
    
    if len(tableau[t_col])!=0:
        tableau_card=tableau[t_col].pop()
        tableau_rank=tableau_card.get_rank()
        tableau_suit=tableau_card.get_suit()

        if len(foundation[f_col])==0:
            if tableau_rank==1:
                foundation[f_col].append(tableau_card)
                valid=True
            else:
                tableau[t_col].append(tableau_card)
        else:
            foundation_card=foundation[f_col][-1]
            foundation_rank=foundation_card.get_rank()
            foundation_suit=foundation_card.get_suit()

            if foundation_rank==tableau_rank-1: #Iterating through rank
                if foundation_suit==tableau_suit:
                    foundation[f_col].append(tableau_card)
                    valid=True
                else:
                    tableau[t_col].append(tableau_card)
            else:
                tableau[t_col].append(tableau_card)
    return valid

def move_to_cell(tableau,cell,t_col,c_col):
    '''
    parameters: a tableau, a cell, column of tableau, column of cell
    returns: Boolean (True if the move is valid, False otherwise)
    moves a card at the end of a column of tableau to a cell
    '''
    valid=False
    t_col=int(t_col)-1
    c_col=int(c_col)-1
    if len(tableau[t_col])!=0:
        tableau_card=tableau[t_col].pop()
    if len(cell[c_col])==0:
        cell[c_col].append(tableau_card)
        valid=True
    else:
        tableau_card.append(tableau[t_col])
    return valid
    

def move_to_tableau(tableau,cell,t_col,c_col):
    '''
    parameters: a tableau, a cell, column of tableau, a cell
    returns: Boolean (True if the move is valid, False otherwise)
    moves a card in the cell to a column of tableau
    remember to check validity of move
    '''
    valid=False
    
    t_col=t_col-1
    c_col=c_col-1
    
    if len(cell[c_col])!=0:#checks to see if the cell's list at current column is empty
        cell_card=cell[c_col].pop()
        cell_card_rank=cell_card.get_rank()
        cell_card_suite=cell_card.get_suit()

        if len(tableau[t_col])==0:#checks to see if tableau's selected column is empty
            tableau[t_col].append(cell_card)
            valid=True
        else:
            tableau_card=tableau[t_col][-1]#
            tableau_rank=tableau_card.get_rank()
            tableau_suit=tableau_card.get_suit()

            if tableau_rank==call_card_rank+1: #Iterating through rank
                if (tableau_suit==1 or tableau_suit==4) and (cell_card_suite==2 or cell_card_suite==3):
                    tableau[t_col].append(cell_card)
                    valid=True
                elif (tableau_suit==2 or tableau_suit==3) and (cell_card_suite==1 or cell_card_suite==4):
                    tableau[t_col].append(cell_card)
                    valid=True
                else:
                    tableau[t_col].append(cell_card)
            else:
                tableau[t_col].append(cell_card)
    return valid


def is_winner(foundation):
    '''
    parameters: a foundation
    return: Boolean
    '''
    total_cards=0
    for i in foundation:
        for j in i:
            total_cards+=1
    if total_cards==52:
        return True
    else:
        return False


def move_in_tableau(tableau,t_col_source,t_col_dest):
    '''
    parameters: a tableau, the source tableau column and the destination tableau column
    returns: Boolean
    move card from one tableau column to another
    remember to check validity of move
    '''
    valid=False
    
    t_col_source=t_col_source-1
    t_col_dest=t_col_dest-1
    
    if len(tableau[t_col_source])!=0:#checks if tableau's first/start column's list is empty
        tableau_card1=tableau[t_col_source].pop()
        tableau_rank1=tableau_card1.get_rank()
        tableau_suit1=tableau_card1.get_suit()

        if len(tableau[t_col_dest])==0:#checks if tableau's second/end column's list is empty
            tableau[t_col_dest].append(tableau_card1)
        else:
            tableau_card2=tableau[t_col_dest][-1]
            tableau_rank2=tableau_card2.get_rank()
            tableau_suit2=tableau_card2.get_suit()

            if tableau_rank2==tableau_rank1+1: #Iterating through rank
                if (tableau_suit1==1 or tableau_suit1==4) and (tableau_suit2==2 or tableau_suit2==3):
                    tableau[t_col_dest].append(tableau_card1)
                    valid=True
                elif (tableau_suit1==2 or tableau_suit1==3) and (tableau_suit2==1 or tableau_suit2==4):
                    tableau[t_col_dest].append(tableau_card1)
                    valid=True
                else:
                    tableau[t_col_source].append(tableau_card1)
            else:
                tableau[t_col_source].append(tableau_card1)
    return valid
    

def print_game(foundation, tableau,cell):
    """
    parameters: a tableau, a foundation and a cell
    returns: Nothing
    prints the game, i.e, print all the info user can see.
    Includes:
        a) print tableau  
        b) print foundation ( can print the top card only)
        c) print cells

    """
    print()
    print("                 Cells:                              Foundation:")
    # print cell and foundation labels in one line
    for i in range(4):
        print('{:8d}'.format(i+1), end = '')
    print('    ', end = '')
    for i in range(4):
        print('{:8d}'.format(i+1), end = '')
    print()  # carriage return at the end of the line

    # print cell and foundation cards in one line; foundation is only top card
    for c in cell:
        # print if there is a card there; if not, exception prints spaces.
        try:
            print('{:>8s}'.format(c[0]), end = '')
        except IndexError:
            print('{:8s}'.format(''), end = '')
            
    print('    ', end = '')
    for stack in foundation:
        # print if there is a card there; if not, exception prints spaces.
        try:
            print('{:>8s}'.format(stack[-1]), end = '')
        except IndexError:
            print('{:8s}'.format(''), end = '')

    print()  # carriage return at the end of the line
    print('----------')

    print("Tableau")
    for i in range(len(tableau)):  # print tableau headers
        print('{:8d}'.format(i + 1), end = '')
    print()  # carriage return at the end of the line

    # Find the length of the longest stack
    max_length = max([len(stack) for stack in tableau])

    # print tableau stacks row by row
    for i in range(max_length):  # for each row
        print(' '*7, end = '')  # indent each row
        for stack in tableau:
            # print if there is a card there; if not, exception prints spaces.
            try:
                print('{:8s}'.format(stack[i]), end = '')
            except IndexError:
                print('{:8s}'.format(''), end = '')
        print()  # carriage return at the end of the line
    print('----------')

def print_rules():
    '''
    parameters: none
    returns: nothing
    prints the rules
    '''
    print("Rules of FreeCell")

    print("Goal")
    print("\tMove all the cards to the Foundations")

    print("Foundation")
    print("\tBuilt up by rank and by suit from Ace to King")

    print("Tableau")
    print("\tBuilt down by rank and by alternating color")
    print("\tThe bottom card of any column may be moved")
    print("\tAn empty spot may be filled with any card ")

    print("Cell")
    print("\tCan only contain 1 card")
    print("\tThe card may be moved")

def show_help():
    '''
    parameters: none
    returns: nothing
    prints the supported commands
    '''
    print("Responses are: ")
    print("\t t2f #T #F - move from Tableau to Foundation")
    print("\t t2t #T1 #T2 - move card from one Tableau column to another")
    print("\t t2c #T #C - move from Tableau to Cell")
    print("\t c2t #C #T - move from Cell to Tableau")
    print("\t c2f #C #F - move from Cell to Foundation")
    print("\t 'h' for help")
    print("\t 'q' to quit")
    
    
def play():
    ''' 
    Main program. Does error checking on the user input. 
    '''
    print_rules()
    foundation, tableau, cell = setup() 
       
    show_help()
    while True:
        # Uncomment this next line. It is commented out because setup doesn't do anything so printing doesn't work.
        print_game(foundation, tableau, cell)
        response = input("Command (type 'h' for help): ")
        response = response.strip()
        response_list = response.split()
        if len(response_list) > 0:
            try:
                r = response_list[0]
                start=int(response_list[1])
                end=int(response_list[2])
                if r == 't2f':
                    t_col=start#keep in mind what list we are in!
                    f_col=end
                    if t_col<1 or t_col>8 or f_col<1 or f_col>4:
                        valid=False
                    else:
                        valid=move_to_foundation(tableau,foundation,t_col,f_col)#call function and set to valid
                    if valid==False:
                        print("illegal move")
                elif r == 't2t':
                    t_col_source=start
                    t_col_dest=end
                    if t_col_source<1 or t_col_source>8 or t_col_dest<1 or t_col_dest>8:#validates input parameters
                        valid=False
                    else:
                        valid=move_in_tableau(tableau,t_col_source,t_col_dest)
                    if valid==False:
                        print("illegal move")
                elif r == 't2c':
                    t_col=start
                    c_col=end
                    if t_col<1 or t_col>8 or c_col<1 or c_col>4:
                        valid=False
                    else:
                        valid=move_to_cell(tableau,cell,t_col,c_col)
                    if valid==False:
                        print("illegal move")
                elif r == 'c2t':
                    c_col=start
                    t_col=end
                    if c_col<1 or c_col>4 or t_col<1 or t_col>8:
                        valid=False
                    else:
                        valid=move_to_tableau(tableau,cell,t_col,c_col)
                    if valid==False:
                        print("illegal move")
                elif r == 'c2f':
                    c_col=start
                    f_col=end
                    if c_col<1 or c_col>4 or f_col<1 or f_col>4:
                        valid=False
                    else:
                        valid=move_to_foundation(cell,foundation,c_col,f_col)
                    if valid==False:
                        print("illegal move")                        
                elif r == 'q':
                    break
                elif r == 'h':
                    show_help()
                else:
                    print('Unknown command:',r)
            except:
                print("invalid Input")
        else:
            print("Unknown Command:",response)
        if is_winner(foundation):
            print("WINNER!!!!!!!!!!")
            break
    print('Thanks for playing')

play()
