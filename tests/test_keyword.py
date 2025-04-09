##############################################################################
# Author: Paolo Ascia                                                        
# Date: February 2025                                                        
##############################################################################     

##############################################################################
# imports
##########
import difflib
from itertools import combinations
import os
import pytest
# from keyword import keyword
from PyDynasty import keyword

# Helper function to open .k files
def open_kfile(keyword_name):
    
    # Check input type
    if not isinstance(keyword_name, str):
        raise TypeError(f"Expected str, {type(keyword_name).__name__} passed.")
        
    # Split keywords to identify correct folder
    keyword_class = keyword_name.split("_")[0] 
    
    # Path of the keyword  
    rel_path = os.path.join("tests", "KEYWORDS", keyword_class, keyword_name + '.k')  
    file_path = os.path.join(os.getcwd(), rel_path)
    
    # If keyword exists
    try:
        
        # Open JSON file 
        with open(file_path, "r") as f:
            key = f.read()
    
    except:
        raise FileNotFoundError(f"{keyword_name} test file is missing.\n")
        
    keys = key.split('\n*')
    
    # Remove potential new line from end of keyword
    keys = [key[:-1] if key.endswith("\n") else key for key in keys]  
    
    # Add potential missing "*" from beginning of keyword
    keys = ["*" + key if not key.startswith("*") else key for key in keys] 
    return keys

# Find differences between the keywords
def find_string_difference(str1, str2):
    differ = difflib.ndiff(str1, str2)
    result = ''.join(differ)
    return result

# Function to compare print output and passed text
def compare_keyobj_keytext(key_obj: keyword, key_text: str): 
    key_obj_out = str(key_obj)
    if key_obj_out == key_text:
        return True
    else:
        return False
    
# Function to determine all possible card combination
def possible_card_combination(key_obj):
    condition = []
    std_value = {}
    for cd in key_obj.cards:
        if cd.requirements.always:
            continue
        else:
            condition.append({cd.requirements.variable: cd.requirements.value})
            std_value[cd.requirements.variable] = key_obj.retrieve_variable(cd.requirements.variable)
    
    # generate all possible combination
    all_combinations = [list(combinations(condition, r)) for r in range(1, len(condition) + 1)]
    combis = [item for sublist in all_combinations for item in sublist]
    
    # Define list with all conditions that could be changed and resetting to std values
    variables_settings = []
    for comb in combis:
        variables_settings.append(std_value.copy())
        for var in comb:
            variables_settings[-1][list(var.keys())[0]] = var[list(var.keys())[0]]
    return variables_settings

# Test keyword input format error
def test_keyword_error():
    with pytest.raises(TypeError):
        keyword(1)
        
# Test opening a keyword
def test_keyword():
    keyword_name = "TEST_SCALAR"
    key = keyword(keyword_name)
    
    assert isinstance(key, keyword)
     
    # Test that the values saved are the expected ones
    assert (isinstance(key.name, str) and key.name == keyword_name)
    assert (isinstance(key.id, int) and key.id == 0)
    
    # Test number of cards loaded
    assert (isinstance(key.cards, list) and len(key.cards) == 2)

# Declare different keywords for testing different features, representation, and printing:
# 1) Keyword with only scalar cards always presents
@pytest.fixture
def test_scalar():
    keyword_name = "TEST_SCALAR"
    return keyword(keyword_name)

# 2) Keyword with scalar cards conditionally presents
@pytest.fixture
def test_scalar_optional():
    keyword_name = "TEST_SCALAR_OPTIONAL"
    return keyword(keyword_name)

# 3) Keyword with only scalar cards without an ID
@pytest.fixture
def test_scalar_no_id():
    keyword_name = "TEST_SCALAR_NO_ID"
    return keyword(keyword_name)

# 4) Keyword with vectorial cards always presents
@pytest.fixture
def test_vector():
    keyword_name = "TEST_VECTOR"
    return keyword(keyword_name)

# 5) Keyword with scalar and vectorial cards always presents
@pytest.fixture
def test_mixed():
    keyword_name = "TEST_MIXED"
    return keyword(keyword_name)

# 6) Keyword with scalar and vectorial cards conditionally presents
@pytest.fixture
def test_mixed_optional():
    keyword_name = "TEST_MIXED_OPTIONAL"
    return keyword(keyword_name)

# Test function to retrieve value of a variable
def test_keyword_retrieve_variable(test_mixed):
    var_scalar = test_mixed.retrieve_variable(variable_name = "v3")
    var_vect = test_mixed.retrieve_variable(variable_name = "vv3")
    assert (isinstance(var_scalar, float) and var_scalar == -1.)
    assert (isinstance(var_vect, list) and var_vect == [-1., -2.])
    
