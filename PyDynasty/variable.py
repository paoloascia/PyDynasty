##############################################################################
# Author: Paolo Ascia                                                        
# Date: February 2025                                                        
##############################################################################     

##############################################################################
# imports
##########

class variable():
    
    
    def __init__(self, var_dict):
        '''
        Class to contain all information regarding a variable.

        Parameters
        ----------
        var_dict : dict
            Dictionary from JSON with information on variable.
        '''
        
        # define variable name
        self.name: str = var_dict['name']
        
        # detect type
        if var_dict['type'] == 'str':
            self.type = str
        elif var_dict['type'] == 'int':
            self.type = int
        elif var_dict['type'] == 'float':
            self.type = float
            
        # Check type and save standard value
        self.value: self.type = var_dict['value']
        
        # read field width
        self.field_width: int = var_dict['field_width']
        
        # read if this is the card id
        self.id: bool = var_dict['id']
        
    def __repr__(self):
        # Represenation of variable
        
        return (f"\n"
                f"Variable: {self.name} \n"
                f"Type: {self.type.__name__} \n"
                f"Field width: {self.field_width} \n"
                f"Is id: {self.id} \n"
                f"Value: {self.value} \n")
    
    def __str__(self):
        # Printing sequence
        
        # Handle the printing differently if the variable is a scalar or ...
        if not isinstance(self.value, (list, tuple)):
            
            # If the variable is float:
            if self.type is float:
                
                # Check that when printed the it is not longer than the field width
                if (abs(self.value) >= 10 ** self.field_width or 
                    (abs(self.value) <= 10 ** (5 - self.field_width) and self.value != 0)):
                    
                    # If so switch to scientific notation
                    if self.value < 0:
                        # If negative value, account for the "-" sign
                        value = f"{self.value:.{self.field_width - 7}E}".rjust(self.field_width)
                        name = f"{self.name}".rjust(self.field_width)
                    else:
                        # Else just account for scientific notation
                        value = f"{self.value:.{self.field_width - 6}E}".rjust(self.field_width)
                        name = f"{self.name}".rjust(self.field_width)
                        
                else:
                    # Else print float without scientific notation (remove extra zeros)
                    if self.value < 0:
                        # If negative value, account for the "-" sign 
                        value = f"{self.value:.{self.field_width - 2}g}".rjust(self.field_width)
                        name = f"{self.name}".rjust(self.field_width)
                    else:
                        # Else account only for the decimal point
                        value = f"{self.value:.{self.field_width - 1}g}".rjust(self.field_width)
                        name = f"{self.name}".rjust(self.field_width)
        
            # If the variable is int:
            if self.type is int:
                
                # Check length
                if len(f"{self.value}") > self.field_width:
                    # If too many digits, raise error
                    raise TypeError(f"{self.name} exceeds the field width of {self.field_width} characters.")
                else:
                    # Else print as it is
                    value = f"{self.value}".rjust(self.field_width)
                    name = f"{self.name}".rjust(self.field_width)
            
            # If the variable is str -> print as it is and truncate to maximum length (str generally can be truncated)
            if self.type is str:
                value = f"{self.value}"[:self.field_width].rjust(self.field_width)
                name = f"{self.name}".rjust(self.field_width)
            
        # ... or a vector (List)
        else:
            
            value = []      # Initialize list of values to concatenate for printing
            
            # Iterate through the values
            for val in self.value:
                
                # If vector is non-empty
                try:
                    # If the variable is float:
                    if self.type is float:
                        
                        # Check that when printed the it is not longer than the field width
                        if (abs(val) >= 10 ** self.field_width or 
                            (abs(val) <= 10 ** (5 - self.field_width) and val != 0)):
                            
                            # If so switch to scientific notation
                            if val < 0:
                                # If negative value, account for the "-" sign
                                value.append(f"{val:.{self.field_width - 7}E}".rjust(self.field_width))
                            else:
                                # Else just account for scientific notation
                                value.append(f"{val:.{self.field_width - 6}E}".rjust(self.field_width))
                                
                        else:
                            # Else print float without scientific notation (remove extra zeros)
                            if val < 0:
                                # If negative value, account for the "-" sign 
                                value.append(f"{val:.{self.field_width - 2}g}".rjust(self.field_width))
                            else:
                                # Else account only for the decimal point
                                value.append(f"{val:.{self.field_width - 1}g}".rjust(self.field_width))
            
                    # If the variable is int:
                    if self.type is int:
                        # Check length
                        if len(f"{val}") > self.field_width:
                            # If too many digits, raise error
                            raise TypeError(f"{self.name} exceeds the field width of {self.field_width} characters.")
                        else:
                            # Else print as it is
                            value.append(f"{val}".rjust(self.field_width))
                    
                    # If the variable is str -> print as it is and truncate to maximum length (str generally can be truncated)
                    if self.type is str:
                        value.append(f"{val}"[:self.field_width].rjust(self.field_width))
                
                # If vector is empty, print spaces for the field width to mantain allignment of other variables
                except:
                    value.append("".join(" " for _ in range(self.field_width)))
            
            # Join the values as one string, and join string of names
            value = "\n".join(f"{val}" for val in value) 
            name = f"{self.name}".rjust(self.field_width)
          
        # Return the string to be printed (name + values)
        return f"{name}\n{value}"    

if __name__ == "__main__":
    tmp = variable({"name": "int_variable",
                     "type": "int",
                     "value": 10,
                     "field_width" : 8,
                     "id": False})  

