def get_formations():
    """
    Returns all predefined formations.

    Return:
        A dictionary with all formations.
    """

    formations = {}
    
    #Einfach neue Formationen hinzufügen.
    formations['F532'] = [[-25,20], [-30,10], [-30,0], [-30,-10], [-25,-20], [-20,5], [-20,-5], [-10,5], [-5,0], [-10,-5]]
    formations['F532F'] = [[-25,20], [-30,10], [-30,0], [-30,-10], [-25,-20], [-20,5], [-20,-5], [-10,5], [-10,0], [-10,-5]]
    formations['F442R']=[[-25,15], [-30,5], [-30,-5], [-25,-15], [-15,15], [-20,0], [-10,0], [-15,-15], [-10,5], [-10,-5]]

    return formations