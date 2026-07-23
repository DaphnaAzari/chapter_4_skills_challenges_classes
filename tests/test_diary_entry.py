import pytest
from lib.diary_entry import DiaryEntry

# Given a title and contents
# format returns a formatted entry like:
# "My Title: These are the contents"

def test_formats_with_title_and_contents():
    diary_entry = DiaryEntry("My Title","Some contents")
    result = diary_entry.format()
    assert result == "My Title: Some contents"

    # Given a title and contents
# count_words returns the number of words in the title
# and contents"
def test_counts_words_in_both_title_and_contents():
    diary_entry = DiaryEntry("My Title","Some contents")
    result = diary_entry.count_words()
    assert result == 4

# # Given an empty title and contents
# # count_words raises an error

# def test_errors_on_empty_title_and_contents():
#     with pytest.raises(Exception) as err:
#         DiaryEntry("", "")
#     assert str(err.value) == "Diary entries must have or contents"

# Given an empty title
# count_words raises an error

def test_errors_on_empty_title():
    with pytest.raises(Exception) as err:
        DiaryEntry("", "my contents")
    assert str(err.value) == "Diary entries must have a title or contents"

# Given an empty  contents
# count_words raises an error

def test_errors_on_empty_contents():
    with pytest.raises(Exception) as err:
        DiaryEntry("My Title", "")
    assert str(err.value) == "Diary entries must have a title or contents"

# Given a wpm of 2
#And a text with 2 words
# reading_time returns 1 min

def test_reading_time_with_two_wpm_and_two_words():
    diary_entry = DiaryEntry("My Title", "one two")
    result = diary_entry.reading_time(2)
    assert result == 1

# Given a wpm of 2
#And a text with 4 words
# reading_time returns 2 min

def test_reading_time_with_two_wpm_and_four_words():
    diary_entry = DiaryEntry("My Title", "one two three four")
    result = diary_entry.reading_time(2)
    assert result == 2

# Given a wpm of 2
#And a text with 3 words
# reading_time returns 2 min

def test_reading_time_with_two_wpm_and_three_words():
    diary_entry = DiaryEntry("My Title", "one two three")
    result = diary_entry.reading_time(2)
    assert result == 2

# Given a wpm of 0
#reading_time Raises an err

def test_reading_time_errors_on_empty_wpm():
    diary_entry = DiaryEntry("My Title", "one two three")
    with pytest.raises(Exception) as err:
        diary_entry.reading_time(0)
    assert str(err.value) == "Cannot calculate a reading time with a wpm of 0"

# Given a contents of 6 words
# And a wpm of 2
#and a minutes of 1
#reading_chunk returns the first 2 words

def test_reading_chunk_with_two_wpm_and_one_minute():
    diary_entry = DiaryEntry("My Title", "one two three four five six")
    result = diary_entry.reading_chunk(2,1)
    assert result == "one two"

# Given a contents of 6 words
# And a wpm of 2
#and a minutes of 2
#reading_chunk returns the first 4words

def test_reading_chunk_with_two_wpm_and_two_minutes():
    diary_entry = DiaryEntry("My Title", "one two three four five six")
    result = diary_entry.reading_chunk(2,2)
    assert result == "one two three four"

# Given a contents of 6 words
# And a wpm of 2  and 1 minute
#first time, reading_chunk returns "one two"
#next time returns "three four"

def test_reading_chunk_with_two_wpm_and_one_minute_called_twice():
    diary_entry = DiaryEntry("My Title", "one two three four five six")
    assert diary_entry.reading_chunk(2,1) == "one two"
    assert diary_entry.reading_chunk(2,1) == "three four"

# Given a contents of 6 words
#First time reading chunck(2,1) returns "one two"
#Next time reading chunck(1,1) returns "three four"
#Next time reading chunck(2,1) returns "three four"

def test_reading_chunk_with_two_wpm_and_one_minute_called_multiple_times():
    diary_entry = DiaryEntry("My Title", "one two three four five six")
    assert diary_entry.reading_chunk(2,1) == "one two"
    assert diary_entry.reading_chunk(1,1) == "three"
    assert diary_entry.reading_chunk(2,1) == "four five"


#Given a contents of 6 words
#If reading_chunk is called repeatedly
#The last chunck is the last words in the text, even if 
#shorter than could be read
#The next chunk after this is at the start again

def test_reading_chunk_wraps_around_on_multiple_calls():
    diary_entry = DiaryEntry("My Title", "one two three four five six")
    assert diary_entry.reading_chunk(2,2) == "one two three four"
    assert diary_entry.reading_chunk(2,2) == "five six"
    assert diary_entry.reading_chunk(2,2) == "one two three four"

#Given a contents of 6 words
#If reading_chunk is called repeatedly with an exact ending
#The last chunck is the last words in the text
#The next chunk after this is at the start again

def test_reading_chunk_wraps_around_on_multiple_calls_with_exact_ending():
    diary_entry = DiaryEntry("My Title", "one two three four five six")
    assert diary_entry.reading_chunk(2,2) == "one two three four"
    assert diary_entry.reading_chunk(2,1) == "five six"
    assert diary_entry.reading_chunk(2,2) == "one two three four"
