##############################################################################
# Author: Paolo Ascia                                                        
# Date: February 2025                                                        
##############################################################################        

##############################################################################
# imports
##########
from PyDynasty.variable import variable
# from variable import variable

class card_requirement():
    
    def __init__(self, always : bool = True, variable : str = " ", value = None):
        '''
        Class containing the requirements to include a card or not.

        Parameters
        ----------
        always : bool, optional
            True if card is always active; False if card is active under conditions (specify variable and value). The default is True.
        variable : str, optional
            Variable to be checked if condition is present.
        value : (str, int, float), optional
            Value variable must fullfill.

        '''
        
        self.always: bool = always
        self.variable: str = variable
        self.value: int = value
        
        return
    
class card():
    
    def __init__(self, card_dict):
        '''
        Class to contain all information regarding a card.        

        Parameters
        ----------
        card_dict : dict
            Dictionary containing information from JSON.

        '''
        
        # Read metadata
        self.name: str = card_dict['name']      # Name of the card
        self.singleORcolumn: bool = card_dict['singleORcolumn']     # Is this card a vector or a scalar?
        
        # Read requirements
        self.requirements = card_requirement(always = card_dict['requirements']['always'],
                                             variable = card_dict['requirements']['variable'],
                                             value = card_dict['requirements']['value'])
        
        # Read variables
        self.variables: list = []       # Initiate list to contain all variables
        
        # Iterate through the variables of the given card
        for vd in card_dict['variables']:
            self.variables.append(variable(vd))
            
        return
            
    def __repr__(self):
        # Represenation of card
        
        # Retrieve information regarding the requirements
        # If card is always present, print "Always"
        if self.requirements.always:
            req = "Always"
        # Otherwise print the variable and value required
        else:
            req = f"if {self.requirements.variable} == {self.requirements.value}"
            
        # Return card representation
        return (f"\n"
                f"Name: {self.name} \n"
                f"Is scalar: {self.singleORcolumn} \n"
                f"Active: {req} \n")
    
    def __str__(self):
        # Printing sequence
        
        # Treat differently if variable is scalar or ...
        if self.singleORcolumn:
            
            names = []      # Initialize list for the names
            values = []     # Initialize list for the values
            
            # Iterate through the variables
            for var in self.variables:
                
                # If the variable is float:
                if var.type is float:
                    
                    # Check that when printed the it is not longer than the field width
                    if (abs(var.value) >= 10 ** (var.field_width-1) or 
                        (abs(var.value) <= 10 ** (5 - var.field_width) and var.value != 0)):
                        
                        # If so switch to scientific notation
                        if var.value < 0:
                            # If negative value, account for the "-" sign
                            names.append(f"{var.name}"[:var.field_width].rjust(var.field_width))
                            values.append(f"{var.value:.{var.field_width - 7}E}".rjust(var.field_width))
                        else:
                            # Else just account for scientific notation
                            names.append(f"{var.name}"[:var.field_width].rjust(var.field_width))
                            values.append(f"{var.value:.{var.field_width - 6}E}".rjust(var.field_width))
                            
                    else:
                        # Else print float without scientific notation (remove extra zeros)
                        if var.value < 0:
                            # If negative value, account for the "-" sign 
                            names.append(f"{var.name}"[:var.field_width].rjust(var.field_width))
                            values.append(f"{var.value:.{var.field_width - 2}g}".rjust(var.field_width))
                        else:
                            # Else account only for the decimal point
                            names.append(f"{var.name}"[:var.field_width].rjust(var.field_width))
                            values.append(f"{var.value:.{var.field_width - 1}g}".rjust(var.field_width))
        
                # If the variable is int:
                if var.type is int:
                    
                    # Check length
                    if len(f"{var.value}") > var.field_width:
                        # If too many digits, raise error
                        raise TypeError(f"{var.name} exceeds the field width of {var.field_width} characters.")
                    else:
                        # Else print as it is
                        names.append(f"{var.name}"[:var.field_width].rjust(var.field_width))
                        values.append(f"{var.value}"[:var.field_width].rjust(var.field_width))
                    
                # If the variable is str -> print as it is and truncate to maximum length (str generally can be truncated)
                if var.type is str:
                    names.append(f"{var.name}"[:var.field_width].rjust(var.field_width))
                    values.append(f"{var.value}"[:var.field_width].rjust(var.field_width))
            
            # Generate string of names and variables to return
            names = "".join(f"{name}" for name in names)
            names = f"$#{names[2:]}"
            values = "".join(f"{value}" for value in values)
        
        # ... or vector
        else:
            
            # Extract the names of the variables
            names = "".join(f"{var.name}"[:var.field_width].rjust(var.field_width) for var in self.variables)
            names = f"$#{names[2:]}"
            
            # Combine all values of variable in single list to iterate through the rows
            values_tmp = [var.value for var in self.variables]
            
            values = []     # Initiate a list containing all values to print
            
            # Iterate through the rows
            for row in zip(*values_tmp):
                
                line = []   # Container of values in a single line
                
                # Iterate the values in a single row
                for i, val in enumerate(row):
                    
                    # If vector is made of empty values append spaces to fill the variable's space
                    if not val and not val == 0:
                        line.append("".join(" " for _ in range(self.variables[i].field_width)))
                        
                        # If the variable is float:
                    elif self.variables[i].type is float:
                            
                        # Check that when printed the it is not longer than the field width
                        if (abs(val) >= 10 ** (self.variables[i].field_width-1) or 
                            (abs(val) <= 10 ** (5 - self.variables[i].field_width) and val != 0)):
                                
                            # If so switch to scientific notation
                            if val < 0:
                                # If negative value, account for the "-" sign
                                line.append(f"{val:.{self.variables[i].field_width - 7}E}".rjust(self.variables[i].field_width))
                            else:
                                # Else just account for scientific notation
                                line.append(f"{val:.{self.variables[i].field_width - 6}E}".rjust(self.variables[i].field_width))
                        else:
                            # Else print float without scientific notation (remove extra zeros)
                            if val < 0:
                                # If negative value, account for the "-" sign 
                                line.append(f"{val:.{self.variables[i].field_width - 2}g}".rjust(self.variables[i].field_width))
                            else:
                                # Else account only for the decimal point
                                line.append(f"{val:.{self.variables[i].field_width - 1}g}".rjust(self.variables[i].field_width))
                    
                    # If the variable is int:
                    elif self.variables[i].type is int:
                            
                        # Check length
                        if len(f"{val}") > self.variables[i].field_width:
                            # If too many digits, raise error
                            raise TypeError(f"{self.variables[i].name} exceeds the field width of {self.variables[i].field_width} characters.")
                        else:
                            # Else print as it is
                            line.append(f"{val}"[:self.variables[i].field_width].rjust(self.variables[i].field_width))
                    
                    # If the variable is str -> print as it is and truncate to maximum length (str generally can be truncated)
                    elif self.variables[i].type is str:
                        line.append(f"{val}"[:self.variables[i].field_width].rjust(self.variables[i].field_width))
                
                # Append line to the container of all values
                values.append("".join(f"{val}" for val in line))
                
            # Join all lines into one string
            values = "\n".join(f"{row}" for row in values)
            
        # Merge names and values strings
        return f"{names}\n{values}"
    
    
