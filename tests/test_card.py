##############################################################################
# Author: Paolo Ascia                                                        
# Date: February 2025                                                        
##############################################################################        

##############################################################################
# imports
##########
import pytest

from PyDynasty.card import card_requirement
from PyDynasty.card import card
from PyDynasty.variable import variable

# Test card requirements function to set always True and nothing else
def test_card_requirement_always():
    req = card_requirement(always = True)
    assert (req.always is True and req.variable == " " and req.value is None)

# Test card requirements function to set always False and define a variable with a value    
def test_card_requirement_conditional():
    req = card_requirement(always = False, variable = "dummy_variable", value = 1)
    assert (req.always is False and req.variable == "dummy_variable" and req.value == 1)
    
# Test scalar card -> declare a scalar card to call and test
@pytest.fixture
def card_scalar_test():
    card_dict = {"name": "scalar_card_test",
                 "singleORcolumn": True,
                 "requirements": {"always": True,
                                  "variable": " ",
                                  "value": None},
                 "variables": [{"name": "var1",                     # -> Test positive integer printing
                                "value": 1,
                                "type": "int",
                                "field_width": 10,
                                "id": True},
                               {"name": "var2",                     # -> Test negative integer printing
                                "value": -1,
                                "type": "int",
                                "field_width": 10,
                                "id": False},
                               {"name": "var3",                     # -> Test positive simple float printing
                                "value": 1.,
                                "type": "float",
                                "field_width": 10,
                                "id": False},
                               {"name": "var4",                     # -> Test negative simple float printing
                                "value": -1.,
                                "type": "float",
                                "field_width": 10,
                                "id": False},
                               {"name": "var5",                     # -> Test positive big float with scientific notation printing
                                "value": 12345678900.123456789,
                                "type": "float",
                                "field_width": 10,
                                "id": False},
                               {"name": "var6",                     # -> Test negative big float with scientific notation printing
                                "value": -12345678900.123456789,
                                "type": "float",
                                "field_width": 10,
                                "id": False},
                               {"name": "var7",                     # -> Test positive small float with scientific notation printing
                                "value": 0.00000000000123456789,
                                "type": "float",
                                "field_width": 10,
                                "id": False},
                               {"name": "var8",                     # -> Test negative small float with scientific notation printing
                                "value": -0.00000000000123456789,
                                "type": "float",
                                "field_width": 10,
                                "id": False},
                               {"name": "var9",                     # -> Test string longer than field printing
                                "value": "random_long_string",
                                "type": "str",
                                "field_width": 10,
                                "id": False}
                               ]}
    
    return card(card_dict)

