##############################################################################
# Author: Paolo Ascia                                                        
# Date: February 2025                                                        
##############################################################################     

##############################################################################
# imports
##########
from PyDynasty.card import card
from PyDynasty.utilities import open_json_keyword
from PyDynasty.utilities import check_card_requirements
# from card import card
# from utilities import open_json_keyword
# from utilities import check_card_requirements

class keyword():
   
    def __init__(self, keyword_name, **kwargs):
        '''
        Class to contain all information regarding a keyword.

        Parameters
        ----------
        keyword_name : str
            Name of the keyword.
        **kwargs : (str, int, float)
            Variables to set.

        '''
        
        # Check input format
        if not isinstance(keyword_name, str):
            raise TypeError(f"Expected str, {type(keyword_name).__name__} passed.")
        
        # Opening json dictionary
        key_dict = open_json_keyword(keyword_name)
            
        # parse json file to keyword metadata
        self.name: str = key_dict['name']   # Keyword name
        self.id: int = key_dict['id']       # Keyword unique ID
        
        # Load all possible cards
        self.cards: list = []   # Initiate list to contain all possible cards
        
        # iterate through cards in dictionarz
        for cd in key_dict['cards']:
            
            # Load and append card
            self.cards.append(card(cd))
            
        # Edit card with values passed
        self.edit(**kwargs)
                
        return
            
    def __repr__(self):
        # Represenation of keyword
        
        # Join all visible cards' names into one list to print
        card_list = ", ".join(cd.name for cd in self.cards if check_card_requirements(self.cards, cd.requirements))
        
        return (f"\n"
                f"Name: {self.name} \n"
                f"Id: {self.id} \n"
                f"Cards: {card_list} \n")
    
    def __str__(self):
        # Printing sequence
        
        # Retrieve name of the keyword and add "*" for keyword output
        name = f"*{self.name}"
        
        # Print all cards that fulfill the visibility requirements
        cards = "\n".join(f"{cd}" for cd in self.cards if check_card_requirements(self.cards, cd.requirements))
        
        # Return the keyword ready to be parsed by LS-Dyna
        return f"{name}\n{cards}"
    
    def retrieve_variable(self, variable_name: str):
        '''
        Function to find and retireve the value of a variable.

        Parameters
        ----------
        variable_name : str
            Name of variable to be retrieved.

        '''
        
        # Check input is correct, otherwise raise error
        if not isinstance(variable_name, str):
            raise TypeError(f"Expected str, {type(variable_name).__name__} passed.")
        
        # Iterate through all cards and their variables to find the request one
        for cd in self.cards:
             for vr in cd.variables:
                 # If variable is found, return its value
                 if vr.name == variable_name:
                     return vr.value
        # If variable is not found, raise error
        raise TypeError(f"{variable_name} not a variable of keyword {self.name}.")
        return
    
    def find_variable(self, variable_name : str):
        '''
        Function to locate a variable inside the keyword

        Parameters
        ----------
        variable_name : str
            Name of variable to be search.

        Returns
        -------
        id_card : int
            ID of the card containing variable (location in the card list).
        
        name_card : str
            Name of the card containing variable (location in the variable list).
            
        id_variable : int
            ID of the variable inside the card.

        '''
        
        # Check input is correct, otherwise raise error
        if not isinstance(variable_name, str):
            raise TypeError(f"Expected str, {variable_name.type.__name__} passed.")
            
        # Iterate through all cards and their variables to find the request one
        for id_card, cd in enumerate(self.cards):
             for id_var, vr in enumerate(cd.variables):
                 # If found, return the card id (location in the card list), name of the card, and variable id (location in the variable list)
                 if vr.name == variable_name:
                     return id_card, cd.name, id_var
        # If variable is not found, raise error
        raise TypeError(f"{variable_name} not a variable of keyword {self.name}.")
        return
    
    def update_id(self):
        '''Function to update the id of the keyword.'''
        
        # If keyword does not have an ID, stop update
        if self.id is None:
            return
        
        # Iterate through all cards looking for a variable flagged as ID
        for cd in self.cards:
            for var in cd.variables:
                # If variable is flagged as ID
                if var.id:
                    # Update keyword ID
                    self.id = var.value
                    # and finish
                    return
        # No id to update -> finish
        return
    
    def edit(self, **kwargs):
        '''Function to edit the variables passed as input.'''
        
        # Iterate the variables to edit
        for arg, val in kwargs.items():
            
            # Identify where is the variable located
            id_card, _, id_var = self.find_variable(arg)
            
            # Different treatment for scalars and ...
            if self.cards[id_card].singleORcolumn:
                # Check if value passed is consistent with variable type
                if isinstance(val, self.cards[id_card].variables[id_var].type):
                    # If so, change value
                    self.cards[id_card].variables[id_var].value = val
                else:
                    # Else raise error
                    raise TypeError(f"Variable {arg} expects {self.cards[id_card].variables[id_var].type.__name__}, {type(val).__name__} was passed.")
            # ... and vector
            else:
                # Check that a list is passed, and that all values in list are of correct type
                if isinstance(val, list) and all(isinstance(item, self.cards[id_card].variables[id_var].type) for item in val):
                    # If so, change the value
                    self.cards[id_card].variables[id_var].value = val
                                
                    # Check that all entries of this card all long the same
                    # Find maximum vector length among read values
                    max_len = 0
                    for vr in self.cards[id_card].variables:
                        if len(vr.value) > max_len:
                            max_len = len(vr.value)
                                        
                    # Check that length is consistent among all vectors, if not add empty rows
                    for vr in self.cards[id_card].variables:
                        while len(vr.value) < max_len:
                            vr.value.append([])
                # If not list -> raise list error
                elif not isinstance(val, list):
                    raise TypeError(f"Variable {arg} expects List, {type(val).__name__} was passed.")
                # If wrong type -> raise type error
                else:
                    raise TypeError(f"Variable {arg} expects {self.cards[id_card].variables[id_var].type.__name__}.")
        return