if __name__ == "__main__":
    card_dict = {"name": "vector_card_test",
                 "singleORcolumn": False,
                 "requirements": {"always": True,
                                  "variable": " ",
                                  "value": None},
                 "variables": [{"name": "var1",
                                "value": [1, 2],
                                "type": "int",
                                "field_width": 10,
                                "id": True},
                               {"name": "var2",
                                "value": [-1, -2],
                                "type": "int",
                                "field_width": 10,
                                "id": False},
                               {"name": "var3",
                                "value": [1.0, 2.0],
                                "type": "float",
                                "field_width": 10,
                                "id": False},
                               {"name": "var4",
                                "value": [-1.0, -2.0],
                                "type": "float",
                                "field_width": 10,
                                "id": False},
                               {"name": "var5",
                                "value": [12345678900.123456789, 23456789100.234567891],
                                "type": "float",
                                "field_width": 10,
                                "id": False},
                               {"name": "var6",
                                "value": [-12345678900.123456789, -23456789100.234567891],
                                "type": "float",
                                "field_width": 10,
                                "id": False},
                               {"name": "var7",
                                "value": [0.00000000000123456789, 0.00000000000234567891],
                                "type": "float",
                                "field_width": 10,
                                "id": False},
                               {"name": "var8",
                                "value": [-0.00000000000123456789, -0.00000000000234567891],
                                "type": "float",
                                "field_width": 10,
                                "id": False},
                               {"name": "var9",
                                "value": ["random_string_one", "random_string_two"],
                                "type": "str",
                                "field_width": 10,
                                "id": False}
                               ]}
    
    tmp = card(card_dict)
    
    tmp.variables[0].value = [123456789123456789, 234567891234567891]
    
    string = str(tmp)
    
    