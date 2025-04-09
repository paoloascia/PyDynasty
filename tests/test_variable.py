##############################################################################
# Author: Paolo Ascia                                                        
# Date: February 2025                                                        
##############################################################################     

##############################################################################
# imports
##########
import pytest
from src.variable import variable

##########
# Test float variable
# Initiate scalar float variable to test
@pytest.fixture
def variable_float():
    return variable({"name": "float_variable",
                     "type": "float",
                     "value": 10.1,
                     "field_width" : 8,
                     "id": False})

###
# Test properties
def test_variable_float_name(variable_float):
    assert isinstance(variable_float.name, str) and variable_float.name == "float_variable"

def test_variable_float_type(variable_float):
    assert variable_float.type is float

def test_variable_float_value(variable_float):
    assert isinstance(variable_float.value, float) and variable_float.value == 10.1

def test_variable_float_width(variable_float):
    assert isinstance(variable_float.field_width, int) and variable_float.field_width == 8
    
def test_variable_float_id(variable_float):
    assert  isinstance(variable_float.id, bool) and variable_float.id is False
    
# Test representation
def test_variable_float_representation(variable_float):
    assert repr(variable_float) == ("\n"
                                    "Variable: float_variable \n"
                                    "Type: float \n"
                                    "Field width: 8 \n"
                                    "Is id: False \n"
                                    "Value: 10.1 \n")
    
# Test the string return of a ...
# ... positive value, shorter than field width
def test_variable_float_string_positive_short(variable_float):
    assert str(variable_float) == ("float_variable\n    10.1")
    
# ... positive value, longer than field width
def test_variable_float_string_positive_long(variable_float):
    variable_float.value = 123456789.123456789  # Set value to positive number with more than 8 characters when printed
    assert str(variable_float) == ("float_variable\n1.23E+08")
    
# ... negative value, shorter than field width
def test_variable_float_string_negative_short(variable_float):
    variable_float.value = -10.1 # Set value to a negative value
    assert str(variable_float) == ("float_variable\n   -10.1")
    
# ... negative value, longer than field width
def test_variable_float_string_negative_long(variable_float):
    variable_float.value = -123456789.123456789  # Set value to negative number with more than 8 characters when printed
    assert str(variable_float) == ("float_variable\n-1.2E+08")
    
# Test float vector
def test_variable_float_string_vector(variable_float):
    # Set vector with all possible combinations
    variable_float.value = [        10.1,           # positive value, shorter than field width
                                   -10.1,           # negative value, shorter than field width
                             123456789.123456789,   # positive value, longer than field width
                            -123456789.123456789]   # negative value, longer than field width
    
    assert str(variable_float) == ("float_variable\n"
                                   "    10.1\n"
                                   "   -10.1\n"
                                   "1.23E+08\n"
                                   "-1.2E+08")

##########
# Test int scalar variable
# Initiate scalar int variable to test
@pytest.fixture
def variable_int():
    return variable({"name": "int_variable",
                     "type": "int",
                     "value": 10,
                     "field_width" : 8,
                     "id": False})

###
# Test properties
def test_variable_int_name(variable_int):
    assert isinstance(variable_int.name, str) and variable_int.name == "int_variable"

def test_variable_int_type(variable_int):
    assert variable_int.type is int

def test_variable_int_value(variable_int):
    assert isinstance(variable_int.value, int) and variable_int.value == 10

def test_variable_int_field_width(variable_int):
    assert isinstance(variable_int.field_width, int) and variable_int.field_width == 8
    
def test_variable_int_id(variable_int):
    assert  isinstance(variable_int.id, bool) and variable_int.id is False
    
# Test representation
def test_variable_int_representation(variable_int):
    assert repr(variable_int) == ("\n"
                                  "Variable: int_variable \n"
                                  "Type: int \n"
                                  "Field width: 8 \n"
                                  "Is id: False \n"
                                  "Value: 10 \n")
    
# Test the string return of a ...
# ... positive value, shorter than field width
def test_variable_int_string_positive_short(variable_int):
    assert str(variable_int) == ("int_variable\n      10")
    
# ... positive value, longer than field width
def test_variable_int_string_positive_long(variable_int):
    variable_int.value = 123456789  # Set value to positive number with more than 8 characters when printed
    with pytest.raises(TypeError):
        assert str(variable_int) == ("int_variable\n12345678")
    
# ... negative value, shorter than field width
def test_variable_int_string_negative_short(variable_int):
    variable_int.value = -10 # Set value to a negative value
    assert str(variable_int) == ("int_variable\n     -10")
    
# ... negative value, longer than field width
def test_variable_int_string_negative_long(variable_int):
    variable_int.value = 123456789  # Set value to positive number with more than 8 characters when printed
    with pytest.raises(TypeError):
        assert str(variable_int) == ("int_variable\n-1234567")

# Test int vector
def test_variable_int_string_vector(variable_int):
    # Set vector with all possible combinations
    variable_int.value = [        10,           # positive value, shorter than field width
                                 -10,           # negative value, shorter than field width
                            12345678,           # positive value, long as field width
                            -1234567]           # negative value, long as width
    
    assert str(variable_int) == ("int_variable\n"
                                 "      10\n"
                                 "     -10\n"
                                 "12345678\n"
                                 "-1234567")

##########
# Test str variable
# Initiate scalar str variable to test
@pytest.fixture
def variable_str():
    return variable({"name": "str_variable",
                     "type": "str",
                     "value": "eightstr",
                     "field_width" : 8,
                     "id": False})

###
# Test properties
def test_variable_str_name(variable_str):
    assert isinstance(variable_str.name, str) and variable_str.name == "str_variable"

def test_variable_str_type(variable_str):
    assert variable_str.type is str

def test_variable_str_value(variable_str):
    assert isinstance(variable_str.value, str) and variable_str.value == "eightstr"

def test_variable_str_field_width(variable_str):
    assert isinstance(variable_str.field_width, int) and variable_str.field_width == 8
    
def test_variable_str_id(variable_str):
    assert  isinstance(variable_str.id, bool) and variable_str.id is False
    
# Test representation
def test_variable_str_representation(variable_str):
    assert repr(variable_str) == ("\n"
                                  "Variable: str_variable \n"
                                  "Type: str \n"
                                  "Field width: 8 \n"
                                  "Is id: False \n"
                                  "Value: eightstr \n")
    
# Test the string return of a ...
# ... positive value, shorter than field width
def test_variable_str_string_short(variable_str):
    assert str(variable_str) == ("str_variable\neightstr")
    
# ... positive value, longer than field width
def test_variable_str_string_long(variable_str):
    variable_str.value = "ThisStringIsCut"  # Set value to string longer than field width
    assert str(variable_str) == ("str_variable\nThisStri")
    
# Test str vector
def test_variable_str_string_vector(variable_str):
    # Set vector with all possible combinations
    variable_str.value = ["shortstr",           # string shorter than field width
                          "verylongstr"]        # string longer than field width
    
    assert str(variable_str) == ("str_variable\n"
                                 "shortstr\n"
                                 "verylong")

             