# Test correct initialization
def test_scalar_card_init(card_scalar_test):
    # Test metadata
    assert (isinstance(card_scalar_test.name, str) and card_scalar_test.name == "scalar_card_test")
    assert (isinstance(card_scalar_test.singleORcolumn, bool) and card_scalar_test.singleORcolumn is True)
    
    # Test requirements
    assert (isinstance(card_scalar_test.requirements.always, bool) and card_scalar_test.requirements.always is True)
    assert (isinstance(card_scalar_test.requirements.variable, str) and card_scalar_test.requirements.variable == " ")
    assert (card_scalar_test.requirements.value is None)
    
    # Test variables content
    assert (isinstance(card_scalar_test.variables[0].name, str) and card_scalar_test.variables[0].name == "var1")
    assert (isinstance(card_scalar_test.variables[0].value, int) and card_scalar_test.variables[0].value == 1)
    assert (card_scalar_test.variables[0].type is int)
    assert (isinstance(card_scalar_test.variables[0].field_width, int) and card_scalar_test.variables[0].field_width == 10)
    assert (isinstance(card_scalar_test.variables[0].id, bool) and card_scalar_test.variables[0].id is True)

    assert (isinstance(card_scalar_test.variables[1].name, str) and card_scalar_test.variables[1].name == "var2")
    assert (isinstance(card_scalar_test.variables[1].value, int) and card_scalar_test.variables[1].value == -1)
    assert (card_scalar_test.variables[1].type is int)
    assert (isinstance(card_scalar_test.variables[1].field_width, int) and card_scalar_test.variables[1].field_width == 10)
    assert (isinstance(card_scalar_test.variables[1].id, bool) and card_scalar_test.variables[1].id is False)
    
    assert (isinstance(card_scalar_test.variables[2].name, str) and card_scalar_test.variables[2].name == "var3")
    assert (isinstance(card_scalar_test.variables[2].value, float) and card_scalar_test.variables[2].value == 1.)
    assert (card_scalar_test.variables[2].type is float)
    assert (isinstance(card_scalar_test.variables[2].field_width, int) and card_scalar_test.variables[2].field_width == 10)
    assert (isinstance(card_scalar_test.variables[2].id, bool) and card_scalar_test.variables[2].id is False)

    assert (isinstance(card_scalar_test.variables[3].name, str) and card_scalar_test.variables[3].name == "var4")
    assert (isinstance(card_scalar_test.variables[3].value, float) and card_scalar_test.variables[3].value == -1.)
    assert (card_scalar_test.variables[3].type is float)
    assert (isinstance(card_scalar_test.variables[3].field_width, int) and card_scalar_test.variables[3].field_width == 10)
    assert (isinstance(card_scalar_test.variables[3].id, bool) and card_scalar_test.variables[3].id is False)

    assert (isinstance(card_scalar_test.variables[4].name, str) and card_scalar_test.variables[4].name == "var5")
    assert (isinstance(card_scalar_test.variables[4].value, float) and card_scalar_test.variables[4].value == 12345678900.123456789)
    assert (card_scalar_test.variables[4].type is float)
    assert (isinstance(card_scalar_test.variables[4].field_width, int) and card_scalar_test.variables[4].field_width == 10)
    assert (isinstance(card_scalar_test.variables[4].id, bool) and card_scalar_test.variables[4].id is False)

    assert (isinstance(card_scalar_test.variables[5].name, str) and card_scalar_test.variables[5].name == "var6")
    assert (isinstance(card_scalar_test.variables[5].value, float) and card_scalar_test.variables[5].value == -12345678900.123456789)
    assert (card_scalar_test.variables[5].type is float)
    assert (isinstance(card_scalar_test.variables[5].field_width, int) and card_scalar_test.variables[5].field_width == 10)
    assert (isinstance(card_scalar_test.variables[5].id, bool) and card_scalar_test.variables[5].id is False)
    
    assert (isinstance(card_scalar_test.variables[6].name, str) and card_scalar_test.variables[6].name == "var7")
    assert (isinstance(card_scalar_test.variables[6].value, float) and card_scalar_test.variables[6].value == 0.00000000000123456789)
    assert (card_scalar_test.variables[6].type is float)
    assert (isinstance(card_scalar_test.variables[6].field_width, int) and card_scalar_test.variables[6].field_width == 10)
    assert (isinstance(card_scalar_test.variables[6].id, bool) and card_scalar_test.variables[6].id is False)

    assert (isinstance(card_scalar_test.variables[7].name, str) and card_scalar_test.variables[7].name == "var8")
    assert (isinstance(card_scalar_test.variables[7].value, float) and card_scalar_test.variables[7].value == -0.00000000000123456789)
    assert (card_scalar_test.variables[7].type is float)
    assert (isinstance(card_scalar_test.variables[7].field_width, int) and card_scalar_test.variables[7].field_width == 10)
    assert (isinstance(card_scalar_test.variables[7].id, bool) and card_scalar_test.variables[7].id is False)
    
    assert (isinstance(card_scalar_test.variables[8].name, str) and card_scalar_test.variables[8].name == "var9")
    assert (isinstance(card_scalar_test.variables[8].value, str) and card_scalar_test.variables[8].value == "random_long_string")
    assert (card_scalar_test.variables[8].type is str)
    assert (isinstance(card_scalar_test.variables[8].field_width, int) and card_scalar_test.variables[8].field_width == 10)
    assert (isinstance(card_scalar_test.variables[8].id, bool) and card_scalar_test.variables[8].id is False)
    