# Test wrong input 
def test_keyword_retrieve_variable_err_input(test_mixed):
    with pytest.raises(TypeError):
        test_mixed.retrieve_variable(variable_name = 1)

# Test variable name not present in keyword
def test_keyword_retrieve_variable_err_var(test_mixed):
    with pytest.raises(TypeError):
        test_mixed.retrieve_variable(variable_name = "rand")
        
# Test function to find a variable inside a keyword
def test_keyword_find_variable(test_mixed):
    id_card, name_card, id_variable = test_mixed.find_variable(variable_name = "vv3")
    assert (isinstance(id_card, int) and id_card == 2)
    assert (isinstance(name_card, str) and name_card == "card_3")
    assert (isinstance(id_variable, int) and id_variable == 3)
    
# Test wrong input 
def test_keyword_find_variable_err_input(test_mixed):
    with pytest.raises(TypeError):
        test_mixed.retrieve_variable(variable_name = 1)

# Test variable name not present in keyword
def test_keyword_find_variable_err_var(test_mixed):
    with pytest.raises(TypeError):
        test_mixed.retrieve_variable(variable_name = "rand")
        
# Test functions to update id
def test_keyword_update_id(test_mixed):
    test_mixed.update_id()
    assert test_mixed.id == 1
    
# Test functions to update id when keyword does not have one
def test_keyword_update_no_id(test_scalar_no_id):
    test_scalar_no_id.update_id()
    assert test_scalar_no_id.id is None
    
# Test edit function with ...
# Changing a simple scalar
def test_keyword_edit_scalar(test_mixed):
    test_mixed.edit(v1 = 1, v2 = -1., v3 = 1.)
    assert (test_mixed.cards[1].variables[1].value == 1 and
            test_mixed.cards[1].variables[2].value == -1. and
            test_mixed.cards[1].variables[3].value == 1.)

# Passing wrong scalar type
def test_keyword_edit_scalar_err_scalar_type(test_mixed):
    with pytest.raises(TypeError):
        test_mixed.edit(v1 = 1, v2 = -1, v3 = 1.)

# Passing a vector to a scalar
def test_keyword_edit_scalar_err_vect_on_scalar(test_mixed):
    with pytest.raises(TypeError):
        test_mixed.edit(v1 = 1, v2 = [-1., -2.], v3 = 1.)

# Changing a vector
def test_keyword_edit_vector(test_mixed):
    test_mixed.edit(vv1 = [1, 2], vv2 = [-1., -2.], vv3 = [1., 2.])
    assert (test_mixed.cards[2].variables[1].value == [1, 2] and
            test_mixed.cards[2].variables[2].value == [-1., -2.] and
            test_mixed.cards[2].variables[3].value == [1., 2.])

# Changing a vector with an incosisten length
def test_keyword_edit_vector_len(test_mixed):
    test_mixed.edit(vv1 = [1, 2, 3, 4], vv2 = [-1.], vv3 = [1., 2.])
    assert (test_mixed.cards[2].variables[0].value == [ 1,  2,  [], []] and
            test_mixed.cards[2].variables[1].value == [ 1,  2,  3,  4] and
            test_mixed.cards[2].variables[2].value == [-1., [], [], []] and
            test_mixed.cards[2].variables[3].value == [ 1., 2., [], []] and
            test_mixed.cards[2].variables[4].value == [12345678900.123456789, 23456789100.234567891, [], []] and
            test_mixed.cards[2].variables[5].value == [-12345678900.123456789, -23456789100.234567891, [], []] and
            test_mixed.cards[2].variables[6].value == [0.00000000000123456789, 0.00000000000234567891, [], []] and
            test_mixed.cards[2].variables[7].value == [-0.00000000000123456789, -0.00000000000234567891, [], []] and
            test_mixed.cards[2].variables[8].value == ["random_string_one", "random_string_two", [], []])

# Passing a scalar to a vector
def test_keyword_edit_err_scalar_on_vector(test_mixed):
    with pytest.raises(TypeError):
        test_mixed.edit(vv1 = [1, 2], vv2 = -1., vv3 = [1., 2.])

# Passing a vector with one wrong entry
def test_keyword_edit_err_vect_type(test_mixed):
    with pytest.raises(TypeError):
        test_mixed.edit(vv1 = [1, 2], vv2 = [-1, -2], vv3 = [1., 2.])

# Test representation of ...
# ... keyword with only scalar card always present
def test_keyword_repr_scalar(test_scalar):
    expect_repr = (f"\n"
                   f"Name: TEST_SCALAR \n"
                   f"Id: 0 \n"
                   f"Cards: card_1, card_2 \n")
    
    assert repr(test_scalar) == expect_repr
    
