##############################################################################
# Author: Paolo Ascia                                                        
# Date: March 2025                                                        
##############################################################################      

##############################################################################
# imports
##########
import os
import pytest
from PyDynasty import deck
from PyDynasty import keyword

# Test initialization of deck
def test_deck():
    ls_deck = deck("Test_ls_deck")
    assert (isinstance(ls_deck, deck) and ls_deck.name == "Test_ls_deck")
    
# Test initialization of deck input error
def test_deck_err():
    with pytest.raises(TypeError):
        deck(1)

# Test add keyword first to use its functionalities in the other tests 
# (assume all lower functions work because already tested)
def test_add_keyword():
    ls_deck = deck("Test_ls_deck")
    
    # Add keyword
    ls_deck.add_keyword("TEST_MIXED", v1 = int(-3))
    
    # Check that the key has been added to the deck
    assert (repr(ls_deck.keywords_list[0]) == (f"\n"
                                               f"Name: TEST_MIXED \n"
                                               f"Id: 0 \n"
                                               f"Cards: card_1, card_2, card_3 \n") and 
            ls_deck.keywords_list[0].cards[1].variables[1].value == -3)
    
# Test add keyword input error
def test_add_keyword_err_type_input():
    ls_deck = deck("Test_ls_deck")
    with pytest.raises(TypeError):
        ls_deck.add_keyword(1)    

# Test not existant keyword
def test_add_keyword_err_keyword():
    ls_deck = deck("Test_ls_deck")
    with pytest.raises(FileNotFoundError):
        ls_deck.add_keyword("TEST_NOT_EXIST")
    
# Declare a deck for testing several functionalities
@pytest.fixture
def deck_for_testing():
    ls_deck = deck("deck_for_testing")
    
    # Add keyword
    ls_deck.add_keyword("TEST_SCALAR")
    
    # Add keyword
    ls_deck.add_keyword("TEST_VECTOR")
    
    # Add keyword
    ls_deck.add_keyword("TEST_MIXED")
    
    # Add keyword
    ls_deck.add_keyword("TEST_MIXED", kid = 2)
    
    return ls_deck

# Test updating ids
def test_update_ids(deck_for_testing):
    deck_for_testing.update_ids()
    
    assert (repr(deck_for_testing.keywords_list[0]) == (f"\n"
                                                        f"Name: TEST_SCALAR \n"
                                                        f"Id: 1 \n"
                                                        f"Cards: card_1, card_2 \n") and 
            repr(deck_for_testing.keywords_list[1]) == (f"\n"
                                                        f"Name: TEST_VECTOR \n"
                                                        f"Id: None \n"
                                                        f"Cards: card_1, card_2 \n") and 
            repr(deck_for_testing.keywords_list[2]) == (f"\n"
                                                        f"Name: TEST_MIXED \n"
                                                        f"Id: 1 \n"
                                                        f"Cards: card_1, card_2, card_3 \n") and 
            repr(deck_for_testing.keywords_list[3]) == (f"\n"
                                                        f"Name: TEST_MIXED \n"
                                                        f"Id: 2 \n"
                                                        f"Cards: card_1, card_2, card_3 \n"))

# Test finding a keyword
def test_find_keyword(deck_for_testing):
    deck_for_testing.update_ids()
    index, key = deck_for_testing.find_keyword("TEST_MIXED", id_ = 2)
    assert (index == 3 and
            isinstance(key, keyword) and
            repr(key) == (f"\n"
                          f"Name: TEST_MIXED \n"
                          f"Id: 2 \n"
                          f"Cards: card_1, card_2, card_3 \n"))

# Test removing a keyword
def test_remove_keyword(deck_for_testing):
    deck_for_testing.update_ids()
    deck_for_testing.remove_keyword("TEST_MIXED", id_ = 1)
    
    assert (repr(deck_for_testing.keywords_list[0]) == (f"\n"
                                                        f"Name: TEST_SCALAR \n"
                                                        f"Id: 1 \n"
                                                        f"Cards: card_1, card_2 \n") and 
            repr(deck_for_testing.keywords_list[1]) == (f"\n"
                                                        f"Name: TEST_VECTOR \n"
                                                        f"Id: None \n"
                                                        f"Cards: card_1, card_2 \n") and 
            repr(deck_for_testing.keywords_list[2]) == (f"\n"
                                                        f"Name: TEST_MIXED \n"
                                                        f"Id: 2 \n"
                                                        f"Cards: card_1, card_2, card_3 \n"))

# Test remove_keyword errors
def test_remove_keyword_err_type_input_name(deck_for_testing):
    with pytest.raises(TypeError):
        deck_for_testing.remove_keyword(1, id_ = 1)
def test_remove_keyword_err_type_input_id(deck_for_testing):
    with pytest.raises(TypeError):
        deck_for_testing.remove_keyword("TEST_MIXED", id_ = 1.)
    
# Testing changing a value in a keyword
def test_edit_keyword(deck_for_testing):
    deck_for_testing.update_ids()
    deck_for_testing.edit_keyword("TEST_MIXED", id_ = 2, v1 = 10)
    assert deck_for_testing.keywords_list[3].cards[1].variables[1].value == 10

# Testing retrieve the value of a variable
def test_retrieve_variable_from_keyword(deck_for_testing):
    deck_for_testing.update_ids()    
    assert deck_for_testing.retrieve_variable_from_keyword("TEST_MIXED", id_ = 2, variable_name = "v1") == -1

# Testing opening a keyfile, read the keywords, and print the deck again
def test_read_deck():
    input_file = os.path.join(os.getcwd(), "tests", "KEYWORDS", "TEST", "TEST_DECK_INPUT.k") 
    output_file = os.path.join(os.getcwd(), "tests", "KEYWORDS", "TEST", "TEST_DECK_OUTPUT.k") 
    
    deck_for_reading = deck("deck_for_reading")
    deck_for_reading.read_deck(input_file)
    
    with open(output_file) as f:
        expected_output = f.read()
    
    print(expected_output)
    print("-----------------------------------------------")
    print(deck_for_reading)
    
    assert str(deck_for_reading) == expected_output
    
    
    
    