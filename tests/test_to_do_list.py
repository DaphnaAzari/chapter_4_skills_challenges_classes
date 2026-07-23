import pytest
from lib.to_do_list import ToDoList

# """
# Given one added task 
# #add_to_list adds to list
# """
def test_add_one_to_list():
    to_do_list = ToDoList()
    result = to_do_list.add_to_list("Walk the dog")
    assert  result == ["Walk the dog"]

# """
# Given two added tasks
# #add_to_list adds to list
# """
def test_add_two_to_list():
    to_do_list = ToDoList()
    to_do_list.add_to_list("Walk the dog")
    result = to_do_list.add_to_list("wash dishes")
    assert result == ["Walk the dog", "wash dishes"]

# Given a task made with no alphambetical letters (e.g. "???" or "")
# #add_to_list should throw an error
# """
def test_no_alpha_throws_err():
    to_do_list = ToDoList()
    with pytest.raises(Exception) as e:
        to_do_list.add_to_list("???")
    assert str(e.value) == "You've attempted to add an invalid task to the list, please try again!"


# Given a task made with an emptry string
# #add_to_list should throw an error
# """
# def test_empty_string_throws_err():
#     to_do_list = ToDoList()
#     with pytest.raises(Exception) as e:
#         to_do_list.add_to_list("")
#     assert str(e.value) == "You've attempted to add an empty task to the list, please try again!"

# ```
# """
# Given one completed task 
# #mark_task_as_complete removes from list and displays the final list
# """
def test_remove_one_task_from_list():
    to_do_list = ToDoList()
    to_do_list.add_to_list ("Walk the dog")
    to_do_list.add_to_list ("Wash dishes")
    result = to_do_list.mark_task_as_complete("Walk the dog")
    assert result == ["Wash dishes"]

# """
# Given three completed task 
# #mark_task_as_complete removes two from list and displays the final list
# """
def test_remove_two_tasks_from_list():
    to_do_list = ToDoList()
    to_do_list.add_to_list ("Walk the dog")
    to_do_list.add_to_list ("Wash dishes")
    to_do_list.add_to_list ("Wash the floor")
    to_do_list.mark_task_as_complete("Wash dishes")
    result = to_do_list.mark_task_as_complete("Walk the dog")
    assert result == ["Wash the floor"]

# """
# Given user tries to remove one empty task 
# #mark_task_as_complete should throw an err
# """


def test_remove_one_empty_task_from_list():
    to_do_list = ToDoList()
    to_do_list.add_to_list ("Walk the dog")
    to_do_list.add_to_list ("Wash dishes")
    with pytest.raises(Exception) as e:
        to_do_list.mark_task_as_complete("")
    assert str(e.value) ==  "You've attempted to remove an empty task from the list, please try again!"


# Given user tries to remove a task that is not on the to do list 
# #mark_task_as_complete should throw an err
# """
def test_remove_a_task__that_isnt_in_list():
    to_do_list = ToDoList()
    with pytest.raises(Exception) as e:
        to_do_list.add_to_list ("Walk the dog")
        to_do_list.add_to_list ("Wash dishes")
        to_do_list.mark_task_as_complete("Wash the floor")
    assert str(e.value) ==  "You've attempted to remove a task that is not on the list, please try again!" 

