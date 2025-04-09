##############################################################################
# Author: Paolo Ascia                                                        
# Date: February 2025                                                        
##############################################################################

##############################################################################
# imports
##########

class comment():
    '''Class to contain all information regarding a comment.'''
    
    def __init__(self, text : str):
        '''
        Class to contain all information regarding a comment.

        Parameters
        ----------
        text : str
            Comment.

        '''
        # Check input format
        if not isinstance(text, str):
            raise TypeError(f"Expected str, {type(text).__name__} passed.")
            
        # Parse text into single lines
        self.lines = [line.replace("\n", "") for line in text.splitlines()]
        
        # If first character is "$" -> remove it
        self.lines = [line[1:] if line.startswith("$") else line for line in self.lines]
        
        return
    
    def __repr__(self):
        # Represenation of keyword
        
        return "LS-Dyna comment"
    
    def __str__(self):
        # Printing sequence
        
        # Join all lines and add comment character
        return "\n".join(f"${line}" for line in self.lines)