# Test representation of card always present
def test_scalar_card_representation_always(card_scalar_test):
    representation = (f"\n"
                      f"Name: scalar_card_test \n"
                      f"Is scalar: True \n"
                      f"Active: Always \n")
    assert(repr(card_scalar_test) == representation)
    
# Test representation of card present on condition var_x == 1
def test_scalar_card_representation_conditional(card_scalar_test):
    card_scalar_test.requirements.always = False
    card_scalar_test.requirements.variable = "var_x"
    card_scalar_test.requirements.value = 1
    representation = (f"\n"
                      f"Name: scalar_card_test \n"
                      f"Is scalar: True \n"
                      f"Active: if var_x == 1 \n")
    assert(repr(card_scalar_test) == representation)
    
# Test string print of card
def test_scalar_card_string(card_scalar_test):
    printed_card = ("$#    var1      var2      var3      var4      var5      var6      var7      var8      var9\n"
                    "         1        -1         1        -11.2346E+10-1.235E+101.2346E-12-1.235E-12random_lon")
    assert (str(card_scalar_test) == printed_card)

# Test integer representation error
def test_scalar_card_string_error(card_scalar_test):
    card_scalar_test.variables[0].value = 123456789123456789
    
    with pytest.raises(TypeError):
        str(card_scalar_test)
    
# Test vectorial card -> declare a vectorial card to call and test
@pytest.fixture
def card_vector_test():
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
    
    return card(card_dict)

# Test correct initialization
def test_vector_card_init(card_vector_test):
    # Test metadata
    assert (isinstance(card_vector_test.name, str) and card_vector_test.name == "vector_card_test")
    assert (isinstance(card_vector_test.singleORcolumn, bool) and card_vector_test.singleORcolumn is False)
    
    # Test requirements
    assert (isinstance(card_vector_test.requirements.always, bool) and card_vector_test.requirements.always is True)
    assert (isinstance(card_vector_test.requirements.variable, str) and card_vector_test.requirements.variable == " ")
    assert (card_vector_test.requirements.value is None)
    
    # Test variables content
    assert (isinstance(card_vector_test.variables[0].name, str) and card_vector_test.variables[0].name == "var1")
    assert (isinstance(card_vector_test.variables[0].value, list) and card_vector_test.variables[0].value == [1, 2])
    assert (card_vector_test.variables[0].type is int)
    assert (isinstance(card_vector_test.variables[0].field_width, int) and card_vector_test.variables[0].field_width == 10)
    assert (isinstance(card_vector_test.variables[0].id, bool) and card_vector_test.variables[0].id is True)

    assert (isinstance(card_vector_test.variables[1].name, str) and card_vector_test.variables[1].name == "var2")
    assert (isinstance(card_vector_test.variables[1].value, list) and card_vector_test.variables[1].value == [-1, -2])
    assert (card_vector_test.variables[1].type is int)
    assert (isinstance(card_vector_test.variables[1].field_width, int) and card_vector_test.variables[1].field_width == 10)
    assert (isinstance(card_vector_test.variables[1].id, bool) and card_vector_test.variables[1].id is False)
    
    assert (isinstance(card_vector_test.variables[2].name, str) and card_vector_test.variables[2].name == "var3")
    assert (isinstance(card_vector_test.variables[2].value, list) and card_vector_test.variables[2].value == [1.0, 2.0])
    assert (card_vector_test.variables[2].type is float)
    assert (isinstance(card_vector_test.variables[2].field_width, int) and card_vector_test.variables[2].field_width == 10)
    assert (isinstance(card_vector_test.variables[2].id, bool) and card_vector_test.variables[2].id is False)

    assert (isinstance(card_vector_test.variables[3].name, str) and card_vector_test.variables[3].name == "var4")
    assert (isinstance(card_vector_test.variables[3].value, list) and card_vector_test.variables[3].value == [-1.0, -2.0])
    assert (card_vector_test.variables[3].type is float)
    assert (isinstance(card_vector_test.variables[3].field_width, int) and card_vector_test.variables[3].field_width == 10)
    assert (isinstance(card_vector_test.variables[3].id, bool) and card_vector_test.variables[3].id is False)

    assert (isinstance(card_vector_test.variables[4].name, str) and card_vector_test.variables[4].name == "var5")
    assert (isinstance(card_vector_test.variables[4].value, list) and card_vector_test.variables[4].value == [12345678900.123456789, 23456789100.234567891])
    assert (card_vector_test.variables[4].type is float)
    assert (isinstance(card_vector_test.variables[4].field_width, int) and card_vector_test.variables[4].field_width == 10)
    assert (isinstance(card_vector_test.variables[4].id, bool) and card_vector_test.variables[4].id is False)

    assert (isinstance(card_vector_test.variables[5].name, str) and card_vector_test.variables[5].name == "var6")
    assert (isinstance(card_vector_test.variables[5].value, list) and card_vector_test.variables[5].value == [-12345678900.123456789, -23456789100.234567891])
    assert (card_vector_test.variables[5].type is float)
    assert (isinstance(card_vector_test.variables[5].field_width, int) and card_vector_test.variables[5].field_width == 10)
    assert (isinstance(card_vector_test.variables[5].id, bool) and card_vector_test.variables[5].id is False)
    
    assert (isinstance(card_vector_test.variables[6].name, str) and card_vector_test.variables[6].name == "var7")
    assert (isinstance(card_vector_test.variables[6].value, list) and card_vector_test.variables[6].value == [0.00000000000123456789, 0.00000000000234567891])
    assert (card_vector_test.variables[6].type is float)
    assert (isinstance(card_vector_test.variables[6].field_width, int) and card_vector_test.variables[6].field_width == 10)
    assert (isinstance(card_vector_test.variables[6].id, bool) and card_vector_test.variables[6].id is False)

    assert (isinstance(card_vector_test.variables[7].name, str) and card_vector_test.variables[7].name == "var8")
    assert (isinstance(card_vector_test.variables[7].value, list) and card_vector_test.variables[7].value == [-0.00000000000123456789, -0.00000000000234567891])
    assert (card_vector_test.variables[7].type is float)
    assert (isinstance(card_vector_test.variables[7].field_width, int) and card_vector_test.variables[7].field_width == 10)
    assert (isinstance(card_vector_test.variables[7].id, bool) and card_vector_test.variables[7].id is False)
    
    assert (isinstance(card_vector_test.variables[8].name, str) and card_vector_test.variables[8].name == "var9")
    assert (isinstance(card_vector_test.variables[8].value, list) and card_vector_test.variables[8].value == ["random_string_one", "random_string_two"])
    assert (card_vector_test.variables[8].type is str)
    assert (isinstance(card_vector_test.variables[8].field_width, int) and card_vector_test.variables[8].field_width == 10)
    assert (isinstance(card_vector_test.variables[8].id, bool) and card_vector_test.variables[8].id is False)
    
