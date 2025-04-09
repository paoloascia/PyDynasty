##############################################################################
# Author: Paolo Ascia                                                        
# Date: February 2025                                                        
##############################################################################      

##############################################################################
# imports
##########
from PyDynasty.keyword import keyword
from PyDynasty.comment import comment
from PyDynasty.utilities import check_card_requirements

# from keyword_t import keyword
# from comment import comment
# from utilities import check_card_requirements
      
class deck():
    
    def __init__(self, name: str):
        '''
        Class to contain all information regarding a LS-Dyna deck.

        Parameters
        ----------
        name : str
            Name of the LS-Dyna deck.

        '''
        
        # Check input format
        if not isinstance(name, str):
            raise TypeError(f"Expected str, {type(name).__name__} passed.")
        
        self.name: str = name           # Save LS-Dyna deck
        
        self.keywords_list: list = []   # Container of all keywords
        
        return
    
    def __repr__(self):
        # Represenation of keyword
        
        return (f"LS-Deck name: {self.name} \n"
                f"Number of keywords: {len(self.keywords_list)} \n")
    
    def __str__(self):
        # Printing sequence
        
        # If there are no keywords/comments in the deck, do not print deck, warn user
        if len(self.keywords_list) == 0:
            return "The deck is empty!"
        
        # Else: iterate and join all keywords and comments.
        deck_txt = "\n".join(f"{key}" for key in self.keywords_list)
        
        # Append EOF and return printed deck
        return f"{deck_txt}\n*END\n"
    
    def add_keyword(self, keyword_name : str, **kwargs):
        '''
        Function to add a keyword to the LS-Dyna deck.

        Parameters
        ----------
        keyword_name : str
            Name of the keyword to add.
        **kwargs : variables to edit.

        '''
        
        # Check input format
        if not isinstance(keyword_name, str):
            raise TypeError(f"Expected str, {type(keyword_name).__name__} passed.")

        # Append keyword to deck
        self.keywords_list.append(keyword(keyword_name, **kwargs))
        
        return
    
    def remove_keyword(self, keyword_name : str, id_: (int, None) = None):
        '''
        Function to remove a keyword from the LS-Dyna deck.

        Parameters
        ----------
        keyword_name : str
            Name of keyword to delete.
        id_ : int, optional
            ID of the keyword.

        '''
        
        # Check inputs type
        if not isinstance(keyword_name, str):
            raise TypeError(f"Expected str for keyword_name, {type(keyword_name).__name__} passed.")
        if not isinstance(id_, (int, None)):
            raise TypeError(f"Expected int for id_, {type(id_).__name__} passed.")
        
        # Find location of keyword to remove
        indx, _ = self.find_keyword(keyword_name, id_)
        
        # Remove keyword from list
        del self.keywords_list[indx]
        
        return
    
    def read_keyword(self, keyword_text : str):
        '''
        Function to read keyword from text

        Parameters
        ----------
        keyword_text : str
            Text with keyword.

        Raises
        ------
        TypeError
            DESCRIPTION.

        Returns
        -------
        key_entry : keyword object
            Keyword object.
        comments : comment object, None
            Possible comments appended to the keyword. If no comment was appended, returns None

        '''
        
        # Check input type
        if not isinstance(keyword_text, str):
            raise TypeError(f"Expected str, {type(keyword_text).__name__} passed.")
        
        # Split text into lines and remove new line characters
        keyword_text = [line.replace("\n", "") for line in keyword_text.splitlines()]
        
        # Extract and remove keyword name
        keyword_name = keyword_text[0]
        keyword_text = keyword_text[1:]
        
        # Load the information from keyword
        key_entry = keyword(keyword_name)
        
        # iterate through cards and read them from lines
        for cd in key_entry.cards:
            
            # If requirements are not met, continue to next card 
            if not check_card_requirements(cards = key_entry.cards, requirements = cd.requirements):
                continue
            
            # Skip & remove comment lines
            while keyword_text[0][0] == "$":
                keyword_text = keyword_text[1:]
            
            # Read variables
            # if card is scalar, read one line
            if cd.singleORcolumn:
                
                # Read and parse one line            
                char_i = 0      # character counter to parse line
                for var in cd.variables:
                    # Try reading characters from line
                    try:
                        var.value = var.type(keyword_text[0][char_i:char_i + var.field_width])
                        if var.id:
                            key_entry.id = var.value
                        char_i += var.field_width
                    
                    # If fails, keep standard value -> no more text on the line
                    except:
                        continue
                
                # Remove line read
                keyword_text = keyword_text[1:]
                if len(keyword_text) == 0:
                    break
            
            # else, is a vector -> read lines until comment
            else:
                
                # Reset std values
                for var in cd.variables:
                    var.value = []
                    
                # Iterate until comment is met
                while keyword_text[0][0] != "$":
                    char_i = 0      # character counter to parse line
                    for var in cd.variables:
                        try:
                            # Parse line
                            var.value.append(var.type(keyword_text[0][char_i:char_i + var.field_width]))
                            char_i += var.field_width
                        
                        # If fails, keep standard value 
                        except:
                            char_i += var.field_width
                            continue
                    
                    # Remove line read
                    keyword_text = keyword_text[1:]
                    if len(keyword_text) == 0:
                        break
                
                # Find maximum vector length among read values
                max_len = 0
                for var in cd.variables:
                    if len(var.value) > max_len:
                        max_len = len(var.value)
                        
                # Check that length is consistent among all vectors, if not add empty rows
                for var in cd.variables:
                    while len(var.value) < max_len:
                        var.value.append([])
                
        # If lines remaining after reading all keywords, mark them as comment
        if len(keyword_text) > 0:
            comments = "\n".join(f"{line}" for line in keyword_text)
            comments = comment(comments)
        else:
            comments = None
            
        return key_entry, comments
    
    def read_deck(self, filename : str):
        '''
        Function to read a LS-Dyna deck from file.

        Parameters
        ----------
        filename : str
            File name to read.

        '''
        
        # Check input type
        if not isinstance(filename, str):
            raise TypeError(f"Expected str, {type(filename).__name__} passed.")
            
        # Check file is a LS-Dyna file
        if not filename.lower().endswith(('.k', '.key', '.dyn')):
            raise TypeError("Expected LS-Dyna input file. Accepted formats: .k, .key, .dyn")
            
        # open and read keyfile
        with open(filename, 'r') as file:
            ls_deck_txt = file.read()
            
        # Parse the content and separate the text of each keyword into a list entry
        ls_deck_txt = ls_deck_txt.split('\n*')
        
        # Iterate through the split text deck
        for entry in ls_deck_txt:
            
            # If end of document is reached, end reading document
            if "END" in entry:
                break
            
            # Append comment if entry starts with "$"
            if entry[0] == "$":
                self.keywords_list.append(comment(entry))
            # Otherwise append keyword and ...
            else:
                key_entry, comments = self.read_keyword(entry)
                self.keywords_list.append(key_entry)
                
                # ... and possible comments 
                if not comments is None:
                    self.keywords_list.append(comments)
            
        return
    
    def find_keyword(self, keyword_name: str, id_: (int, None) = None):
        '''
        Function to find and retrieve a keyword in the deck.

        Parameters
        ----------
        keyword_name : str
            Name of keyword to find.
        id_ : int, optional
            ID of the keyword.

        Returns
        -------
        index : int
            Index in the deck list.
        key : keyword object
            Keyword object.

        '''
        
        # Iterate through the list of keywords and comments
        for index, key in enumerate(self.keywords_list):
            
            # Check if item of list is a keyword
            if isinstance(key, keyword):
                
                # If so, check if the name and ID of the keyword
                if key.name == keyword_name and key.id == id_:
                    
                    # If match, return indexa and key
                    return index, key
        
        # If not found, return error -> keyword not in LS-Deck
        raise TypeError(f"{keyword_name} (id: {id_}) not in LS-Dyna deck {self.name}")
        
        return
    
    def update_ids(self):
        '''
        Function to update all IDs of the keywords

        '''
        
        # Iterate through deck list
        for key in self.keywords_list:
            
            # Check if entry is a keyword
            if isinstance(key, keyword):
                # If so, update the ID
                key.update_id()
                
        return
    
    def edit_keyword(self, keyword_name: str, id_: (int, None) = None, **kwargs):
        '''
        Function to edit a keyword in LS-Deck.

        Parameters
        ----------
        keyword_name : str
            Name of keyword to edit.
        id_ : int, optional
            ID of the keyword.
        **kwargs : variables to edit.

        '''
        
        # Find the keyword to update
        idx, _ = self.find_keyword(keyword_name, id_)
        
        # edit keyword
        self.keywords_list[idx].edit(**kwargs)
        
        return
    
    def retrieve_variable_from_keyword(self, keyword_name: str, id_: (int, None) = None, variable_name : str = " "):
        '''
        Function to retrieve the value of a variable from a keyword.

        Parameters
        ----------
        keyword_name : str
            Name of the keyword containing the variable.
        id_ : int, optional
            ID of the keyword.
        variable_name : str
            Name of the variable.

        Returns
        -------
        value : str, int, float, list
            Value of the variable requested.

        '''
        
        # Find keyword
        idx, _ = self.find_keyword(keyword_name, id_)
        
        # Retrieve variable
        return self.keywords_list[idx].retrieve_variable(variable_name)
    
# if __name__ == "__main__":
#     ls_d = deck("test")
#     ls_d.read_deck("TEST_DECK_INPUT.k")