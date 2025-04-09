##############################################################################
# Author: Paolo Ascia                                                        
# Date: February 2025                                                        
##############################################################################   

##############################################################################
# imports
##########
import json
import os  
from importlib.resources import files

def open_json_keyword(keyword : str):
    '''
    Function to open the JSON file containing the keyword information.

    Parameters
    ----------
    keyword : str
        Name of keyword to load from JSON..

    Returns
    -------
    key_dict : dict
        Dictionary with information about keyword from JSON.

    '''
    
    # Check input type
    if not isinstance(keyword, str):
        raise TypeError(f"Expected str, passed {type(keyword).__name__}")
    
    # Split keywords to identify correct folder
    keyword_class = keyword.split("_")[0] 
    
    # Path of the keyword  
    rel_path = os.path.join("KEYWORDS", keyword_class, keyword + '.json')  
    file_path = files("PrePyna").joinpath(rel_path)
    # file_path = os.path.join(os.getcwd(), rel_path)
    
    # If keyword exists
    try:
        
        # Open JSON file 
        with open(file_path, "r") as f:
            key_dict = json.load(f)
    
        # and return the dictionary loaded from the JSON
        return key_dict
    
    except:
        raise FileNotFoundError(f"{keyword} is still not supported. See documentation to add the keyword to the library.\n"
                                 " Please, then submit your JSON file to the repository to expand the number of supported keywords.")

            
def check_card_requirements(cards: list, requirements):
    '''
    Function to check if requirements to include a card are met

    Parameters
    ----------
    cards : list
        List of cards.
    requirements : requirement obj
        Object containing requirements to check.

    Returns
    -------
    True if requirements are met
    False if requirements are NOT met
    
    '''
    
    # if card is always present return true
    if requirements.always:
        return True
    
    else: 
        # else iterate throuh the variables of the previous cards to check if requirements are met
        for card in cards:
            for var in card.variables:
                if var.name == requirements.variable and var.value == requirements.value:
                    if check_card_requirements(cards, card.requirements):
                        return True
        # If the function is not stopped earlier -> requirements are not met
        return False
    
if __name__ == "__main__":
    keyword = "TEST_SCALAR"
    tmp = open_json_keyword(keyword)
