##############################################################################
# Author: Paolo Ascia                                                        
# Date: February 2025                                                        
##############################################################################   

##############################################################################
# imports
##########
import pytest

from PyDynasty.utilities import open_json_keyword
from PyDynasty.utilities import check_card_requirements



# Test function to load JSON dictionary
def test_open_json_keyword():
    
    keyword = "TEST_SCALAR"
    tmp = open_json_keyword(keyword)
    
    # Check that the dictionary is loaded correctly
    assert (isinstance(tmp["name"], str) and tmp["name"] == "TEST_SCALAR")
    assert (isinstance(tmp["id"], int) and tmp["id"] == 0)
    assert (isinstance(tmp["cards"], list) and len(tmp["cards"]) == 2)
    
    assert (isinstance(tmp["cards"][0]["name"], str) and tmp["cards"][0]["name"] == "card_1")
    assert (isinstance(tmp["cards"][0]["singleORcolumn"], bool) and tmp["cards"][0]["singleORcolumn"] is True)
    
    assert (isinstance(tmp["cards"][0]["requirements"]["always"], bool) and tmp["cards"][0]["requirements"]["always"] is True)
    assert (isinstance(tmp["cards"][0]["requirements"]["variable"], str) and tmp["cards"][0]["requirements"]["variable"] == " ")
    assert (isinstance(tmp["cards"][0]["requirements"]["value"], int) and tmp["cards"][0]["requirements"]["value"] == -1)
    
    assert (isinstance(tmp["cards"][0]["variables"], list) and len(tmp["cards"][0]["variables"]) == 1)
    
    assert (isinstance(tmp["cards"][0]["variables"][0]["name"], str) and tmp["cards"][0]["variables"][0]["name"] == "title")
    assert (isinstance(tmp["cards"][0]["variables"][0]["value"], str) and tmp["cards"][0]["variables"][0]["value"] == "Test of scalar variables without optional cards")
    assert (isinstance(tmp["cards"][0]["variables"][0]["type"], str) and tmp["cards"][0]["variables"][0]["type"] == "str")
    assert (isinstance(tmp["cards"][0]["variables"][0]["field_width"], int) and tmp["cards"][0]["variables"][0]["field_width"] == 90)
    assert (isinstance(tmp["cards"][0]["variables"][0]["id"], bool) and tmp["cards"][0]["variables"][0]["id"] is False)

    assert (isinstance(tmp["cards"][1]["name"], str) and tmp["cards"][1]["name"] == "card_2")
    assert (isinstance(tmp["cards"][1]["singleORcolumn"], bool) and tmp["cards"][1]["singleORcolumn"] is True)
    
    assert (isinstance(tmp["cards"][1]["requirements"]["always"], bool) and tmp["cards"][1]["requirements"]["always"] is True)
    assert (isinstance(tmp["cards"][1]["requirements"]["variable"], str) and tmp["cards"][1]["requirements"]["variable"] == " ")
    assert (isinstance(tmp["cards"][1]["requirements"]["value"], int) and tmp["cards"][1]["requirements"]["value"] == -1)
    
    assert (isinstance(tmp["cards"][1]["variables"], list) and len(tmp["cards"][1]["variables"]) == 9)
        
    assert (isinstance(tmp["cards"][1]["variables"][0]["name"], str) and tmp["cards"][1]["variables"][0]["name"] == "svip")
    assert (isinstance(tmp["cards"][1]["variables"][0]["value"], int) and tmp["cards"][1]["variables"][0]["value"] == 1)
    assert (isinstance(tmp["cards"][1]["variables"][0]["type"], str) and tmp["cards"][1]["variables"][0]["type"] == "int")
    assert (isinstance(tmp["cards"][1]["variables"][0]["field_width"], int) and tmp["cards"][1]["variables"][0]["field_width"] == 10)
    assert (isinstance(tmp["cards"][1]["variables"][0]["id"], bool) and tmp["cards"][1]["variables"][0]["id"] is True)
    
    assert (isinstance(tmp["cards"][1]["variables"][1]["name"], str) and tmp["cards"][1]["variables"][1]["name"] == "svin")
    assert (isinstance(tmp["cards"][1]["variables"][1]["value"], int) and tmp["cards"][1]["variables"][1]["value"] == -1)
    assert (isinstance(tmp["cards"][1]["variables"][1]["type"], str) and tmp["cards"][1]["variables"][1]["type"] == "int")
    assert (isinstance(tmp["cards"][1]["variables"][1]["field_width"], int) and tmp["cards"][1]["variables"][1]["field_width"] == 10)
    assert (isinstance(tmp["cards"][1]["variables"][1]["id"], bool) and tmp["cards"][1]["variables"][1]["id"] is False)
    
    assert (isinstance(tmp["cards"][1]["variables"][2]["name"], str) and tmp["cards"][1]["variables"][2]["name"] == "svfps")
    assert (isinstance(tmp["cards"][1]["variables"][2]["value"], float) and tmp["cards"][1]["variables"][2]["value"] == 1.)
    assert (isinstance(tmp["cards"][1]["variables"][2]["type"], str) and tmp["cards"][1]["variables"][2]["type"] == "float")
    assert (isinstance(tmp["cards"][1]["variables"][2]["field_width"], int) and tmp["cards"][1]["variables"][2]["field_width"] == 10)
    assert (isinstance(tmp["cards"][1]["variables"][2]["id"], bool) and tmp["cards"][1]["variables"][2]["id"] is False)
    
    assert (isinstance(tmp["cards"][1]["variables"][3]["name"], str) and tmp["cards"][1]["variables"][3]["name"] == "svfns")
    assert (isinstance(tmp["cards"][1]["variables"][3]["value"], float) and tmp["cards"][1]["variables"][3]["value"] == -1.)
    assert (isinstance(tmp["cards"][1]["variables"][3]["type"], str) and tmp["cards"][1]["variables"][3]["type"] == "float")
    assert (isinstance(tmp["cards"][1]["variables"][3]["field_width"], int) and tmp["cards"][1]["variables"][3]["field_width"] == 10)
    assert (isinstance(tmp["cards"][1]["variables"][3]["id"], bool) and tmp["cards"][1]["variables"][3]["id"] is False)
    
    assert (isinstance(tmp["cards"][1]["variables"][4]["name"], str) and tmp["cards"][1]["variables"][4]["name"] == "svfpl")
    assert (isinstance(tmp["cards"][1]["variables"][4]["value"], float) and tmp["cards"][1]["variables"][4]["value"] == 123456789.123456789)
    assert (isinstance(tmp["cards"][1]["variables"][4]["type"], str) and tmp["cards"][1]["variables"][4]["type"] == "float")
    assert (isinstance(tmp["cards"][1]["variables"][4]["field_width"], int) and tmp["cards"][1]["variables"][4]["field_width"] == 10)
    assert (isinstance(tmp["cards"][1]["variables"][4]["id"], bool) and tmp["cards"][1]["variables"][4]["id"] is False)
    
    assert (isinstance(tmp["cards"][1]["variables"][5]["name"], str) and tmp["cards"][1]["variables"][5]["name"] == "svfnl")
    assert (isinstance(tmp["cards"][1]["variables"][5]["value"], float) and tmp["cards"][1]["variables"][5]["value"] == -123456789.123456789)
    assert (isinstance(tmp["cards"][1]["variables"][5]["type"], str) and tmp["cards"][1]["variables"][5]["type"] == "float")
    assert (isinstance(tmp["cards"][1]["variables"][5]["field_width"], int) and tmp["cards"][1]["variables"][5]["field_width"] == 10)
    assert (isinstance(tmp["cards"][1]["variables"][5]["id"], bool) and tmp["cards"][1]["variables"][5]["id"] is False)
    
    assert (isinstance(tmp["cards"][1]["variables"][6]["name"], str) and tmp["cards"][1]["variables"][6]["name"] == "svfpsmal")
    assert (isinstance(tmp["cards"][1]["variables"][6]["value"], float) and tmp["cards"][1]["variables"][6]["value"] == 0.00000000000123456789)
    assert (isinstance(tmp["cards"][1]["variables"][6]["type"], str) and tmp["cards"][1]["variables"][6]["type"] == "float")
    assert (isinstance(tmp["cards"][1]["variables"][6]["field_width"], int) and tmp["cards"][1]["variables"][6]["field_width"] == 10)
    assert (isinstance(tmp["cards"][1]["variables"][6]["id"], bool) and tmp["cards"][1]["variables"][6]["id"] is False)
    
    assert (isinstance(tmp["cards"][1]["variables"][7]["name"], str) and tmp["cards"][1]["variables"][7]["name"] == "svfnsmal")
    assert (isinstance(tmp["cards"][1]["variables"][7]["value"], float) and tmp["cards"][1]["variables"][7]["value"] == -0.00000000000123456789)
    assert (isinstance(tmp["cards"][1]["variables"][7]["type"], str) and tmp["cards"][1]["variables"][7]["type"] == "float")
    assert (isinstance(tmp["cards"][1]["variables"][7]["field_width"], int) and tmp["cards"][1]["variables"][7]["field_width"] == 10)
    assert (isinstance(tmp["cards"][1]["variables"][7]["id"], bool) and tmp["cards"][1]["variables"][7]["id"] is False)

    assert (isinstance(tmp["cards"][1]["variables"][8]["name"], str) and tmp["cards"][1]["variables"][8]["name"] == "svstr")
    assert (isinstance(tmp["cards"][1]["variables"][8]["value"], str) and tmp["cards"][1]["variables"][8]["value"] == "random_long_string")
    assert (isinstance(tmp["cards"][1]["variables"][8]["type"], str) and tmp["cards"][1]["variables"][8]["type"] == "str")
    assert (isinstance(tmp["cards"][1]["variables"][8]["field_width"], int) and tmp["cards"][1]["variables"][8]["field_width"] == 10)
    assert (isinstance(tmp["cards"][1]["variables"][8]["id"], bool) and tmp["cards"][1]["variables"][8]["id"] is False)
    