# ... keyword with scalar cards conditionally presents
def test_keyword_repr_scalar_optional(test_scalar_optional):
    test_scalar_optional.edit(trig2=1)
    expect_repr = (f"\n"
                   f"Name: TEST_SCALAR_OPTIONAL \n"
                   f"Id: 0 \n"
                   f"Cards: card_1, card_2, card_3 \n")
    
    assert repr(test_scalar_optional) == expect_repr
    
# ... keyword with only scalar cards without an ID
def test_keyword_repr_no_id(test_scalar_no_id):
    expect_repr = (f"\n"
                   f"Name: TEST_SCALAR_NO_ID \n"
                   f"Id: None \n"
                   f"Cards: card_1, card_2 \n")
    
    assert repr(test_scalar_no_id) == expect_repr
    
# ... keyword with vectorial cards always presents
def test_keyword_repr_vector(test_vector):
    expect_repr = (f"\n"
                   f"Name: TEST_VECTOR \n"
                   f"Id: 0 \n"
                   f"Cards: card_1, card_2 \n")
    
    assert repr(test_vector) == expect_repr
    
# ... keyword with scalar and vectorial cards always presents
def test_keyword_repr_mixed(test_mixed):
    expect_repr = (f"\n"
                   f"Name: TEST_MIXED \n"
                   f"Id: 0 \n"
                   f"Cards: card_1, card_2, card_3 \n")
    
    assert repr(test_mixed) == expect_repr
    
# ... keyword with scalar and vectorial cards conditionally presents
def test_keyword_repr_mixed_optional(test_mixed_optional):
    test_mixed_optional.edit(trig3 = 1)             # -> the parent card is still hidden, should not appear in the list
    expect_repr = (f"\n"
                   f"Name: TEST_MIXED_OPTIONAL \n"
                   f"Id: 0 \n"
                   f"Cards: card_1, card_2 \n")
    
    assert repr(test_mixed_optional) == expect_repr
    
# Test string output of ...
# ... keyword with only scalar card always present
def test_keyword_str_scalar(test_scalar):
    expected_text = open_kfile("TEST_SCALAR")
    test_key_obj = test_scalar
    print("\nRead k-file:")
    [print(text) for text in expected_text]
    combs = possible_card_combination(test_key_obj)
    print("\nTested keywords:")
    if not combs:
        print(test_key_obj)
        assert compare_keyobj_keytext(test_key_obj, expected_text[0]) is True
    else:
        tests = []
        for c in combs:
            test_key_obj.edit(**c)
            
            single_test = False
            for text in expected_text:
                print(test_key_obj)
                print("------------------------------------------------------")
                if compare_keyobj_keytext(test_key_obj, text) is True:
                    print("True")
                    single_test = True
                    break
            tests.append(single_test)
            
        # Print comparison between text and object -> help finding differences
        if not all(tests) is True:
            for c in combs:
                test_key_obj.edit(**c)
                for text in expected_text:
                    print("\n- Character missing in read k-fyle and present in object printout"
                          "\n+ Character present in object printout and missing in read k-fyle")
                    print(find_string_difference(str(test_key_obj), text))
                    print("------------------------------------------------------")
        assert all(tests) is True
    
# ... keyword with scalar cards conditionally presents
def test_keyword_str_scalar_optional(test_scalar_optional):
    expected_text = open_kfile("TEST_SCALAR_OPTIONAL")
    test_key_obj = test_scalar_optional
    print("\nRead k-file:")
    [print(text) for text in expected_text]
    combs = possible_card_combination(test_key_obj)
    print("\nTested keywords:")
    if not combs:
        print(test_key_obj)
        assert compare_keyobj_keytext(test_key_obj, expected_text[0]) is True
    else:
        tests = []
        for c in combs:
            test_key_obj.edit(**c)
            
            single_test = False
            for text in expected_text:
                print(test_key_obj)
                print("------------------------------------------------------")
                if compare_keyobj_keytext(test_key_obj, text) is True:
                    print("True")
                    single_test = True
                    break
            tests.append(single_test)
            
        # Print comparison between text and object -> help finding differences
        if not all(tests) is True:
            for c in combs:
                test_key_obj.edit(**c)
                for text in expected_text:
                    print("\n- Character missing in read k-fyle and present in object printout"
                          "\n+ Character present in object printout and missing in read k-fyle")
                    print(find_string_difference(str(test_key_obj), text))
                    print("------------------------------------------------------")
        assert all(tests) is True

# ... keyword with only scalar cards without an ID -> no need, the ID is not called in the printing method
        
