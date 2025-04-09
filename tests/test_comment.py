##############################################################################
# Author: Paolo Ascia                                                        
# Date: February 2025                                                        
##############################################################################

##############################################################################
# imports
##########
import pytest
from PyDynasty.comment import comment

# fixture with a comment without comment symbol $
@pytest.fixture
def plain_comment():
    return comment("This is a plain comment. \n"
                   "And a second line of plain comment.")

# Test wrong input
def test_comment_error_input():
    with pytest.raises(TypeError):
        comment(4.)

# Test comment representation
def test_comment_representation(plain_comment):
    assert (isinstance(repr(plain_comment), str) and repr(plain_comment) == "LS-Dyna comment")

# Test comment printing
def test_comment_string(plain_comment):
    assert (isinstance(str(plain_comment), str) and str(plain_comment) == "$This is a plain comment. \n$And a second line of plain comment.")

# Test comment with comment symbol
def test_comment_string2():
    commented_comment = ("$This is a plain comment. \n"
                         "$And a second line of plain comment.")
    assert (isinstance(str(commented_comment), str) and str(commented_comment) == "$This is a plain comment. \n$And a second line of plain comment.")