# Test loading a keyword not supported
def test_open_json_keyword_unsupported():
    keyword = "TEST_UNSUPPORTED"
    
    with pytest.raises(FileNotFoundError):
        open_json_keyword(keyword)
        
# Test passing a non-string
def test_open_json_keyword_nonstring():
    keyword = 3
    
    with pytest.raises(TypeError):
        open_json_keyword(keyword)
    
# Define a test card class to test card requirements
class requirements():
    def __init__(self, always):
        self.always = always
        self.variable = 'var_1'
        self.value = 1
        
class variable():
    def __init__(self, name, value, type_, field_width, id_):
        self.name = name
        self.value = value
        self.type = type_
        self.field_width = field_width
        self.id = id_
    
class card():
    def __init__(self, name, always, variables):
        
        self.name = "card_1"
        self.singleORcolumn = True
        self.requirements = requirements(always)
        
        self.variables = variables
     
# Test cards that are always available
def test_check_card_requirements_always_true():
    
    cards = []
    req = requirements(always = True)
    
    assert check_card_requirements(cards, req) is True
    
# Test cards that are available on condition var_1 = 1, card present
def test_check_card_requirements_conditional_true():
    
    variables_1 = [variable('var_1', 1, int, 10, False),
                   variable('var_2', "2", str, 10, False),
                   variable('var_3', 3., float, 10, False)]
                   
    variables_2 = [variable('var_4', 4, int, 10, False),
                   variable('var_5', "5", str, 10, False),
                   variable('var_6', 6., float, 10, False)]
    cards = [card('card_1', True, variables_1),
             card('card_2', True, variables_2)]
    req = requirements(always = False)
    
    assert check_card_requirements(cards, req) is True
    
# Test cards that are available on condition var_1 = 1, card absent
def test_check_card_requirements_conditional_false():
    
    variables_1 = [variable('var_1', 2, int, 10, False),
                   variable('var_2', "3", str, 10, False),
                   variable('var_3', 4., float, 10, False)]
                   
    variables_2 = [variable('var_4', 5, int, 10, False),
                   variable('var_5', "6", str, 10, False),
                   variable('var_6', 7., float, 10, False)]
    cards = [card('card_1', True, variables_1),
             card('card_2', True, variables_2)]
    req = requirements(always = False)
    
    assert check_card_requirements(cards, req) is False