# Test representation of card always present
def test_vector_card_representation_always(card_vector_test):
    representation = (f"\n"
                      f"Name: vector_card_test \n"
                      f"Is scalar: False \n"
                      f"Active: Always \n")
    assert(repr(card_vector_test) == representation)
    
# Test representation of card present on condition var_x == 1
def test_vector_card_representation_conditional(card_vector_test):
    card_vector_test.requirements.always = False
    card_vector_test.requirements.variable = "var_x"
    card_vector_test.requirements.value = 1
    representation = (f"\n"
                      f"Name: vector_card_test \n"
                      f"Is scalar: False \n"
                      f"Active: if var_x == 1 \n")
    assert(repr(card_vector_test) == representation)
    
# Test string print of card
def test_vector_card_string(card_vector_test):
    printed_card = ("$#    var1      var2      var3      var4      var5      var6      var7      var8      var9\n"
                    "         1        -1         1        -11.2346E+10-1.235E+101.2346E-12-1.235E-12random_str\n"
                    "         2        -2         2        -22.3457E+10-2.346E+102.3457E-12-2.346E-12random_str")
    assert (str(card_vector_test) == printed_card)

# Test integer representation error
def test_vector_card_string_error(card_vector_test):
    card_vector_test.variables[0].value = [123456789123456789, 234567891234567891]
    
    with pytest.raises(TypeError):
        str(card_vector_test)


