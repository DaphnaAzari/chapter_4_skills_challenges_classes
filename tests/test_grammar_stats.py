import pytest
from lib.grammar_stats import GrammarStats

#Given a string that starts with cap letter
#and ends in correct punctuation mark
#return True

def test_text_starts_with_cap_and_ends_with_exclamation():
    grammar_stats = GrammarStats()
    result = grammar_stats.check("Hello dude!") 
    assert result == True

    #  Given a correct string that begins with a capital letter and 
    #full stop

def test_with_correct_grammar_full_stop():
    grammar_stats = GrammarStats()
    result = grammar_stats.check("Hello dude.") 
    assert result == True

 #  Given a correct string that begins with a capital letter and 
    #full stop

def test_with_correct_grammar_question_mark():
    grammar_stats = GrammarStats()
    result = grammar_stats.check("Hello dude?") 
    assert result == True

 # Given a correct string that begins with a capital letter
 #but missing punc

def test_with_correct_grammar_but_missing__punc_mark():
    grammar_stats = GrammarStats()
    result = grammar_stats.check("Hello dude") 
    assert result == False


# Given a string with a capital letter but with a comma (incorrect
# punctuation mark):

def test_without_cap_and_without_punc_mark():
    grammar_stats = GrammarStats()
    result = grammar_stats.check("hello dude") 
    assert result == False

# Given a string with a capital letter but with a comma (incorrect
# punctuation mark):

def test_with_cap_and_with_comma():
    grammar_stats = GrammarStats()
    result = grammar_stats.check("Hello dude,") 
    assert result == False

# Given a string without a capital letter but with the correct
# punctuation marks:

def test_without_cap_but_with_correct_punc_exclation():
    grammar_stats = GrammarStats()
    result = grammar_stats.check("hello dude!") 
    assert result == False



def test_given_an_empty_string_raises_err():
    grammar_stats = GrammarStats()
    with pytest.raises(Exception) as e:
        grammar_stats.check("") 
    assert str(e.value) == "Can't check the grammar of an empty string."

# Given a an integer: 
# Raises error with error_message 

def test_given_a_string_of_integers_raises_err():
    grammar_stats = GrammarStats()
    with pytest.raises(Exception) as e:
        grammar_stats.check(123) 
    assert str(e.value) == "Input must be a string of text!"

#Given one text that is correct grammar
#returns percentage of 100%

def test_one_good_text():
    grammar_stats = GrammarStats()
    grammar_stats.check("Hello!")
    assert grammar_stats.percentage_good() == 100

#Given three texts that are correct grammar
#returns percentage of 100%
def test_the_good_texts():
    grammar_stats = GrammarStats()
    grammar_stats.check("Hello!")
    grammar_stats.check("Heya!")
    grammar_stats.check("Hi you!")
    assert grammar_stats.percentage_good() == 100

#Given one good grammar and one bad grammar texts
#returns percentage of 50%
def test_one_good_one_bad():
    grammar_stats = GrammarStats()
    grammar_stats.check("Hello!")
    grammar_stats.check("Heya")
    assert grammar_stats.percentage_good() == 50

#Given one bad grammar text
#returns percentage of 0%
def test_only_bad_text():
    grammar_stats = GrammarStats()
    grammar_stats.check("Hello")
    assert grammar_stats.percentage_good() == 0


#Given no text was entered to the check method
#should throw and exception

def test_no_text_was_entered():
    grammar_stats = GrammarStats()
    with pytest.raises(Exception) as e:
        grammar_stats.percentage_good()
    assert str(e.value) == "No texts have been validated!"
    