# ... keyword with vectorial cards always presents
def test_keyword_str_vector(test_vector):
    expected_text = open_kfile("TEST_VECTOR")
    test_key_obj = test_vector
    print("\nRead k-file:")
    [print(text) for text in expected_text]
    combs = possible_card_combination(test_key_obj)
    print("\nTested keywords:")
    if not combs:
        print(test_key_obj)
        assert compare_keyobj_keytext(test_key_obj, expected_text[0]) is True
    else:
        tests = []
        for c in combs:
            test_key_obj.edit(**c)
            
            single_test = False
            for text in expected_text:
                print(test_key_obj)
                print("------------------------------------------------------")
                if compare_keyobj_keytext(test_key_obj, text) is True:
                    print("True")
                    single_test = True
                    break
            tests.append(single_test)
            
        # Print comparison between text and object -> help finding differences
        if not all(tests) is True:
            for c in combs:
                test_key_obj.edit(**c)
                for text in expected_text:
                    print("\n- Character missing in read k-fyle and present in object printout"
                          "\n+ Character present in object printout and missing in read k-fyle")
                    print(find_string_difference(str(test_key_obj), text))
                    print("------------------------------------------------------")
        assert all(tests) is True
        
# ... keyword with vectorial cards always presents and vectors with different lengths
def test_keyword_str_vector_len(test_vector):
    test_vector.edit(svin = [1, 2, 3, 4], svfps = [-1.], svfns = [1., 2.])
    expected_text = open_kfile("TEST_VECTOR_LEN")
    test_key_obj = test_vector
    print("\nRead k-file:")
    [print(text) for text in expected_text]
    combs = possible_card_combination(test_key_obj)
    print("\nTested keywords:")
    if not combs:
        print(test_key_obj)
        assert compare_keyobj_keytext(test_key_obj, expected_text[0]) is True
    else:
        tests = []
        for c in combs:
            test_key_obj.edit(**c)
            
            single_test = False
            for text in expected_text:
                print(test_key_obj)
                print("------------------------------------------------------")
                if compare_keyobj_keytext(test_key_obj, text) is True:
                    print("True")
                    single_test = True
                    break
            tests.append(single_test)
            
        # Print comparison between text and object -> help finding differences
        if not all(tests) is True:
            for c in combs:
                test_key_obj.edit(**c)
                for text in expected_text:
                    print("\n- Character missing in read k-fyle and present in object printout"
                          "\n+ Character present in object printout and missing in read k-fyle")
                    print(find_string_difference(str(test_key_obj), text))
                    print("------------------------------------------------------")
        assert all(tests) is True
        
# ... keyword with scalar and vectorial cards always presents
def test_keyword_str_mixed(test_mixed):
    expected_text = open_kfile("TEST_MIXED")
    test_key_obj = test_mixed
    print("\nRead k-file:")
    [print(text) for text in expected_text]
    combs = possible_card_combination(test_key_obj)
    print("\nTested keywords:")
    if not combs:
        print(test_key_obj)
        assert compare_keyobj_keytext(test_key_obj, expected_text[0]) is True
    else:
        tests = []
        for c in combs:
            test_key_obj.edit(**c)
            
            single_test = False
            for text in expected_text:
                print(test_key_obj)
                print("------------------------------------------------------")
                if compare_keyobj_keytext(test_key_obj, text) is True:
                    print("True")
                    single_test = True
                    break
            tests.append(single_test)
            
        # Print comparison between text and object -> help finding differences
        if not all(tests) is True:
            for c in combs:
                test_key_obj.edit(**c)
                for text in expected_text:
                    print("\n- Character missing in read k-fyle and present in object printout"
                          "\n+ Character present in object printout and missing in read k-fyle")
                    print(find_string_difference(str(test_key_obj), text))
                    print("------------------------------------------------------")
        assert all(tests) is True
        
# ... keyword with scalar and vectorial cards conditionally presents
def test_keyword_str_mixed_optional(test_mixed_optional):
    expected_text = open_kfile("TEST_MIXED_OPTIONAL")
    test_key_obj = test_mixed_optional
    print("\nRead k-file:")
    [print(text) for text in expected_text]
    combs = possible_card_combination(test_key_obj)
    print("\nTested keywords:")
    if not combs:
        print(test_key_obj)
        assert compare_keyobj_keytext(test_key_obj, expected_text[0]) is True
    else:
        tests = []
        for c in combs:
            test_key_obj.edit(**c)
            
            single_test = False
            for text in expected_text:
                print(test_key_obj)
                print("------------------------------------------------------")
                if compare_keyobj_keytext(test_key_obj, text) is True:
                    print("True")
                    single_test = True
                    break
            tests.append(single_test)
            
        # Print comparison between text and object -> help finding differences
        if not all(tests) is True:
            for c in combs:
                test_key_obj.edit(**c)
                for text in expected_text:
                    print("\n- Character missing in read k-fyle and present in object printout"
                          "\n+ Character present in object printout and missing in read k-fyle")
                    print(find_string_difference(str(test_key_obj), text))
                    print("------------------------------------------------------")
        assert all(tests) is True
