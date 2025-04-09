##############################################################################
# Author: Paolo Ascia                                                        
# Date: February 2025                                                        
##############################################################################     

##############################################################################
# imports
##########
import difflib
from importlib.resources import files
from itertools import combinations
import os
import pytest
from PyDynasty import keyword

# Find all available cards
rel_path = os.path.join("KEYWORDS")  
file_path = files("PyDynasty").joinpath(rel_path)
# file_path = os.path.join(os.getcwd(), "PyDynasty", rel_path)

key_classes_dir = os.listdir(file_path)

keywords = []

for class_ in key_classes_dir:
    rel_path = os.path.join("KEYWORDS", class_)
    file_path = files("PyDynasty").joinpath(rel_path)
    # file_path = os.path.join(os.getcwd(), "PyDynasty", rel_path)
    
    for key in os.listdir(file_path):
        keywords.append(key[:-5])

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
        
        # Open k file 
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

@pytest.mark.parametrize("keyword_name", keywords)
   
# Test string output of all keywords available in the package
def test_keywords(keyword_name):
    print("\n")
    expected_text = open_kfile(keyword_name)
    test_key_obj = keyword(keyword_name)
    # print("\nRead k-file:")
    # [print(text) for text in expected_text]
    combs = possible_card_combination(test_key_obj)
    # print("\nTested keywords:")
    if not combs:
        # print(test_key_obj)
        if compare_keyobj_keytext(test_key_obj, expected_text[0]) is True:
            print(f"{keyword_name}: passed")
        else:
            print(f"{keyword_name}: failed")
            print(str(test_key_obj))
            print(expected_text[0])
            print("\n- Character missing in read k-fyle and present in object printout"
                  "\n+ Character present in object printout and missing in read k-fyle")
            print(find_string_difference(str(test_key_obj), expected_text[0]))
            print("------------------------------------------------------")
        assert compare_keyobj_keytext(test_key_obj, expected_text[0]) is True
    else:
        tests = []
        for c in combs:
            test_key_obj.edit(**c)
            
            single_test = False
            for text in expected_text:
                # print(test_key_obj)
                # print("------------------------------------------------------")
                if compare_keyobj_keytext(test_key_obj, text) is True:
                    # print("True")
                    single_test = True
                    break
            tests.append(single_test)
            
        # Print comparison between text and object -> help finding differences
        if all(tests) is True:
            print(f"{keyword_name}: passed")
        else:
            print(f"{keyword_name}: failed")
            for c in combs:
                test_key_obj.edit(**c)
                for text in expected_text:
                    print("\n- Character missing in read k-fyle and present in object printout"
                          "\n+ Character present in object printout and missing in read k-fyle")
                    print(find_string_difference(str(test_key_obj), text))
                    print("------------------------------------------------------")
        assert all(tests) is True